import discord
from discord.ext import commands
import random,requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Responds with Pong!"""
        message = await ctx.send("Pong!")
        await message.add_reaction("🏓")

    @commands.command()
    async def roll(self, ctx, dice: str = ''):
        """Rolls a dice in NdN format."""
        if not dice:
            embed = discord.Embed(title="How to use the roll command",
                                  description="The roll command lets you roll a dice in NdN format. For example, to roll two six-sided dice, type `!roll 2d6`. Here are some examples:",
                                  color=discord.Color.blue())
            embed.add_field(name="Roll two six-sided dice", value="!roll 2d6", inline=False)
            embed.add_field(name="Roll a twenty-sided die", value="!roll 1d20", inline=False)
            embed.add_field(name="Roll three four-sided dice", value="!roll 3d4", inline=False)
            embed.set_footer(text="TheGathering | Made by Ceru#2976",icon_url=ctx.guild.icon.url)
            await ctx.send(embed=embed)
            return

        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def flip(self, ctx):
        """Flips a coin and returns Heads or Tails."""
        await ctx.send(random.choice(['Heads!', 'Tails!']))

    @commands.command()
    async def say(self, ctx, *, message):
        """Repeats a message."""
        await ctx.send(message)

    @commands.command()
    async def quote(self, ctx):
        """Responds with a random famous quote."""
        try:
            response = requests.get('https://api.quotable.io/random')
            data = response.json()
            content = f"{data['content']} -{data['author']}"
            await ctx.send(content)
        except Exception as e:
            print(f"An error occurred while fetching the quote: {e}")

    @commands.command()
    async def meme(self,ctx):
        """Generates a random meme."""
        try:
            response = requests.get('https://meme-api.com/gimme')
            data = response.json()
            meme_url = data['url']
            embed = discord.Embed(title='Random Meme', color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=meme_url)
            await ctx.send(embed=embed)
        except Exception as e:

            print(f"An error occurred while fetching the meme: {e}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
