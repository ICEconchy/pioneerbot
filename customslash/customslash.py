from redbot.core import commands
import discord


class customslash(commands.Cog):
    def __init__(self bot):
        self.bot = bot
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def customslash(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command()
    async def close(self, ctx):
        await ctx.send("!reacticket close")

def setup(bot):
    bot.add_cog(customslash(bot))