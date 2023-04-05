import discord
from discord.ext import commands

class StaffList(commands.Cog):
    staff_roles = ['Owner', 'Community Manager', 'Staff Manager', 'Development Team', 'Admin', 'Jr-Admin', 'Sr-Moderator', 'Moderator', 'Helper', 'Builder']
    staff_info = {role: {'count': 0, 'members': []} for role in staff_roles}

    async def update_staff_info(self, guild):
        total_count = 0
        for role in guild.roles:
            if role.name in self.staff_roles:
                count = len(role.members)
                self.staff_info[role.name]['count'] = count
                self.staff_info[role.name]['members'] = [member.mention for member in role.members]
                total_count += count
        return total_count

    @commands.command()
    @commands.has_role('Community Manager')
    async def stafflist(self, ctx):
        """Displays the current list of The Gathering Team"""
        await ctx.message.delete()

        try:
            # Try to find an existing message with the same title
            async for message in ctx.channel.history():
                if message.author == ctx.me and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "TheGathering Staff":
                        await message.edit(embed=await self.create_staff_embed(ctx))
                        return
        except Exception as e:
            print("An error occured", e)

        # If no existing message was found, create a new one
        await ctx.send(embed=await self.create_staff_embed(ctx))

    async def create_staff_embed(self, ctx):
        total_count = await self.update_staff_info(ctx.guild)

        embed = discord.Embed(title="TheGathering Staff", color=0xF7CAC9)

        embed.description = f"Total of {total_count} staff members\n"

        for role in self.staff_roles:
            count = self.staff_info[role]['count']
            members = '\n'.join(self.staff_info[role]['members'])
            embed.add_field(name=f"{role} - {count}", value=f"{members}", inline=False)

        embed.set_footer(text="TheGathering | Made by Ceru#2976", icon_url=ctx.guild.icon.url)

        return embed

async def setup(bot):
    await bot.add_cog(StaffList(bot))
