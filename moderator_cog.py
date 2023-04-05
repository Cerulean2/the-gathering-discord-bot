import discord
from discord.ext import commands
import json

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel = None
        self.msglog_channel = 1092957060980809800
        self.load_config()

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
                self.log_channel_id = data.get("log_channel_id")
        except FileNotFoundError:
            pass

    def save_config(self):
        data = {"log_channel_id": self.log_channel_id}
        with open("config.json", "w") as f:
            json.dump(data, f)

    @commands.command()
    @commands.has_role('Community Manager')
    async def log_channel(self, ctx, channel: discord.TextChannel):
        """Sets the channel for moderation logs"""
        self.log_channel_id = channel.id
        self.save_config()
        await ctx.send(f"The log channel has been set to {channel.mention}")

        #Console log
        print(f"The moderation log channel was set to {self.log_channel_id}.")

    async def log_action(self, action, moderator, member, reason):
        if self.log_channel_id is not None:
            log_channel = self.bot.get_channel(self.log_channel_id)
            if log_channel is not None:
                embed = discord.Embed(
                    title=f"{action.capitalize()}",
                    description=f"**Member:** {member.mention}\n**Moderator:** {moderator.mention}\n**Reason:** {reason}",
                    color=0x8ee299,
                )
                embed.set_author(name=moderator.display_name, icon_url=moderator.avatar.url)
                await log_channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        """Kicks a member from the server"""
        if member is None:
            embed = discord.Embed(title="Missing Required Argument :no_entry:", description=f"{ctx.author.mention}, Please specify a member for me to kick.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
            return
        if reason is None:
            embed = discord.Embed(title="Missing Required Argument :no_entry:", description=f"{ctx.author.mention}, Please provide a reason for kicking the member.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
            return
        try:
            await member.kick(reason=reason)
            await ctx.send(f'{member} has been kicked from the server.')
        except discord.Forbidden:
            embed = discord.Embed(title="Insufficient Permissions :no_entry:", description=f"{ctx.author.mention}, I don't have permission to kick that member.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
        try:
            await self.log_action("kick", ctx.author, member, reason)
        except Exception as e:
            print(f"An error occurred: {e}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        """Bans a member from the server"""
        if member is None:
            embed = discord.Embed(title="Missing Required Argument :no_entry:", description=f"{ctx.author.mention}, Please specify a member for me to ban.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
            return
        if reason is None:
            embed = discord.Embed(title="Missing Required Argument :no_entry:", description=f"{ctx.author.mention}, Please provide a reason for banning the member.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member} has been banned from the server.')
        except discord.Forbidden:
            embed = discord.Embed(title="Insufficient Permissions :no_entry:", description=f"{ctx.author.mention}, I don't have permission to ban that member.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
        try:
            await self.log_action("ban", ctx.author, member, reason)
        except Exception as e:
            print(f"An error occurred: {e}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = None):
        """Delete a specified number of messages from the current channel."""
        if amount is None:
            embed = discord.Embed(title="Missing Required Argument :no_entry:", description=f"{ctx.author.mention}, Please provide the number of messages to delete.", color=discord.Color.red())
            server_icon = ctx.guild.icon.url
            embed.set_footer(text="The Gathering", icon_url=server_icon)
            await ctx.send(embed=embed)
            return
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f":white_check_mark: Successfully deleted {amount} messages!", delete_after=10.0)

async def setup(bot):
    await bot.add_cog(Moderator(bot))
