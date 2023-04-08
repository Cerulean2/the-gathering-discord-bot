import discord
from discord.ext import commands
import asyncio

# Set your own prefix, bot title, bot description, and bottom info here
prefix = '!'
bot_title = 'The Gathering'
bot_description = 'A list of all the commands available on this server.'
bottom_info = 'If you have any questions please ask a member of our staff team.'
trashcan_emoji = '🗑️'

class Help(commands.Cog):
    """Help command"""
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')
        
    @commands.command(name='help', description='Shows this message', aliases=['h'])
    async def help_command(self, ctx, *commands):
        """The help command!"""
        # If there are no arguments, get a list of all cogs and commands, and display them
        if not commands:
            help_embed = discord.Embed(title=bot_title, description=bot_description, color=discord.Color.blurple())
            help_embed.set_thumbnail(url=self.bot.user.avatar.url)
            for cog in self.bot.cogs:
                commands = self.bot.get_cog(cog).get_commands()
                command_list = [command.name for command in commands if not command.hidden]
                if command_list:
                    command_list = '\n'.join(command_list)
                    help_embed.add_field(name=cog.capitalize(), value=f'```{command_list}```', inline=False)
            help_embed.set_footer(text=bottom_info)
            help_msg = await ctx.send(embed=help_embed)
            await help_msg.add_reaction(trashcan_emoji)
        else:
            # If an argument is passed, see if it's a cog or command name
            entity = self.bot.get_cog(commands[0]) or self.bot.get_command(commands[0])
            if not entity:
                await ctx.send(f'No such command or category: {commands[0]}')
                return

            # If it's a cog, list all its commands
            if isinstance(entity, commands.Cog):
                cog = entity
                help_embed = discord.Embed(title=f"{cog.qualified_name.capitalize()} Commands", description=cog.description or "", color=discord.Color.blurple())
                help_embed.set_thumbnail(url=self.bot.user.avatar_url)
                command_list = cog.get_commands()
                filtered_commands = [command for command in command_list if not command.hidden]
                for command in filtered_commands:
                    help_embed.add_field(name=f'{prefix}{command}', value=command.help or 'No help given', inline=False)
                help_msg = await ctx.send(embed=help_embed)
                await help_msg.add_reaction(trashcan_emoji)

            # If it's a command, show the command's help
            elif isinstance(entity, commands.Command):
                command = entity
                help_embed = discord.Embed(title=f"Help with `{prefix}{command}`", description=command.help or "", color=discord.Color.blurple())
                help_embed.set_thumbnail(url=self.bot.user.avatar_url)
                help_embed.add_field(name='Usage', value=f"`{prefix}{command} {command.signature}`")
                help_msg = await ctx.send(embed=help_embed)
                await help_msg.add_reaction(trashcan_emoji)

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == trashcan_emoji and reaction.message.id == help_msg.id
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            pass
        else:
            # Delete the invoking command message
            await ctx.message.delete()
            await help_msg.delete()

async def setup(bot):
    await bot.add_cog(Help(bot))

