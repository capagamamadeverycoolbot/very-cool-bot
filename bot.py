import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import app

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

app.run(host="0.0.0.0", port=8080)

# at bottom of bot.py
if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))