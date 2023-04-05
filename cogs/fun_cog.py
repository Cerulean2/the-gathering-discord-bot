import discord
from discord.ext import commands
import random 

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
        quotes = [
            "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
            "The way to get started is to quit talking and begin doing. -Walt Disney",
            "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
            "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
            "Life is what happens when you're busy making other plans. -John Lennon",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
            "When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt",
            "In the end, it's not the years in your life that count. It's the life in your years. -Abraham Lincoln",
            "Believe you can and you're halfway there. -Theodore Roosevelt"
        ]
        await ctx.send(random.choice(quotes))

async def setup(bot):
    await bot.add_cog(Fun(bot))
