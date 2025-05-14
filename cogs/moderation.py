# Credits: R.O.D
# Moderation commands for the Discord Bot

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command: Kick a member
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member.name} has been kicked for: {reason}")
        except Exception as e:
            await ctx.send(f"Error: {e}")

    # Command: Ban a member
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member.name} has been banned for: {reason}")
        except Exception as e:
            await ctx.send(f"Error: {e}")

    # Command: Unban a member
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name):
        try:
            banned_users = await ctx.guild.bans()
            for ban_entry in banned_users:
                user = ban_entry.user
                if user.name == member_name:
                    await ctx.guild.unban(user)
                    await ctx.send(f"{user.name} has been unbanned.")
                    return
            await ctx.send(f"User {member_name} not found in ban list.")
        except Exception as e:
            await ctx.send(f"Error: {e}")

# Add the cog to the bot
def setup(bot):
    bot.add_cog(Moderation(bot))
