from .customslash import customslash


async def setup(bot):
    await bot.add_cog(customslash(bot))