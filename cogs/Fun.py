import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
target_user_id = 387317544228487168
def is_target_user(ctx):
    return ctx.author.id == target_user_id

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            for mentioned_user in message.mentions:
                if mentioned_user.id == 161821149485858816:
                    await message.add_reaction('\U0001F451')  # crown emoji
                    print("Hail king leon")
                if mentioned_user.id == 553367214217232394:
                    await message.add_reaction('\U0001F496')  # heart emoji
                    print("Morgg indeed pretty")
                if mentioned_user.id == 313449244885516288:
                    await message.add_reaction('\U0001F3A9')  # wizard emoji 
                    print("Hocus pocus")
                if mentioned_user.id == 387317544228487168:
                    await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji
                    print("BEEPBOOP")

        if 'leon' in message.content.lower() and message.author.bot is False:
            print("Hail king leon")
            if 'king leon' in message.content.lower():
                await message.add_reaction('\U0001F451')  # crown emoji
            else:
                if message.channel.id == 1205294988045455411:
                    # If the message was sent in the channel, return immediately (imo-core)
                    return
                italic_message = f'*did you mean King Leon?*'
                await message.channel.send(italic_message)

        if 'morgg' in message.content.lower() and message.author.bot is False:
            print("Morgg indeed pretty")
            if 'not pretty' in message.content.lower():
                mad_reaction = '\U0001F621'  # angry face emoji
                await message.add_reaction(mad_reaction)
            elif 'pretty' in message.content.lower():
                await message.add_reaction('\U0001F496')  # heart emoji
            else:
                if message.channel.id == 1205294988045455411:
                    # If the message was sent in the channel, return immediately (imo-core)
                    return
                italic_message = f'*did you mean Pretty Morgg?*'
                await message.channel.send(italic_message)

        if 'haku' in message.content.lower() and message.author.bot is False:
            print("Hocus pocus")
            await message.add_reaction('\U0001F3A9')  # wizard emoji 

        if 'maksoo' in message.content.lower() and message.author.bot is False:
            print("BEEPBOOP")
            await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji 
        if 'maks' in message.content.lower() and message.author.bot is False:
            print("BEEPBOOP")
            await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji  

def setup(bot):
    bot.add_cog(Fun(bot))
