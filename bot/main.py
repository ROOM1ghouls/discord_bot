import discord
from config import settings
from bot.api import analyze_message, transform_with_openai
from bot.webhook import send_as_user
class MyBot(discord.Client):
    async def on_ready(self):
        print(f"[Bot Ready] Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        result = await analyze_message(
            content=message.content,
            server_id=message.guild.id,
            user_id=message.author.id
        )

        if result["is_abusive"]:
            score = result["updated_score"]
            username = f"{message.author.display_name} ({score}점)"

            await message.delete()

            temp_msg = await message.channel.send(
                content="⚠️ 악플 검열 중입니다...",
            )

            transformed = await transform_with_openai(message.content)

            await temp_msg.delete()

            await send_as_user(
                message.channel,
                message.author,
                content=transformed,
                override_name=username
            )

        else:
            # 욕설이 아닌 경우 아무 처리도 하지 않음
            pass

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True  # 유저 메시지 읽기 권한 활성화
    bot = MyBot(intents=intents)
    bot.run(settings["DISCORD_TOKEN"])
