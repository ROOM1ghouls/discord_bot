import asyncio
import discord
from config import settings
from bot.api import analyze_message
from bot.webhook import send_as_user
class MyBot(discord.Client):
    async def on_ready(self):
        print(f"[Bot Ready] Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        # 메시지 분석
        result = await analyze_message(message.content)


        if result["is_abusive"]:
            score = result["updated_score"]
            username = f"{message.author.display_name} ({score}점)"

            # 삭제와 전송을 동시에 수행
            await asyncio.gather(
                message.delete(),
                send_as_user(message.channel, message.author, result["sanitized"], override_name=username)
            )

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True  # 유저 메시지 읽기 권한 활성화
    bot = MyBot(intents=intents)
    bot.run(settings["DISCORD_TOKEN"])
