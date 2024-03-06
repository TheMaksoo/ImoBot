import discord
import asyncio
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

target_user_id = 387317544228487168

def is_target_user(ctx):
    return ctx.author.id == target_user_id


@bot.command()
@commands.check(is_target_user)
async def test(ctx):
    await ctx.send("hii")

@bot.command()
@commands.check(is_target_user)
async def copyall(ctx: commands.Context, source_guild_id: int, source_channel_id: int, destination_guild_id: int, destination_channel_id: int):
    try:
        source_guild = bot.get_guild(source_guild_id)
    except AttributeError:
        await ctx.send("Error: Source guild not found.")
        return

    try:
        destination_guild = bot.get_guild(destination_guild_id)
    except AttributeError:
        await ctx.send("Error: Destination guild not found.")
        return

    source_channel = discord.utils.get(source_guild.channels, id=source_channel_id, type=discord.ChannelType.text)
    destination_channel = discord.utils.get(destination_guild.channels, id=destination_channel_id, type=discord.ChannelType.text)

    if not source_channel or not destination_channel:
        await ctx.send("Error: Source or destination channel not found.")
        return

    async for message in source_channel.history(limit=None, oldest_first=True):
        if message.attachments:
            for attachment in message.attachments:
                await attachment.save(attachment.filename)
                await destination_channel.send(file=discord.File(attachment.filename))
                await asyncio.sleep(0.5)
        await destination_channel.send(message.content)
        await asyncio.sleep(0.5)
    await ctx.send('Messages and images copied successfully!')

@bot.command()
@commands.check(is_target_user)
@commands.check(lambda ctx: ctx.channel.permissions_for(ctx.me).manage_messages)
async def purge(ctx: commands.Context, amount: int):
    if amount > 100:
        await ctx.send("I can't delete more than 100 messages at a time.")
        return
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{len(deleted) - 1} messages deleted.")

@bot.command()
@commands.check(is_target_user)
async def auto_translate(ctx):
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

@bot.command()
@commands.check(is_target_user)
async def friend_time(ctx):
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

@bot.command()
@commands.check(is_target_user)
async def guild_rules(ctx):
    embed = discord.Embed(
        title="Inmortals Guild Rules and Expectations",
        description="Welcome to the Inmortals Guild! Inmortals is a guild started by <@698888351763136523>.Here are our rules and expectations for all members of the guild.",
        color=0x0099ff
    )
    embed.add_field(name="Rules", value="1. Be a decent human being in the game. No harassment, excessive shit talking, mistreatment, or hate speeches towards anyone.\n2. Be active in helping out both Inmortals and the server community.\n3. Weekly guild contribution of 4000.\n4. Play daily, like at least once every 8-10 hours for a while and participate in server events.\n5. Check Discord for important information.\n6. Be communicative in game and in Discord.\n7. No inactivity for more than 24-48 hours. If something were to happen in real life, let us know and we can accommodate you accordingly.\n8. If your progress or guild contribution is not aligned with what the guild needs, understand that the guild has helped you more than you have helped the guild. Do not take it personally if you are required to move to a different guild.", inline=False)
    embed.add_field(name="Purpose of Inmortals", value="Our purpose is to provide a strong environment for the strongest players in S40 to grow, and to provide stability and strength to the rest of the server when relied upon. Ultimately, our goal is to dominate with balance in other aspects of real life.", inline=False)
    embed.set_footer(text="Last updated on March 6, 2024")
    await ctx.send(embed=embed)

last_said_time = {}

@bot.event
async def on_message(message):
    if message.mentions:
        for mentioned_user in message.mentions:
            if mentioned_user.id == 161821149485858816:
                await message.add_reaction('\U0001F451') # crown emoji
                print("Hail king leon")
            if mentioned_user.id == 553367214217232394:
                await message.add_reaction('\U0001F496') # heart emoji
                print("Morgg indeed pretty")
            if mentioned_user.id == 313449244885516288:
                await message.add_reaction('\U0001F3A9') # wizard emoji 
                print("Hocus pocus")
            if mentioned_user.id == 387317544228487168:
                await message.add_reaction('\U0001F468\u200D\U0001F4BB') # computer emoji
                print("BEEPBOOP")
                
    if 'leon' in message.content.lower() and message.author.bot is False:
        print("Hail king leon")
        if 'king leon' in message.content.lower():
            await message.add_reaction('\U0001F451') # crown emoji
        else:
            italic_message = f'*did you mean King Leon?*'
            await message.channel.send(italic_message)

    if 'morgg' in message.content.lower() and message.author.bot is False:
        print("Morgg indeed pretty")
        if 'not pretty' in message.content.lower():
            mad_reaction = '\U0001F621' # angry face emoji
            await message.add_reaction(mad_reaction)
        elif 'pretty' in message.content.lower():
            await message.add_reaction('\U0001F496') # heart emoji
        else:
            italic_message = f'*did you mean Pretty Morgg?*'
            await message.channel.send(italic_message)

    if 'haku' in message.content.lower() and message.author.bot is False:
        print("Hocus pocus")
        await message.add_reaction('\U0001F3A9') # wizard emoji 
        
    if 'maksoo' in message.content.lower() and message.author.bot is False:
        print("BEEPBOOP")
        await message.add_reaction('\U0001F468\u200D\U0001F4BB') # computer emoji
    if 'maks' in message.content.lower() and message.author.bot is False:
        print("BEEPBOOP")
        await message.add_reaction('\U0001F468\u200D\U0001F4BB') # computer emoji 
        
bot.run('MTIxNDQxODUwNjE4NDEzODgxNA.G8nuNm.DXAcSAMQAhusBr1z7JNepoas6KNThghk9FCIrU')
