# Credits: R.O.D
# Help command for the Discord Bot

from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command: Show help for commands
    @commands.command()
    async def help(self, ctx):
        help_message = """
**Moderation Bot Commands**:
- `!kick <@member> [reason]` - Kicks a member from the server.
- `!ban <@member> [reason]` - Bans a member from the server.
- `!unban <username>` - Unbans a member from the server.
- `!mute <@member> [reason]` - Mutes a member.
- `!unmute <@member>` - Unmutes a member.

**Events**:
- Welcomes new members and logs when members leave.
        """
        await ctx.send(help_message)

# Add the cog to the bot
def setup(bot):
    bot.add_cog(Help(bot))
