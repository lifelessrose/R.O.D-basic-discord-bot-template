# Credits: R.O.D
# Main file for initializing and running the Discord Bot

import discord
from discord.ext import commands
import os
from config import BOT_TOKEN

# Intents for the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True  # For member join/leave events and moderation

# Create the bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")

# Load cogs from the cogs folder
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

# Run the bot using the token from config.py
bot.run(BOT_TOKEN)
