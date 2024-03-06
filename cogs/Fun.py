
Bot-Hosting.net

Console
Files
Databases
Schedules
Users
Backups
Network
Startup
Settings
Activity
/
home
/
container
/
cogs
/
fun.py
1
import discord
2
import asyncio
3
from discord.ext import commands
4
​
5
​
6
class Fun(commands.Cog):
7
    def __init__(self, bot):
8
        self.bot = bot
9
​
10
    @commands.Cog.listener()
11
    async def on_message(self, message):
12
        if message.mentions:
13
            for mentioned_user in message.mentions:
14
                if mentioned_user.id == 161821149485858816:
15
                    await message.add_reaction('\U0001F451')  # crown emoji
16
                    print("Hail king leon")
17
                if mentioned_user.id == 553367214217232394:
18
                    await message.add_reaction('\U0001F496')  # heart emoji
19
                    print("Morgg indeed pretty")
20
                if mentioned_user.id == 313449244885516288:
21
                    await message.add_reaction('\U0001F3A9')  # wizard emoji 
22
                    print("Hocus pocus")
23
                if mentioned_user.id == 387317544228487168:
24
                    await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji
25
                    print("BEEPBOOP")
26
​
27
        if 'leon' in message.content.lower() and message.author.bot is False:
28
            print("Hail king leon")
29
            if 'king leon' in message.content.lower():
30
                await message.add_reaction('\U0001F451')  # crown emoji
31
            else:
32
                if message.channel.id == 1205294988045455411:
33
                    # If the message was sent in the channel, return immediately (imo-core)
34
                    return  
35
                italic_message = f'*did you mean King Leon?*'
36
                await message.channel.send(italic_message)
37
​
38
        if 'morgg' in message.content.lower() and message.author.bot is False:
39
            print("Morgg indeed pretty")
40
            if 'not pretty' in message.content.lower():
41
                mad_reaction = '\U0001F621'  # angry face emoji
42
                await message.add_reaction(mad_reaction)
43
            elif 'pretty' in message.content.lower():
44
                await message.add_reaction('\U0001F496')  # heart emoji
45
            else:
46
                if message.channel.id == 1205294988045455411:
47
                    # If the message was sent in the channel, return immediately (imo-core)
48
                    return  
49
                italic_message = f'*did you mean Pretty Morgg?*'
50
                await message.channel.send(italic_message)
51
​
52
        if 'haku' in message.content.lower() and message.author.bot is False:
53
            print("Hocus pocus")
54
            await message.add_reaction('\U0001F3A9')  # wizard emoji 
55
​
56
        if 'maksoo' in message.content.lower() and message.author.bot is False:
57
            print("BEEPBOOP")
58
            await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji 
59
        if 'maks' in message.content.lower() and message.author.bot is False:
60
            print("BEEPBOOP")
61
            await message.add_reaction('\U0001F468\u200D\U0001F4BB')  # computer emoji  
62
​
63
async def setup(bot):

Python
SAVE CONTENT
Pterodactyl® © 2015 - 2024
