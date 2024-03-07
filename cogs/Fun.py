import asyncio
import discord
import json
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def is_target_role(ctx):
    return any(role.name == "Manager" for role in ctx.author.roles)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklisted_channels = []
        self.file_path = os.path.join('/home/container/storage', 'blacklisted_channels.json')
        try:
            with open(self.file_path, 'r') as f:
                self.blacklisted_channels = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_blacklist(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.blacklisted_channels, f)

    @bot.slash_command(guild_ids=[1102649117458563243], description="Add a channel to the blacklist")
    @commands.check(is_target_role)
    async def add_blacklist(self, ctx, channel: discord.TextChannel):
        self.blacklisted_channels.append(channel.id)
        self.save_blacklist()
        embed = discord.Embed(title="Channel added to blacklist", description=f"{channel.name} has been added to the blacklist.", color=0xFF0000)
        await ctx.send(embed=embed)

    @bot.slash_command(guild_ids=[1102649117458563243], description="Remove a channel from the blacklist")
    @commands.check(is_target_role)
    async def remove_blacklist(self, ctx, channel: discord.TextChannel):
        if channel.id in self.blacklisted_channels:
            self.blacklisted_channels.remove(channel.id)
            self.save_blacklist()
            embed = discord.Embed(title="Channel removed from blacklist", description=f"{channel.name} has been removed from the blacklist.", color=0xFF0000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Channel not in blacklist", description=f"{channel.name} is not in the blacklist.", color=0xFF0000)
            await ctx.send(embed=embed)
            
           
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in self.blacklisted_channels:
            return

        if message.mentions:
            for mentioned_user in message.mentions:
                if mentioned_user.id == 161821149485858816:
                    await message.add_reaction('\U0001F451')  # crown emoji
                    print(f"{message.created_at} - Hail king leon in {message.channel}")
                if mentioned_user.id == 553367214217232394:
                    await message.add_reaction('\U0001F496')  # heart emoji
                    print(f"{message.created_at} - Morgg indeed pretty in {message.channel}")
                if mentioned_user.id == 313449244885516288:
                    await message.add_reaction('\U0001F3A9')  # wizard emoji
                    print(f"{message.created_at} - Hocus pocus in {message.channel}")
                if mentioned_user.id == 387317544228487168:
                    await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji
                    print(f"{message.created_at} - BEEPBOOP in {message.channel}")

        if 'leon' in message.content.lower() and message.author.bot is False:
            print(f"{message.created_at} - Hail king leon in {message.channel}")
            if 'king leon' in message.content.lower():
                await message.add_reaction('\U0001F451')  # crown emoji
            else:
                italic_message = f'*did you mean King Leon?*'
                await message.channel.send(italic_message)

        if 'morgg' in message.content.lower() and message.author.bot is False:
            print(f"{message.created_at} - Morgg indeed pretty in {message.channel}")
            if 'not pretty' in message.content.lower():
                mad_reaction = '\U0001F621'  # angry face emoji
                await message.add_reaction(mad_reaction)
            elif 'pretty' in message.content.lower():
                await message.add_reaction('\U0001F496')  # heart emoji
            else:
                italic_message = f'*did you mean Pretty Morgg?*'
                await message.channel.send(italic_message)

        if 'haku' in message.content.lower() and message.author.bot is False:
            print(f"{message.created_at} - Hocus pocus in {message.channel}")
            await message.add_reaction('\U0001F3A9')  # wizard emoji

        if 'maksoo' in message.content.lower() and message.author.bot is False:
            print(f"{message.created_at} - BEEPBOOP in {message.channel}")
            await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji  

def setup(bot):
    bot.add_cog(Fun(bot))
