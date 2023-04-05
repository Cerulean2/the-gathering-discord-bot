import discord
from discord.ext import commands
import sqlite3

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = sqlite3.connect('settings.db')
        self.db.execute('CREATE TABLE IF NOT EXISTS guild_settings (guild_id TEXT PRIMARY KEY, prefix TEXT)')
        self.db.commit()

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setprefix(self, ctx, prefix: str):
        """Sets the command prefix for this guild."""
        guild_id = str(ctx.guild.id)
        self.db.execute('INSERT OR REPLACE INTO guild_settings (guild_id, prefix) VALUES (?, ?)', (guild_id, prefix))
        self.db.commit()
        await ctx.send(f"Prefix set to `{prefix}`")

    def get_prefix(self, guild):
        """Returns the prefix for this guild."""
        guild_id = str(guild.id)
        result = self.db.execute('SELECT prefix FROM guild_settings WHERE guild_id = ?', (guild_id,))
        row = result.fetchone()
        if row is not None:
            return row[0]
        else:
            return '!'

    async def on_guild_remove(self, guild):
        """Deletes the settings for a guild when it leaves the bot."""
        guild_id = str(guild.id)
        self.db.execute('DELETE FROM guild_settings WHERE guild_id = ?', (guild_id,))
        self.db.commit()

    async def on_ready(self):
        """Prints a message when the bot is ready."""
        print(f'Logged in as {self.bot.user}')

    async def on_message(self, message):
        """Processes incoming messages."""
        prefix = self.get_prefix(message.guild)
        if message.content.startswith(prefix):
            ctx = await self.bot.get_context(message)
            await self.bot.invoke(ctx)

async def setup(bot):
    await bot.add_cog(Settings(bot))

