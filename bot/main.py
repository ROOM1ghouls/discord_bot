import discord
from config import settings
from bot.api import analyze_message

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"[Bot Ready] Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        # 메시지 분석
        result = await analyze_message(message.content)

        if result["is_abusive"]:
            try:
                await message.delete()
            except discord.Forbidden:
                print("[Warning] 메시지 삭제 권한이 없습니다.")

            # 검열된 메시지 출력
            sanitized = result["sanitized"]
            username = message.author.display_name
            await message.channel.send(f"{username}: {sanitized}")

        else:
            # 욕설이 아니라면 아무 반응도 하지 않음
            pass

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True  # 유저 메시지 읽기 권한 활성화
    bot = MyBot(intents=intents)
    bot.run(settings["DISCORD_TOKEN"])
