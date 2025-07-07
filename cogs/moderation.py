from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} was kicked. Reason: {reason or 'No reason'}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member.mention} was banned. Reason: {reason or 'No reason'}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, name_with_tag):
        banned_users = await ctx.guild.bans()
        name, discriminator = name_with_tag.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == name and user.discriminator == discriminator:
                await ctx.guild.unban(user)
                await ctx.send(f"🕊️ {user} has been unbanned.")
                return
        await ctx.send("❌ User not found.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"🧹 Cleared {amount} messages.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))