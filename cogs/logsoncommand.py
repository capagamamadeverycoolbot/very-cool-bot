from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f"📘 {ctx.author} used command: {ctx.command}")

async def setup(bot):
    await bot.add_cog(Logging(bot))