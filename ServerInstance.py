import discord, typing, asyncio
from discord.ext import commands

import Writer, Lists
from ConversationManager import ConversationManager

async def send(bot: commands.Bot, channel: discord.Channel, message: typing.AnyStr, delay=0.8) -> None:
    await bot.send_typing(channel)
    await asyncio.sleep(delay)
    await bot.send_message(channel, message)


class ServerInstance:
    bot: commands.Bot = None
    server = None
    channel = None
    commands = {}
    conversations: ConversationManager = None

    def __init__(self, bot, server_id: str):
        self.bot = bot
        self.server = bot.get_server(server_id)
        self.conversations = ConversationManager()

        self.commands["clear"] = self.command_clear
        self.commands["kick"] = self.command_kick
        
    async def on_message(self, message: discord.Message):
        content = message.content.lower()
        channel = message.channel
        author = message.author
        if author == self.bot.user: return

        if "!Henry, help" in message.content:
            msg = Writer.respond(content, gen_type=2)
            await send(self.bot, channel, msg)
        elif message.content.startswith("!Henry, ") and author.id not in Lists.blackList:
            await self.bot.process_commands(message)            
        else:
            if self.conversations.conversing_with(author):
                self.conversations.update(author)
                if len(ConversationManager.conversations) > 1:
                    msg = Writer.respond(content)+" {}".format(author.mention)
                else:
                    msg = Writer.respond(content)
                    await send(self.bot, channel, msg)

            elif "henry" in content or '<@' + self.bot.user.id + '>' in content:
                self.conversations.add(author)
                if len(ConversationManager.conversations) > 1:
                    msg = Writer.respond(content)+" {}".format(author.mention)
                else:
                    msg = Writer.respond(content)
                await send(self.bot, channel, msg)
                
    async def command_clear(self, ctx, arg: str):
        message = ctx.message
        author = message.author
        channel: discord.Channel = message.channel
        server = channel.server
        
        if not author.server_permissions.manage_messages:
            await send(self.bot, channel, Lists.errorMsgGen(3))
        elif not server.me.server_permissions.manage_messages:
            await send(self.bot, channel, Lists.errorMsgGen(6))
        else:
            if not arg.isdigit():
                await send(self.bot, channel, Lists.errorMsgGen(4))
            arg = int(arg)
            if arg < 2:
                await send(self.bot, channel, Lists.errorMsgGen(4))
            else:

                to_delete = [msg async for msg in self.bot.logs_from(channel, limit=arg)]
                step = 75
                while len(to_delete) >= 100:
                    await self.bot.delete_messages(to_delete[:step])
                    to_delete = to_delete[step:]
                if len(to_delete) == 1:
                    await self.bot.delete_message(to_delete[0])
                else:
                    await self.bot.delete_messages(to_delete)

    async def command_kick(self, ctx, user: discord.Member):
        message = ctx.message
        author = message.author
        channel: discord.Channel = message.channel
        server = channel.server

        if not author.server_permissions.kick_members or user.id == "187656701380526080":
            await send(self.bot, channel, Lists.errorMsgGen(3))
        elif server.me.top_role <= user.top_role:
            await send(self.bot, channel, Lists.errorMsgGen(6))
        elif author.top_role <= user.top_role:
            await send(self.bot, channel, Lists.errorMsgGen(7))
        else:
            await send(self.bot, channel, "Okay {}, time to go.".format(user.mention))
            await asyncio.sleep(3)
            await self.bot.kick(user)
            
    async def command_ban(self, ctx, user: discord.Member):
        message = ctx.message
        author = message.author
        channel: discord.Channel = message.channel
        server = channel.server

        if not author.server_permissions.ban_members or user.id == "187656701380526080":
            await send(self.bot, channel, Lists.errorMsgGen(3))
        elif server.me.top_role <= user.top_role:
            await send(self.bot, channel, Lists.errorMsgGen(6))
        elif author.top_role <= user.top_role:
            await send(self.bot, channel, Lists.errorMsgGen(7))
        else:
            await send(self.bot, channel, "Bye {}, don't come back.".format(user.mention))
            await asyncio.sleep(2.5)
            await self.bot.ban(user)
    
    def __str__(self) -> str:
        return self.server.id
