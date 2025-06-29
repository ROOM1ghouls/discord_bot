import asyncio

import discord
import config
from bot.api import analyze_message, transform_with_openai
from bot.webhook import send_as_user

settings = config.settings

MAX_QUEUE        = 1_000     # 버퍼 크기
MAX_CONCURRENT   = 3         # 동시에 백엔드/OpenAI 몇 개까지?

class MyBot(discord.Client):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.msg_q: asyncio.Queue[discord.Message] = asyncio.Queue(MAX_QUEUE)
        self.sem = asyncio.Semaphore(MAX_CONCURRENT)
        self.worker_task = None  # 아직 워커 태스크는 만들지 않음

    async def setup_hook(self):
        # 여기가 비동기 초기화 구역입니다!
        self.worker_task = asyncio.create_task(self._worker())
    async def on_ready(self):
        print(f"[Bot Ready] Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        try:
            self.msg_q.put_nowait(message)  # ➜ 큐에 적재하고 바로 복귀
        except asyncio.QueueFull:
            await message.channel.send(
                "⚠️ 필터 대기열이 가득 찼습니다. 잠시 후 다시 시도해 주세요!",
                delete_after=5
            )

    async def _worker(self):
        while True:
            msg = await self.msg_q.get()
            self.loop.create_task(self._handle(msg))  # 메시지마다 별도 태스크
            self.msg_q.task_done()

    async def _handle(self, msg: discord.Message):
        async with self.sem:  # 동시 처리량 제한
            res = await analyze_message(msg.content, msg.guild.id, msg.author.id)
            if not res["is_abusive"]:
                return

            try:
                await msg.delete()
            except discord.HTTPException:
                pass

            username = f"{msg.author.display_name} ({res['updated_score']:.3f}점)"
            proxy_msg = await send_as_user(msg.channel, msg.author, "⚠️ 악플 검열 중입니다…", override_name=username)
            sanitized = await transform_with_openai(msg.content)
            await proxy_msg.edit(content=sanitized)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True  # 유저 메시지 읽기 권한 활성화
    bot = MyBot(intents=intents)
    bot.run(settings["DISCORD_TOKEN"])
