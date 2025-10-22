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

import json

WORDS_FILE = "words.json"

def load_words():
    if not os.path.exists(WORDS_FILE):
        return []
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_words(words):
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, indent=4, ensure_ascii=False)

@bot.command()
async def addword(ctx, word, type, meaning, example=None):
    words = load_words()
    for w in words:
        if w["word"] == word:
            await ctx.send(f":x: The word {word} already exists.")
            return
    new_word = {
        "word" : word,
        "type" : type,
        "meaning" : meaning,
        "example" : example or ""
    }
    words.append(new_word)
    save_words(words)
    await ctx.send(f":white_check_mark: Added word: {word} to dictionary.")

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
