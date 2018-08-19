import discord, typing, asyncio
from discord.ext import commands

import Writer, Lists
from ConversationManager import ConversationManager

async def send(bot: commands.Bot, channel: discord.Channel, message: typing.AnyStr, delay=0.8) -> None:
    await bot.send_typing(channel)
    await asyncio.sleep(delay)
    await bot.send_message(channel, message)


class Henry:
    bot: commands.Bot = None
    server = None
    channel = None
    commands = {}
    conversations: ConversationManager = None

    def __init__(self, bot, server_id: str, channel_id: str):
        self.bot = bot
        self.server = bot.get_server(server_id)
        self.channel = bot.get_channel(channel_id)
        self.conversations = ConversationManager()

    async def on_message(self, message: discord.Message):
        content = message.content.lower()
        channel = message.channel
        author = message.author
        if author == self.bot.user: return

        if "!Henry, help" in message.content:
            msg = Writer.respond(content, gen_type=2)
            await send(self.bot, channel, msg)
        elif message.content.startswith("!Henry, ") and author.id not in Lists.blackList:
            await self.bot.process_command(message)
        else:
            if self.conversations.conversing_with(author):
                self.conversations.update(author)
                msg = Writer.respond(content)
                await send(self.bot, channel, msg)

            elif "henry" in content or '<@' + self.bot.user.id + '>' in content:
                self.conversations.add(author)
                msg = Writer.respond(content)
                await send(self.bot, channel, msg)
        

    async def command_clear(self, ctx, input: str):
        print("clear command")

    async def command_kick(self, ctx, user: discord.Member):
        print("kick command")
    
    def __str__(self) -> str:
        return self.server.id
