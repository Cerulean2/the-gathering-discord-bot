"""
A discord.py utility application made by Ceru#2976. 
This application is intended to help provide cleaner and more efficent information in the TG Server
Dependancies -- please see requirements.txt
"""

import discord, asyncio, os
from discord.ext import commands
from discord import Game, Status
from dotenv import load_dotenv

#Loads token | Sets application intents | Configures bot prefix
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print(f"Connected to {len(bot.guilds)} guild(s)")
    print("-------------------")

    # Load all cogs in the "cogs" folder
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded {filename}")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

    # Change application presence
    await bot.change_presence(status=Status.online, activity=Game(name="play.thegathering.net"))
    
@bot.event
async def on_command_error(ctx, error):
    """Sends an error message to a member when they do not have proper permissions to run a command."""
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.message.delete() # Delete the invoking command message
        embed = discord.Embed(title="Sorry, command denied! :no_entry:", description=f"{ctx.author.mention}, you do not have permission to use this command.", color=0xff0000)
        
        server_icon = ctx.guild.icon.url
        embed.set_footer(text="The Gathering", icon_url=server_icon)

        error_msg = await ctx.send(embed=embed)

        await asyncio.sleep(5) # Wait for 5 seconds!

        try:
            await error_msg.delete() # Delete the error message embed
        except:
            pass

@bot.event
async def on_member_join(member):
    """Adds a role when a member joins the guild."""
    role = member.guild.get_role(1092230821752082452) # Replace with the ID of your role
    await member.add_roles(role)

import discord
from discord.ext import commands

@bot.command()
async def support(ctx):
        """Provides information on how to get support for the bot."""
        embed = discord.Embed(title="Bot Support",
                            description="Need help with the bot? Here's how to get support:",
                            color=0x7289DA)
        
        embed.add_field(name="Join the Support Server",
                        value="[Invite Link](https://discord.gg/g5GF7rEwsm)",
                        inline=False)
        embed.add_field(name="Check the Documentation",
                        value="[Documentation Link](https://github.com/Cerulean2/the-gathering-discord-bot)",
                        inline=False)
        
        embed.add_field(name="Contact the Developer",
                        value="Send a direct message to the developer `Ceru#2976`",
                        inline=False)
        
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text="TheGathering | Made by Ceru#2976", icon_url=ctx.guild.icon.url)
        
        await ctx.send(embed=embed)

#Runs the bot application
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
