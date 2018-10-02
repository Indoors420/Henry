import discord, asyncio, typing, os, json, logging
from discord.ext import commands

from ServerInstance import ServerInstance

bot: commands.Bot = commands.Bot(command_prefix="!Henry, ")

instances = {}


def is_henry_server(server: discord.Server) -> bool:
    return server.id in instances


def get_henry(server: discord.Server) -> ServerInstance:
    if not is_henry_server(server):
        add_server(server.id)
    return instances[server.id]


def add_server(server_id):
    new_henry = ServerInstance(bot, server_id)
    instances[server_id] = new_henry


@bot.event
async def on_ready():
    print("Henry is ready")


@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    print("Hey chief, something went wrong")
    print(error)


@bot.event
async def on_message(message: discord.Message):
    await get_henry(message.server).on_message(message)



@bot.command(pass_context=True)
async def clear(ctx: commands.Context, argument):
    await get_henry(ctx.message.server).command_clear(ctx, argument)


@bot.command(pass_context=True)
async def kick(ctx: commands.Context, user: discord.Member):
    await get_henry(ctx.message.server).command_kick(ctx, user)


@bot.command(pass_context=True)
async def ban(ctx: commands.Context, user: discord.Member):
    await get_henry(ctx.message.server).command_ban(ctx, user)


def start(token):
    bot.run(token)


# If this is the main file,
# start using environment token
if __name__ == "__main__":
    start(os.getenv("TOKEN"))
