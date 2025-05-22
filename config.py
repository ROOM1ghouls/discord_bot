from dotenv import load_dotenv
import os

load_dotenv()

settings = {
    "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN")
}