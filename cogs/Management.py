import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
def is_target_role(ctx):
    return any(role.name == "Manager" for role in ctx.author.roles)

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timezones = {}
        self.guild_roles = {}
        self.file_path = os.path.join('/home/container/storage', 'timezones.json')
        self.guild_roles_path = os.path.join('/home/container/storage', 'guild_roles.json')
        self.load_timezones()
        self.load_guild_roles()

    def load_timezones(self):
        """Load the timezones from the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                self.timezones = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.timezones = {}

    def load_guild_roles(self):
        """Load the guild roles from the JSON file."""
        try:
            with open(self.guild_roles_path, 'r') as f:
                self.guild_roles = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.guild_roles = {}

    def save_timezones(self):
        """Save the timezones to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(self.timezones, f, indent=4)

    def save_guild_roles(self):
        """Save the guild roles to the JSON file."""
        with open(self.guild_roles_path, 'w') as f:
            json.dump(self.guild_roles, f, indent=4)
            
    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def auto_translate(self, ctx):
        """
        Explains how to use the Translator Bot
        """
        await ctx.send("# How to use Translator Bot\n## Try using it in <#1214775106019000380>")
        embed = discord.Embed(
            title='non-English speakers',
            description=f'- Type `/auto_translate` in any channel chat and hit send. This command will be hidden from everyone else in the channel.\n'
                      f'- The Translate bot will ask you to choose a language to translate to. Click the drop-down menu and select English (or your desired language).\n'
                      f'- Now you can write in any language in the channel chat, and the bot will auto-translate it.\n',
            color=0x0099ff
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1214621093311025223/1214771696041594930/image.png?ex=65fa534d&is=65e7de4d&hm=bdf623e50c1d445db445a9c4878e060d1bf3fb18d38e66b5c3834aa80dfdac8c&')
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title='English speakers',
            description=f'- It will translate English to English for example, so be sure to turn it off if you don\'t speak another language.\n'
                      f'- To turn it off, Type `/auto_translate`  and select "Clear Auto-Translations".',
            color=0x0099ff
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1214621093311025223/1214772011788664895/image.png?ex=65fa5398&is=65e7de98&hm=1e717865aff99856aa4b7f4b4681f1ee8f7283b7d9e8f9ebebbb46072c4c3ca1&')
        await ctx.send(embed=embed)
        
    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def friend_time(self, ctx):
        """
        Explains how to use Friend Time Bot (timezone)
        """
        await ctx.send("# How to use Friend Time Bot (timezone)\n## Try using it in <#1214775106019000380>")
        embed = discord.Embed(
            title='Set your timezone',
            description=f'- Type `/set me` in any channel chat and hit send. The bot will ask where your time zone is.\n'
                      f'- Click the link and select your time zone on the map. Copy the time zone code (e.g. "America/New_York") and paste it in the chat.\n'
                      f'- The bot will show you the current time in your time zone and ask for confirmation. Type "yes" if it\'s correct, or "no" to try again.\n',
            color=0x0099ff
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1214621093311025223/1214793190423531550/image.png?ex=65fa6752&is=65e7f252&hm=689c30774df826596c1946a88a8853c6e58b1245feafc6ad0ce5b0dddbcc787c&')
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title='Check someones timezone',
            description=f'- To check the time of another user, type `/time user` followed by the user\'s name.\n'
                      f'- To turn off notifications when other users view your time, mute the Friend Time bot and the "write-commands" channel in your server.\n',
            color=0x0099ff
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1214621093311025223/1214792810654466088/image.png?ex=65fa66f7&is=65e7f1f7&hm=ba27c23e5bbc72a4367ab0dce632db6697a5ae35ef3720b1696f8366cdc8d659&')
        await ctx.send(embed=embed)
        
    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def guild_rules(self, ctx):
        """
        Displays the Inmortals Guild Rules and Expectations
        """
        embed = discord.Embed(
            title="Inmortals Guild Rules and Expectations",
            description="Welcome to the Inmortals Guild! Inmortals is a guild started by <@698888351763136523>. Here are our rules and expectations for all members of the guild.",
            color=0x0099ff
        )
        embed.add_field(name="Rules", value="1. Be a decent human being in the game. No harassment, excessive shit talking, mistreatment, or hate speeches towards anyone.\n2. Be active in helping out both Inmortals and the server community.\n3. Weekly guild contribution of 4000.\n4. Play daily, like at least once every 8-10 hours for a while and participate in server events.\n5. Check Discord for important information.\n6. Be communicative in game and in Discord.\n7. No inactivity for more than 24-48 hours. If something were to happen in real life, let us know and we can accommodate you accordingly.\n8. If your progress or guild contribution is not aligned with what the guild needs, understand that the guild has helped you more than you have helped the guild. Do not take it personally if you are required to move to a different guild.", inline=False)
        embed.add_field(name="Purpose of Inmortals", value="Our purpose is to provide a strong environment for the strongest players in S40 to grow, and to provide stability and strength to the rest of the server when relied upon. Ultimately, our goal is to dominate with balance in other aspects of real life.", inline=False)
        embed.set_footer(text="Last updated on March 6, 2024")
        await ctx.send(embed=embed)
  
          
    
    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def add_user(self, ctx, rank: str, name: str, guild_name: str, ign: Optional[str] = None, timezone: Optional[str] = None):
        """
        Add a user to the timezones.json file.

        :param ctx: The context of the command.
        :param rank: Rank of the user.
        :param name: Name of the user.
        :param guild_name: Name of the guild.
        :param ign: In-game name of the user.
        :param timezone: Timezone of the user.
        """
        member = ctx.author
        user = {
            str(member.id): {
                'Name': member.name,
                'IGN': ign or None,
                'Timezone': timezone or None,
                'Guild': guild_name,
                'Rank': rank,
            }
        }
        self.timezones.update(user)
        self.save_timezones()

        embed = discord.Embed(title="User Added", description=f"{member.mention} has been added to the database!", color=0x00ff00)
        embed.add_field(name="Rank", value=rank, inline=True)
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="IGN", value=ign or "Not specified", inline=True)
        embed.add_field(name="Guild", value=guild_name, inline=True)
        embed.add_field(name="Timezone", value=timezone or "Not specified", inline=True)
        await ctx.send(embed=embed)

    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def remove_user(self, ctx, member: discord.Member, ign: Optional[str] = None):
        """
        Remove a user from the timezones.json file.

        :param ctx: The context of the command.
        :param member: The member to remove.
        :param ign: In-game name of the user.
        """
        user_id = None
        if ign:
            for user in self.timezones.values():
                if user['IGN'] == ign:
                    user_id = user['ID']
                    break

        if str(member.id) in self.timezones or user_id:
            if user_id:
                del self.timezones[user_id]
            else:
                del self.timezones[str(member.id)]
            self.save_timezones()
            embed = discord.Embed(title="User Removed", description=f"{member.mention if ign else ign} has been removed from the database.", color=0xff0000)
            embed.add_field(name="Name", value=member.name, inline=True)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="User Not Found", description=f"{member.mention if ign else ign} was not found in the database.", color=0xff0000)
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Update the user object in the JSON file if their roles change."""
        guild_role = next((role for role in after.roles if role.name in self.guild_roles), None)
        if not guild_role:
            return

        guild_name = self.guild_roles[guild_role.name]['name']
        rank = next((int(role.name[1]) for role in after.roles if role.name.startswith('r')), None)

        user = {
            str(after.id): {
                'Name': after.name,
                'IGN': None,
                'Timezone': None,
                'Guild': guild_name,
                'Rank': rank,
            }
        }

        self.timezones.update(user)  # Update the user object
        self.save_timezones()

        embed = discord.Embed(title="User updated", description=f"{after.mention} has updated their roles.", color=0xff0000)
        embed.add_field(name="Name", value=after.name, inline=True)
        embed.add_field(name="Guild", value=guild_name, inline=True)
        embed.add_field(name="Rank", value=rank, inline=True)
        channel = self.bot.get_channel(1215443533037707334)
        if channel:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Update the user object in the JSON file if the member joins the guild."""
        if member.guild != self.bot.guild:  # Check if the member is in the right guild
            return

        guild_role = next((role for role in member.roles if role.name in self.guild_roles), None)
        if not guild_role:
            return

        guild_name = self.guild_roles[guild_role.name]['name']
        rank = next((int(role.name[1]) for role in member.roles if role.name.startswith('r')), None)

        user = {
            str(member.id): {
                'Name': member.name,
                'IGN': None,
                'Timezone': None,
                'Guild': guild_name,
                'Rank': rank,
            }
        }

        self.timezones.update(user)  # Update the user object
        self.save_timezones()

        embed = discord.Embed(title="User Join", description=f"{member.mention} has joined the server.", color=0x00ff00)
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="Guild", value=f"{guild_name} ({guild_role.name})", inline=True)
        embed.add_field(name="Rank", value=rank, inline=True)
        channel = self.bot.get_channel(1215443533037707334)
        if channel:
            await channel.send(embed=embed)
        
    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    async def add_guild_role(self, ctx, guild_name: str, tag: str):
        """
        Add a guild role to the JSON file.

        :param ctx: The context of the command.
        :param guild_name: Name of the guild.
        :param tag: Tag of the guild.
        """
        self.guild_roles[guild_name] = {"tag": guild_tag, "name": guild_name}
        self.save_guild_roles()
        await ctx.send(f"Added {guild_name} with tag {tag} to the guild roles")

    @commands.check(is_target_role)
    @bot.slash_command(guild_ids=[1102649117458563243])
    async def remove_guild_role(
        self,
        ctx,
        guild_name_or_tag: Option(
            str,
            "Enter the name or tag of the guild role you want to remove",
            choices=[
                OptionChoice(name=guild_name, value=guild_name)
                for guild_name in self.guild_roles
            ] + [
                OptionChoice(name=f"Tag: {guild_name['tag']}", value=guild_name["tag"])
                for guild_name in self.guild_roles.values()
            ],
        ),
    ):
        """
        Remove a guild role from the JSON file.

        :param ctx: The context of the command.
        :param guild_name_or_tag: Name or tag of the guild.
        """
        if guild_name_or_tag in self.guild_roles:
            del self.guild_roles[guild_name_or_tag]
            self.save_guild_roles()
            await ctx.send(f"Removed {guild_name_or_tag} from the guild roles")
        else:
            for guild_name in self.guild_roles:
                if self.guild_roles[guild_name]["tag"] == guild_name_or_tag:
                    del self.guild_roles[guild_name]
                    self.save_guild_roles()
                    await ctx.send(f"Removed {guild_name} from the guild roles")
                    return
            await ctx.send(f"{guild_name_or_tag} not found in the guild roles")
        
        
        
def setup(bot):
    bot.add_cog(Management(bot))
