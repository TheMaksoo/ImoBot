import discord
import asyncio
from discord.ext import commands
import os

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
async def start(ctx):
    for filename in os.listdir('./cogs'):
        if os.path.isfile(os.path.join('./cogs', filename)) and filename.endswith('.py'):
            cog_name = f'cogs.{filename[:-3]}'
           	if not bot.extensions.get(cog_name, None):
                print(f'Loading cog {filename}')
                try:
                    await bot.load_extension(cog_name)
                except Exception as e:
                    await ctx.send(e)
                else:
                    loaded_cogs.append(cog_name)
    print(f'We have logged in as {bot.user}')
    if loaded_cogs:
        embed = discord.Embed(
            title="Cogs Loaded",
            description="\n".join(loaded_cogs),
            color=0x0099ff,
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("All cogs loaded successfully!")
    
@bot.command()
@commands.check(is_target_user)
async def reload(ctx, cog_name: str):
    """Reloads a cog."""
    try:
        await bot.unload_extension(f'cogs.{cog_name}')
        bot.load_extension(f'cogs.{cog_name}')
        await ctx.send(f'Reloaded cog `{cog_name}` successfully.')
    except Exception as e:
        await ctx.send(f'Error reloading cog `{cog_name}`: {str(e)}')

@bot.command()
@commands.check(is_target_user)
async def dashboard(ctx):
    """Shows the status of all cogs."""
    cogs = bot.extensions
    cog_names = list(cogs.keys())
    cog_status = [bot.get_cog(name).loaded if bot.get_cog(name) else False for name in cog_names]
    cog_strings = [f"{name}: {status}" for name, status in zip(cog_names, cog_status)]
    cog_list = '\n'.join(cog_strings)

    embed = discord.Embed(
        title="Cog Status",
        description=f"Here is the status of all cogs:\n\n{cog_list}",
        color=0x0099ff,
    )
    embed.set_footer(text="IMO bot v4.15")

    await ctx.send(embed=embed)

bot.run('BOT-TOKEN')
