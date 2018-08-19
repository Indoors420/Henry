import discord, random, asyncio, datetime, os, Lists, RecentGen, HenryNet.Generate
from discord.ext import commands

bot = commands.Bot(command_prefix="!Henry, ")


@bot.event
async def on_ready():
    print("Henry is here to "+Lists.verbGen(1)+" "+Lists.nounGen(1))
    await send()


@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        msg = Lists.errorMsgGen(2)
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        print("ERROR!")


conversing = False


@bot.event
async def on_message(message):  # Handles responding to messages
    if message.author == bot.user:
        return
    global conversing
    if "!Henry, help" in message.content:
        msg = msgGen(message.content, 2)
        await bot.send_typing(message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(message.channel, msg)
    elif message.content.startswith("!Henry, ") and message.author.id not in Lists.blackList:
        await bot.process_commands(message)
    else:
        response = None
        content = message.content.lower()
        if not conversing:
            if "henry" in content or '<@476854637371195433>' in content:
                msg = msgGen(content, 1)
                await bot.send_typing(message.channel)
                await asyncio.sleep(0.8)
                await bot.send_message(message.channel, msg)
                response = await bot.wait_for_message(author=message.author, timeout=8.0)
            while response is not None:  # Currently brakes when user says henry as first response in convo
                content = response.content.lower()
                msg = msgGen(content, 1)
                await bot.send_typing(message.channel)
                await asyncio.sleep(0.8)
                await bot.send_message(message.channel, msg)
                response = await bot.wait_for_message(author=message.author, timeout=8.0)
                conversing = False


@bot.command(pass_context=True)
async def clear(ctx, argument):
    if not ctx.message.author.server_permissions.manage_messages:
        msg = Lists.errorMsgGen(3)
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
        return
    elif not ctx.message.channel.server.me.server_permissions.manage_messages:
        msg = Lists.errorMsgGen(6)
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        if not argument.isdigit():
            msg = Lists.errorMsgGen(4)
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)
            return          
        argument = int(argument)
        if argument < 2:
            msg = Lists.errorMsgGen(4)
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)
            return
        elif argument <= 100:  # Command can clear from 2 to 100 messages by default
            amount = argument
            mgs = []  # Empty list to put all the messages in the log
            async for i in bot.logs_from(ctx.message.channel, limit=amount):
                mgs.append(i)
            await bot.delete_messages(mgs)
        elif 1000 > argument > 100:  # All the math below enables the bot to delete sets of 100 messages, + the remainder that isn't divisable by 100
            amount = 100
            loops = str(argument / 100)
            # removing decimal points
            loops = int(loops[:loops.index('.')])
            # loops = remaining messages / less than 100
            remainder = argument % 100
            for _ in range(0, loops):
                mgs = []  # Empty list to put all the messages in the log
                async for i in bot.logs_from(ctx.message.channel, limit=amount):
                    mgs.append(i)
                if len(mgs) > 0:  # Don't try to delete messages that don't exist
                    await bot.delete_messages(mgs)
                    await asyncio.sleep(0.8)
            remain = []  # Empty list to put all the messages in the log
            async for r in bot.logs_from(ctx.message.channel, limit=remainder):
                remain.append(r)
            await asyncio.sleep(0.8)
            if len(remain) > 0:  # Don't try to delete messages that don't exist
                await bot.delete_messages(remain)
            else:
                return
        elif argument >= 1000:
            msg = Lists.errorMsgGen(5)
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if not ctx.message.author.server_permissions.kick_members or user.id == "187656701380526080":
        msg = Lists.errorMsgGen(3)
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    elif ctx.message.server.me.top_role <= user.top_role:
        msg = Lists.errorMsgGen(6)
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    elif ctx.message.author.top_role <= user.top_role:
        msg = Lists.errorMsgGen(7)
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    else:
        await bot.say('Okay {}, time to go.'.format(user.mention))
        await asyncio.sleep(3)
        await bot.kick(user)


async def send():
    henrys_testing_server = bot.get_server(os.getenv('HENRYS_TESTING_SERVER'))
    msg = shitpost()
    await bot.send_typing(henrys_testing_server.get_channel(os.getenv('HENRYS_TESTING_SERVER_GENERAL')))
    await asyncio.sleep(0.8)
    await bot.send_message(henrys_testing_server.get_channel(os.getenv('HENRYS_TESTING_SERVER_GENERAL')), msg)
    print('''Henry says: "'''+msg+'''"''')


def msgGen(a, b):
    msg = ""
    if b == 1:
        if classify(a) == 'why':
            msg = Lists.introGen(3, 1)+Lists.nounGen(1)+" "+Lists.verbGen(1)+" "+Lists.nounGen(1)
        elif classify(a) == 'how':
            msg = Lists.introGen(3, 2)+Lists.nounGen(1)+" "+Lists.verbGen(1)+"s "+Lists.nounGen(1)
        elif classify(a) == 'who' or classify(a) == 'what':
            msg = Lists.nounGen(1)
        elif classify(a) == 'when':
            msg = Lists.timeGen()
        else:
            chance = random.randint(0, 100)
            if chance < 75:
                msg = Lists.phraseGen()
            else:
                msg = retaliate(a, rand=True)
    elif b == 2:
        msg = Lists.errorMsgGen(1)
    return msg


def classify(a):
    if "why" in a:
        classification = 'why'
    elif "how" in a:
        classification = 'how'
    elif "who" in a:
        classification = 'who'
    elif "what" in a or "which" in a:
        classification = 'what'
    elif "when" in a:
        classification = 'when'
    else:
        classification = None
    return classification


def shitpost():  # Uses returned intros, verbs, and nouns to create a coherent shitpost
    a = random.randint(0, 10)
    if a < 5:
        intro = Lists.introGen(1, None)
        end = "."
    else:
        intro = Lists.introGen(2, None)
        end = "?"
    b = random.randint(0, 100)
    if b < 50:
        verb = Lists.verbGen(1)+" "
        noun = Lists.nounGen(1)
    elif 68 > b > 50:
        verb = Lists.verbGen(2)+" "
        noun = Lists.nounGen(2)
    elif 90 > b > 68:
        shit = Lists.phraseGen()
        return shit
    else:
        verb = Lists.verbGen(3)  # ends without noun
        noun = ""
    shit = intro+verb+noun+end
    return shit


def retaliate(msg="", rand=False):  # generates a random retaliation using AI
    if rand:
        import string
        msg += ''.join([random.choice(string.ascii_letters) for _ in range(20)])
    return "I" + HenryNet.Generate.retaliate(msg, 0.8)


bot.run(os.getenv('TOKEN'))
