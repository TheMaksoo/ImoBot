import asyncio
import discord
from discord.ext import commands
import os
import psutil

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
target_user_id = 387317544228487168
def is_target_user(ctx):
    return ctx.author.id == target_user_id


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    
@bot.slash_command(guild_ids=[1102649117458563243])
@commands.check(is_target_user)
async def test(ctx):
    """A test command to send a 'hii' message."""
    await ctx.send("hii")

@bot.slash_command(guild_ids=[1102649117458563243])
@commands.check(is_target_user)
async def start(ctx):
    """Starts the bot and loads all available cogs."""
    await ctx.send("Starting up...")

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f'cogs.{filename[:-3]}'
            if not bot.extensions.get(cog_name, None):
                try:
                    bot.load_extension(cog_name)
                    print(f'Loaded cog {filename}')
                except Exception as e:
                    print(f'Error loading cog {cog_name}: {e}')

    embed = discord.Embed(title="Loaded Cogs", color=discord.Color.green())
    for cog in bot.extensions:
        embed.add_field(name=cog, value="✅", inline=False)
    await ctx.send(embed=embed)

    print(f'Bot started up successfully.')
    synced = await bot.sync_commands()
    
    
    
@bot.slash_command(guild_ids=[1102649117458563243])
@commands.check(is_target_user)
async def reload(ctx, cog_name: str):
    """Reloads a cog."""
    try:
        await bot.unload_extension(f'cogs.{cog_name}')
        bot.load_extension(f'cogs.{cog_name}')
        await ctx.send(f'Reloaded cog `{cog_name}` successfully.')
    except Exception as e:
        await ctx.send(f'Error reloading cog `{cog_name}`: {str(e)}')
        
bot.run('BOT-TOKEN')
