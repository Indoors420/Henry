import discord, asyncio, typing, os, json
from discord.ext import commands

from Henry import Henry

bot: commands.Bot = commands.Bot(command_prefix="!Henry, ")

henrys = {}


def is_henry_server(server: discord.Server) -> bool:
    return server.id in henrys


def get_henry(server: discord.Server) -> Henry:
    return henrys[server.id]


def add_server(server_id, server_general_channel):
    new_henry = Henry(bot, server_id, server_general_channel)
    henrys[server_id] = new_henry


@bot.event
async def on_ready():
    print("Henry is ready")


@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    print("Henry command error")


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

# If this is the main file,
# load servers and token from env variables
# SERVERS env should be a 2d json array
# [[server_id, channel_id], [server_id, channel_id], etc]
if __name__ == "__main__":
    servers = json.loads(os.getenv("SERVERS"))

    for server in servers:
        add_server(server[0], server[1])

    bot.run(os.getenv("TOKEN"))