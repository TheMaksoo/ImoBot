import discord
import psutil
import os
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
target_user_id = 387317544228487168
def is_target_user(ctx):
    return ctx.author.id == target_user_id

class Dashboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_user)
    async def stats(self, ctx):
        """Display server stats and cog status."""
        guild = ctx.guild
        member_count = guild.member_count
        bot_member = guild.members[0] if guild.members else None
        cogs = self.bot.extensions
        online_cogs = sum(1 for cog in cogs.values())

        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        network_io_counters = psutil.net_io_counters()
        network_bytes_sent = network_io_counters.bytes_sent
        network_bytes_recv = network_io_counters.bytes_recv

        embed = discord.Embed(title="Server Stats", color=0x00ff00)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Member Count", value=member_count, inline=False)
        embed.add_field(name="Bot Status", value=f"Online on {len(self.bot.guilds)} servers.", inline=False)
        embed.add_field(name="Cogs Loaded", value=online_cogs, inline=False)
        embed.add_field(name="CPU Load", value=f"{cpu_percent}%", inline=False)
        embed.add_field(name="Memory Usage", value=f"{memory_percent}%", inline=False)
        embed.add_field(name="Network Bytes Sent", value=f"{network_bytes_sent}", inline=False)
        embed.add_field(name="Network Bytes Received", value=f"{network_bytes_recv}", inline=False)

        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Dashboard(bot))
