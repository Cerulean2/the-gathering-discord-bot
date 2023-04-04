import discord
from discord.ext import commands

class ModeratorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        """Kicks a member from the server"""
        if member is None:
            embed = discord.Embed(title="Missing Required Argument", description="Please specify a member for me to kick.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        if reason is None:
            embed = discord.Embed(title="Missing Required Argument", description="Please provide a reason for kicking the member.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        try:
            await member.kick(reason=reason)
            await ctx.send(f'{member} has been kicked from the server.')
        except discord.Forbidden:
            embed = discord.Embed(title="Insufficient Permissions", description="I don't have permission to kick that member.", color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        """Bans a member from the server"""
        if member is None:
            embed = discord.Embed(title="Missing Required Argument", description="Please specify a member for me to ban.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        if reason is None:
            embed = discord.Embed(title="Missing Required Argument", description="Please provide a reason for banning the member.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member} has been banned from the server.')
        except discord.Forbidden:
            embed = discord.Embed(title="Insufficient Permissions", description="I don't have permission to ban that member.", color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = None):
        """Delete a specified number of messages from the current channel."""
        if amount is None:
            embed = discord.Embed(title="Missing Required Argument", description="Please provide the number of messages to delete.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f":white_check_mark: Successfully deleted {amount} messages!", delete_after=10.0)

async def setup(bot):
    await bot.add_cog(ModeratorCog(bot))
