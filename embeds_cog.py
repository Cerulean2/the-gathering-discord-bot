import discord
from discord.ext import commands
import random 

class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Community Manager')
    async def apply_staff(self,ctx):
        
        """Creates an embed containing information about applying for a staff position"""
        # Delete the invoking command message
        await ctx.message.delete()
        
        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "Staff Application Information":
                        await message.delete()
        except Exception as e:
            print("An error occured",e)

        
        embed = discord.Embed(title="Staff Application Information", description="__Some general rules to know about applying:__", color=0x7289da)
        embed.add_field(name="Lengthy Answers Required :speech_balloon:", value="We require you to provide lengthy answers that will let us have a look inside your mind. Please make sure your answers are at least 300 characters long.", inline=False)
        embed.add_field(name="Activity Required :shield:", value="Being on the staff team means you are responsible for moderating the server and helping players with any questions they might have. To do that efficiently and professionally you are required to join the discord server to keep up with the updates we put out and always have up-to-date information regarding the server!", inline=False)
        embed.add_field(name="Microphone Required :microphone:", value="We will be briefing our staff members regarding updates, future plans, changes and other stuff through calls / voice chats occasionally on Discord. To take part in all this you need to have a working microphone.", inline=False)
        embed.add_field(name="Age Requirement :underage:", value="You must be at least 16 years old to apply for staff on our server. We believe that being staff requires a degree of maturity and a friendly demeanor is crucial to being a member of the staff team.", inline=False)
        embed.add_field(name="Application Form :information_source:", value=f"If you meet the requirements above and are interested in applying, please fill out our [application form](https://docs.google.com/forms/d/1ZNxVXd76ZwnYzhvBVI0zFkRcMESAmVLZFvZ6jQ/viewform?edit_requested=true).", inline=False)
        
        embed.set_thumbnail(url=ctx.guild.icon.url)
        
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.has_role('Community Manager')
    async def apply_developer(self,ctx):
        """Creates an embed containing information about applying for a developer position"""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        async for message in ctx.channel.history():
            if message.author == ctx.author and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Developer Application Information":
                    await message.delete()

        embed = discord.Embed(title="Developer Application Information", description="__Some general rules to know about applying:__", color=0x7289da)
        embed.add_field(name="Lengthy Answers Required :speech_balloon:", value="We require you to provide lengthy answers that will let us have a look inside your mind. Please make sure your answers are at least 300 characters long.", inline=False)
        embed.add_field(name="Clean and lightweight plugins :feather:", value="Writing plugins using a clean syntax & format is essential for them to work without having too much bloat. You must be able to create plugins that don't hog server resources and are lightweight.", inline=False)
        embed.add_field(name="Knowledgeable about Minecraft :brain:", value="As a developer, you should have a good understanding of Minecraft, including its mechanics, commands, and plugins. This knowledge will enable you to create custom plugins, troubleshoot issues, and provide technical support to players.", inline=False)
        embed.add_field(name="Communication skills :speaking_head:", value="Communication is an essential skill for any staff member, especially for developers. You should be able to communicate effectively with the server's management and other staff members, as well as with players who require technical support or have bug reports.", inline=False)
        embed.add_field(name="Show initiative and creativity :art:", value="As a developer, you should be proactive in identifying opportunities for improving the server, whether it be through new plugins or creative solutions to existing problems. Being able to think outside the box and propose innovative solutions will make you an important member of our staff team.", inline=False)
        embed.add_field(name="Be prepared to work as part of a team :man_technologist:", value="Being a staff member is not a solo endeavor, and you should be prepared to work with other staff members to achieve the server's goals. This includes collaborating with other developers, moderators, and administrators to maintain the server's stability, security, and fun factor.", inline=False)
        embed.add_field(name="Application Form :information_source:", value=f"If you meet the requirements above and are interested in applying, please fill out our [application form](https://docs.google.com/forms/d/1xMQsKXwxzdsbfa5AxRcXlAoqJTqn8c/viewform?edit_requested=true).", inline=False)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def apply_builder(self,ctx):
        """Creates an embed containing information about applying for a builder position"""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        async for message in ctx.channel.history():
            if message.author == ctx.author and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Builder Application Information":
                    await message.delete()

        embed = discord.Embed(title="Builder Application Information", description="__Some general rules to know about applying:__", color=0x7289da)
        embed.add_field(name="Lengthy Answers Required :speech_balloon:", value="We require you to provide lengthy answers that will let us have a look inside your mind. Please make sure your answers are at least 300 characters long.", inline=False)
        embed.add_field(name="You must actually know how to build well :construction_worker:", value="The things you will be building for Eternity will be representative of a part of our server's reputation & all our community members and players will see your builds, therefore, you need to know what you are doing and build premium quality stuff.", inline=False)
        embed.add_field(name="You must create original work :compass:", value="You are not allowed to copy a build or use it during your portfolio presentation. Everything that you build must be original. While you are allowed to take inspiration from other peoples' work, you are not allowed to steal it and pass it off as your own work.", inline=False)
        embed.add_field(name="You must keep us up-to-date with builds that are in-progress :date:", value=" If you are asked by us to build something that will be used on the server, you must keep us up-to-date with the progress of the build. Informing us about things such as how long the build will take to finish or if you are unsure about something is essential. If you can't decide in what way to build something or have other questions about the project you are assigned to, let us know. ", inline=False)
        embed.add_field(name="Application Form :information_source:", value=f"If you meet the requirements above and are interested in applying, please fill out our [application form](https://docs.google.com/forms/d/18lAPw33dcG329eOSeZrQuXqBaTty1pnjIk-g/viewform?edit_requested=true).", inline=False)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def staff_ranks(self,ctx):
        """Displays information about the server's staff ranks."""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        async for message in ctx.channel.history():
            if message.author == ctx.author and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Server Staff Ranks":
                    await message.delete()

        server_icon = ctx.guild.icon.url

        embed = discord.Embed(
            title="Server Staff Ranks",
            description="Below is a list of the server's staff ranks and their responsibilities.",
            color=0xD8BFD8  # Light pastel color
        )
        embed.set_thumbnail(url=server_icon)
        embed.add_field(
            name=":crown: Owner",
            value="The owner is responsible for the overall management and development of the server. They have the final say in all matters and can overrule any decision made within the team where they see necessary.",
            inline=False
        )
        embed.add_field(
            name=":busts_in_silhouette: Community Manager",
            value="The community manager is responsible for the community aspect of the server. They prioritize making the server a luxurious place for both players and staff. They handle staff disputes and staff/player reports, and work closely with the Owners and Developers. Community Managers enforce and may tweak server rules. They have the final say in staff matters, and can overrule decisions made by the staff team if they feel it will benefit the server or players.",
            inline=False
        )
        embed.add_field(
            name=":star: Staff Manager",
            value="The staff manager is the leader of the staff team. They oversee promotion and recruitment of staff, and help train new members of the team. The staff manager's focus should be placed mainly on the staff team to ensure that the team provides the best support for the player base. Staff issues within the team should usually be reported directly to the staff manager to deal with.",
            inline=False
        )
        embed.add_field(
            name=":shield: Admin",
            value="Admins are the highest rank of junior staff. They work alongside the staff manager to help train new staff members. They hold a key role in enforcement of rules within the server and player support. Earning Admin allows you to build permissions from that of a Moderator/Senior-Moderator and handle most in-game matters for players.",
            inline=False
        )
        embed.add_field(
            name=":small_blue_diamond: Jr. Admin",
            value="Jr. Admins are experienced moderators who have demonstrated exceptional skills in their duties and are capable of handling a larger set of permissions. They work closely with the Admins and Staff Manager to help train and mentor new staff members, and assist in handling more complex player support issues.",
            inline=False
        )
        embed.add_field(
            name=":diamond_shape_with_a_dot_inside: Senior Moderator",
            value="Senior-Moderators have shown that they are incredibly capable as moderators and can help train new staff to reach a similar level. They understand seamlessly the rules and punishments for rule-breaks. As a Senior-Mod, you should be willing to be assigned new staff members to train directly at the start of their time on the team.",
            inline=False
        )
        embed.add_field(
            name=":hammer: Moderator",
            value="Earning moderator is the first promotion you may earn within the team. It is a step-up from Trial-Mod showing you have learned the processes a staff member should undergo when handling rule-breaks, player disputes and general community issues. Moderators are granted access to banning and kicking players in-game for situations such as utilization of hacked clients.",
            inline=False
        )
        embed.add_field(
            name=":clipboard: Helper",
            value="This rank is the first rank gained when applying for staff. It's a trial rank for managers to see your commitment, activity and community involvement on the server. The rank also stands to help you in adapting into the team comfortably with close training with a Senior-Moderator, Admin or Staff Manager. Helpers will only be given access to mute players in-game as well as other smaller general staff permissions to encourage new staff to earn their place in the team. Remember, you're encouraged to ask questions in this position, especially if you're not sure about something, that's what the management is there for!",
            inline=False)

        embed.set_footer(text="Note: Only management positions and owners are authorized to make demotions, promotions, and recruitments within the staff team.")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def dev_ranks(self,ctx):
        """Displays information about the server's developement ranks."""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "Server Development Positions":
                        await message.delete()
        except Exception as e:
            print(f"An error occurred: {e}")
                    
        server_icon = ctx.guild.icon.url
        try:
            embed = discord.Embed(
                title="Server Development Positions",
                color=0xD8BFD8,
            )

            if server_icon:
                embed.set_thumbnail(url=server_icon)

            embed.add_field(
                name=":hammer: Server Developers",
                value="The server developers are responsible for the server's development on various platforms, including in-game development and website/store development. They work closely with the Owners to provide a seamless experience for players, handling plugin creation and management. Discord developers also ensure smooth communication on the server.",
                inline=False
            )
            embed.add_field(
                name=":construction_worker: Server Builder",
                value="Builders  create the wonderful builds that give our server its unique touch. With a creative mindset, they design impressive structures and landscapes that enhance the player experience.",
                inline=False)
                    
            embed.set_footer(text="Note: Development roles do not grant moderation permissions. To participate in both moderation and development, separate applications are required.")
            await ctx.send(embed=embed)
        except Exception as e:
            print(f"An error occurred: {e}")

    @commands.command()
    @commands.has_role('Community Manager')
    async def discord_rules(self,ctx):
        """Displays information about the server's discord rules."""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "📜 Server Rules":
                        await message.delete()
        except Exception as e:
            print(f"An error occurred: {e}")

        embed = discord.Embed(title="📜 Server Rules", 
                            description="Please read the following rules before participating in our Discord community.", 
                            color=0xE6C7B8)
                
        server_icon = ctx.guild.icon.url
        if server_icon:
                embed.set_thumbnail(url=server_icon)
                        
        embed.add_field(name="🗨️ Chat Rules", 
                        value="1. Be respectful and considerate towards other members. Do not harass, bully, or discriminate against anyone. Treat others the way you want to be treated.\n2. Keep conversations appropriate for all ages. Do not use excessive profanity or post any NSFW content.\n3. Do not spam the chat or use excessive caps, emojis, or symbols. Use channels appropriately for their intended purposes.\n4. Do not ping members excessively or use @mentionable roles unless it is necessary and appropriate.\n5. Do not impersonate other members, staff, or management.\n6. Respect the server and players. Do not share exploits or gamebreaking bugs publicly on the server, spread misinformation, or promote any form of cheating or abusive content.\n7. Do not advertise other servers or external websites. Misc links are allowed if they are relevant and appropriate for the conversation.\n8. Follow the instructions of the staff members. Refusal to listen to staff may result in disciplinary actions.", inline=False)

        embed.add_field(name="🔊 Voice Rules", 
                        value="1. Do not cause disruptions in voice channels. Do not play loud noises or engage in excessive screaming or use any form of voice changing software.", inline=False)

        embed.add_field(name="📝 Discord Guidelines", 
                        value="1. Choose an appropriate name and avatar for your profile. \n2. Consistently using channels for the wrong purpose may result in disciplinary actions.\n3. Breaking Discord's Terms of Service is not allowed and will result in a permanent ban.", inline=False)

        embed.set_footer(text="Breaking any of these rules may result in disciplinary actions at the discretion of the staff. The severity of the disciplinary action will depend on the severity of the offense and the history of the member.")
                
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def gameplay_rules(self,ctx):
        """Displays information about the server's gameplay rules."""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "📜 Minecraft Server Rules":
                        await message.delete()
        except Exception as e:
            print(f"An error occurred: {e}")

        embed = discord.Embed(title="📜 Minecraft Server Rules", 
                            description="Please read the following rules before participating in our Discord community.", 
                            color=0xE6C7B8)

        server_icon = ctx.guild.icon.url
        if server_icon:
                embed.set_thumbnail(url=server_icon)
                        
        # Embed for Minecraft server rules
        embed = discord.Embed(title="📜 Minecraft Server Rules", 
                            description="Please read the following rules before participating in our Minecraft server community.", 
                            color=0x87CEFA)
                
        embed.add_field(name="👉 Click here to view the Minecraft server rules", 
                        value="[Minecraft Server Rules Forum Post](https://example.com/minecraft-rules)", inline=False)

        embed.set_footer(text="Breaking any of these rules may result in disciplinary actions at the discretion of the staff. The severity of the disciplinary action will depend on the severity of the offense and the history of the member.")
            
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def tg_welcome(self,ctx):
        """Sends the TG Server welcome message as an embed."""
        # Delete the invoking command message
        await ctx.message.delete()
        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "🎉 Welcome to the Official TG Server Discord":
                        await message.delete()
        except Exception as e:
            print(f"An error occurred: {e}")

        embed = discord.Embed(title="🎉 Welcome to the Official TG Server Discord", 
                            description="Welcome to the TG Server Discord server! Join our community and experience a server like no other, with unique features and a friendly atmosphere that will keep you entertained for hours on end! \n\nOur Discord is your hub for all things related to the server, from important announcements and support issues to community discussions and events. We hope you enjoy your stay and become a part of our growing community!\n\n**We hope to see you soon!**", 
                            color=0xF7CAC9)
                
        server_icon = ctx.guild.icon.url
        if server_icon:
                embed.set_thumbnail(url=server_icon)

        embed.set_footer(text="TG Server | Made by Ceru#2976", icon_url=server_icon)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Community Manager')
    async def tg_links(self,ctx):
        """Sends the TG Server important links as an embed."""
        # Delete the invoking command message
        await ctx.message.delete()

        # Delete the previous embed message if there is one
        try:
            async for message in ctx.channel.history():
                if message.author == ctx.author and message.embeds:
                    embed = message.embeds[0]
                    if embed.title == "🔗 Important Links":
                        await message.delete()
        except Exception as e:
            print(f"An error occurred: {e}")
                    
        embed = discord.Embed(title="🔗 Important Links", 
                            description="Below is a list of important links to help you navigate the TG Server network.", 
                            color=0xF7CAC9)
                
        links = [
            {
                "name": "🎮 Server IP",
                "value": "`play.tgserver.net`"
            },
            {
                "name": "📖 Forums",
                "value": "[Click me](https://tgserver.net/forums)"
            },
            {
                "name": "🛒 Store",
                "value": "[Click me](https://tgserver.net/store)"
            },
            {
                "name": "📷 Tiktok",
                "value": "[Click me](https://www.tiktok.com/@tgserver)"
            },
            {
                "name": "🐦 Twitter",
                "value": "[Click me](https://twitter.com/tgserver)"
            },
            {
                "name": "🎲 Discord",
                "value": "[Click me](https://discord.gg/tgserver)"
            }
        ]
                
        for link in links:
            embed.add_field(name=link['name'], value=link['value'], inline=False)

        server_icon = ctx.guild.icon.url
        embed.set_footer(text="TheGathering | Made by Ceru#2976", icon_url=server_icon)

        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Embeds(bot))
