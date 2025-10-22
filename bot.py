import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Load token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Events
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Commands
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! 👋 I’m alive and ready!")

# Keep bot alive
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = threading.Thread(target=run)
    thread.start()

keep_alive()
bot.run(TOKEN)
