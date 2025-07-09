# bot.py

from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Bot is alive!"

@app.route("/health")
def health():
    return "OK", 200

# Run Flask on a separate thread
def run_web():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run_web).start()

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Get token from .env
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("❌ DISCORD_BOT_TOKEN is not set in environment.")

bot.run(DISCORD_TOKEN)