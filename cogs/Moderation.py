import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
def is_target_role(ctx):
    return any(role.name == "Manager" for role in ctx.author.roles)

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(guild_ids=[1102649117458563243])
    @commands.check(is_target_role)
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def purge(self, ctx, limit: int):
        """
        Purge a specified number of messages from a channel.
        """
        # Check if the user has the necessary permissions to delete messages
        if not ctx.channel.permissions_for(ctx.author).manage_messages:
            await ctx.send("You don't have the permission to delete messages.")
            return

        # Get the messages from the channel
        messages = await ctx.channel.history(limit=limit + 1).flatten()

        # Delete the specified number of messages
        to_delete = [message for message in messages if message.id > ctx.message.id]
        await ctx.channel.delete_messages(to_delete)
        
def setup(bot):
   	bot.add_cog(Moderation(bot))
