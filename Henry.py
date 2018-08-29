import discord, asyncio, typing, os, json, logging
from discord.ext import commands

from ServerInstance import ServerInstance

bot: commands.Bot = commands.Bot(command_prefix="!Henry, ")

instances = {}


def is_henry_server(server: discord.Server) -> bool:
    return server.id in instances


def get_henry(server: discord.Server) -> ServerInstance:
    return instances[server.id]


def add_server(server_id):
    new_henry = ServerInstance(bot, server_id)
    instances[server_id] = new_henry


@bot.event
async def on_ready():
    init_all_servers()
    print("Henry is ready")


@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    print("Hey chief, something went wrong")
    print(error)


@bot.event
async def on_message(message: discord.Message):
    if is_henry_server(message.server):
        await get_henry(message.server).on_message(message)
    


@bot.command(pass_context=True)
async def clear(ctx: commands.Context, argument):
    if is_henry_server(ctx.message.server):
        await get_henry(ctx.message.server).command_clear(ctx, argument)


@bot.command(pass_context=True)
async def kick(ctx: commands.Context, user: discord.Member):
    if is_henry_server(ctx.message.server):
        await get_henry(ctx.message.server).command_kick(ctx, user)


@bot.command(pass_context=True)
async def ban(ctx: commands.Context, user: discord.Member):
    if is_henry_server(ctx.message.server):
        await get_henry(ctx.message.server).command_ban(ctx, user)


def init_all_servers():
    for server in bot.servers:
        add_server(server.id)


def start(token):
    bot.run(token)


# If this is the main file,
# start using environment token
if __name__ == "__main__":
    start(os.getenv("TOKEN"))
