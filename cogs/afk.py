from discord.ext import commands
import discord

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}

    @commands.command()
    async def afk(self, ctx):
        member = ctx.author
        current_nick = member.nick or member.name
        if member.id not in self.afk_users:
            new_nick = f"{current_nick} AFK"
            self.afk_users[member.id] = current_nick
            try:
                await member.edit(nick=new_nick)
                await ctx.send(f"🔕 {member.mention} is now AFK.")
            except discord.Forbidden:
                await ctx.send("❌ I don't have permission to change your nickname.")
        else:
            # Remove AFK
            original_nick = self.afk_users.pop(member.id)
            try:
                await member.edit(nick=original_nick)
                await ctx.send(f"🔔 {member.mention} is no longer AFK.")
            except discord.Forbidden:
                await ctx.send("❌ I couldn't revert your nickname.")

async def setup(bot):
    await bot.add_cog(AFK(bot))