import discord
from config import settings

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"[Bot Ready] Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        await message.channel.send("hi")

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True  # 유저 메시지 읽기 권한 활성화
    bot = MyBot(intents=intents)
    bot.run(settings["DISCORD_TOKEN"])
