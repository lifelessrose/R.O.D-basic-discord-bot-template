# Credits: R.O.D
# Event handlers for the Discord Bot

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Event: When the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is ready and logged in as {self.bot.user}!")

    # Event: When a member joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} has joined the server.")
        # Send a welcome message (optional)
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome to the server, {member.mention}!")

    # Event: When a member leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member.name} has left the server.")

# Add the cog to the bot
def setup(bot):
    bot.add_cog(Events(bot))
