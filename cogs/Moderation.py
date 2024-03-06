import discord
import asyncio
from discord.ext import commands

target_user_id = 387317544228487168

def is_target_user(ctx):
    return ctx.author.id == target_user_id

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_target_user)
    async def purge(ctx, limit: int, message_id: int):
        # Check if the user has the necessary permissions to delete messages
        if not ctx.channel.permissions_for(ctx.author).manage_messages:
            await ctx.send("You don't have the permission to delete messages.")
            return

        # Get the message that triggered the command
        triggered_message = ctx.message

        # Get the messages from the channel
        messages = await ctx.channel.history(limit=limit + 1).flatten()

        # Find the message with the specified ID
        target_message = None
        for message in messages:
            if message.id == message_id:
                target_message = message
                break

        # If the target message is not found, delete the specified number of messages
        if target_message is None:
            await ctx.send("Target message not found.")
        # If the target message is found, delete the messages until the target message
        else:
            to_delete = [message for message in messages if message.id != target_message.id and message.id > triggered_message.id]
            await ctx.channel.delete_messages(to_delete)
async def setup(bot):
    await bot.add_cog(Moderation(bot))
