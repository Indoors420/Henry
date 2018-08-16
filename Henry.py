import discord, random, asyncio, datetime, os, Lists, RecentGen
from discord.ext import commands
bot = commands.Bot(command_prefix="!Henry, ")
@bot.event
async def on_ready():
    seconds = 3601
    while (not bot.is_closed):
        HENRYS_TESTING_SERVER = bot.get_server(os.getenv('HENRYS_TESTING_SERVER'))
        msg = shitpost()
        await bot.send_typing(HENRYS_TESTING_SERVER.get_channel(os.getenv('HENRYS_TESTING_SERVER_GENERAL')))
        await asyncio.sleep(0.8)
        await bot.send_message(HENRYS_TESTING_SERVER.get_channel(os.getenv('HENRYS_TESTING_SERVER_GENERAL')), msg)
        print("Meme Sent")
        print("Waiting "+str(seconds)+" seconds...")
        for _ in range(0,seconds):
            await asyncio.sleep(1)
@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        msg = Lists.commandError[random.randint(0,len(Lists.commandError)-1)]
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        print("ERROR!")
@bot.event
async def on_message(message): #Handles responding to messages
    if ("!Henry, help" in message.content):
        await bot.send_typing(message.channel)
        await asyncio.sleep(0.8)
        msg = Lists.rejected[random.randint(0,len(Lists.rejected)-1)]
        await bot.send_message(message.channel, msg)
        return
    elif (message.content.startswith("!Henry, ") and message.author.id not in Lists.blackList):
        await bot.process_commands(message)
    else:
        lMessage = message.content.lower()
        if (message.author == bot.user):
            return
        elif ("henry" in lMessage or '<@472243513837355009>' in lMessage):
            if (classify(lMessage) == 'question'):
                msg = Lists.answerIntros[random.randint(0,len(Lists.answerIntros)-1)]+nounGen(1)
                await bot.send_typing(message.channel)
                await asyncio.sleep(0.8)
                await bot.send_message(message.channel, msg)
            else:
                msg = phraseGen()
                await bot.send_typing(message.channel)
                await asyncio.sleep(0.8)
                await bot.send_message(message.channel, msg)
@bot.command(pass_context = True)
async def clear(ctx, input):
    if (ctx.message.author.server_permissions.manage_messages == False):
        msg = Lists.noRights[random.randint(0, len(Lists.noRights)-1)]
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
        return
    elif (ctx.message.channel.server.me.server_permissions.manage_messages == False):
        msg = Lists.botOutrank[random.randint(0, len(Lists.botOutrank)-1)]
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        if (not input.isdigit()):
            msg = Lists.badArg[random.randint(0, len(Lists.badArg)-1)]
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)
            return          
        input = int(input)
        if (input < 2):
            msg = Lists.badArg[random.randint(0, len(Lists.badArg)-1)]
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)
            return
        elif (input <= 100): #Command can clear from 2 to 100 messages by default
            amount = input
            mgs = [] #Empty list to put all the messages in the log
            async for i in bot.logs_from(ctx.message.channel, limit = amount):
                mgs.append(i)
            await bot.delete_messages(mgs)
        elif(1000 > input > 100): #All the math below enables the bot to delete sets of 100 messages, + the remainder that isn't divisable by 100
            amount = 100
            loops = str(input / 100)
            #removing decimal points
            loops=int(loops[:loops.index('.')])
            #loops = remaining messages / less than 100
            remainder = input % 100
            for _ in range(0, loops):
                mgs = [] #Empty list to put all the messages in the log
                async for i in bot.logs_from(ctx.message.channel, limit = amount):
                    mgs.append(i)
                if (len(mgs) > 0): #Don't try to delete messages that don't exist
                    await bot.delete_messages(mgs)
                    await asyncio.sleep(0.8)
            remain = [] #Empty list to put all the messages in the log
            async for r in bot.logs_from(ctx.message.channel, limit = remainder):
                remain.append(r)
            await asyncio.sleep(0.8)
            if (len(remain) > 0): #Don't try to delete messages that don't exist
                await bot.delete_messages(remain)
            else:
                return
        elif(input >= 1000):
            msg = Lists.clear1k[random.randint(0, len(Lists.clear1k)-1)]
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(0.8)
            await bot.send_message(ctx.message.channel, msg)
@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    if (ctx.message.author.server_permissions.kick_members == False or user.id == "187656701380526080"):
        msg = Lists.noRights[random.randint(0, len(Lists.noRights)-1)]
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    elif (ctx.message.server.me.top_role <= user.top_role):
        msg = Lists.botOutrank[random.randint(0, len(Lists.botOutrank)-1)]
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    elif (ctx.message.author.top_role <= user.top_role):
        msg = Lists.authorOutrank[random.randint(0, len(Lists.authorOutrank)-1)]
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.8)
        await bot.send_message(ctx.message.channel, msg)
    else:
        await bot.say('Okay {}, time to go.'.format(user.mention))
        await asyncio.sleep(3)
        await bot.kick(user)
def classify(a):
    for word in Lists.questionWords:
        if (word in a):
            type = 'question'
            break
        else:
            type = None
    return(type)
def shitpost(): #Uses returned intros, verbs, and nouns to create a coherent shitpost
    a = random.randint(0,10)
    if (a < 5):
        intro = introGen(1)
        end = "."
    else:
        intro = introGen(2)
        end = "?"
    b = random.randint(0,100)
    if (b < 50):
        verb = verbGen(1)
        noun = nounGen(1)
    elif (68 > b > 50):
        verb = verbGen(2)
        noun = nounGen(2)
    elif (90 > b > 68):
        shit = phraseGen()
        return(shit)       
    else:
        verb = verbGen(3)
        noun = ""
    shit = intro+verb+noun+end
    return(shit)
def introGen(a): #Returns a sentence starter for use in random phrase generation
    if (len(RecentGen.intros1) >= len(Lists.statementIntros) * 0.85):
        del RecentGen.intros1[0]
    elif(len(RecentGen.intros2) >= len(Lists.questionIntros) * 0.85):
        del RecentGen.intros2[0]
    if (a == 1):
        i = random.randint(0, len(Lists.statementIntros)-1)
        while (i in RecentGen.intros1):
            if (i < len(Lists.statementIntros)-1):
                i += 1
            else:
                i = 0
        RecentGen.intros1.append(i)
        intro = Lists.statementIntros[i]
    elif (a == 2):
        i = random.randint(0, len(Lists.questionIntros)-1)
        while (i in RecentGen.intros2):
            if (i < len(Lists.questionIntros)-1):
                i += 1
            else:
                i = 0
        RecentGen.intros2.append(i)
        intro = Lists.questionIntros[i]
    return(intro)
def verbGen(a): #Returns a verb for use in random phrase generation
    if (len(RecentGen.verbs1) >= len(Lists.verbs1) * 0.85):
        del RecentGen.verbs1[0]
    elif (len(RecentGen.verbs2) >= len(Lists.verbs2) * 0.85):
        del RecentGen.verbs2[0]
    elif (len(RecentGen.verbs3) >= len(Lists.verbs3) * 0.85):
        del RecentGen.verbs3[0]
    if (a == 1):
        i = random.randint(0,len(Lists.verbs1)-1)
        while (i in RecentGen.verbs1):
            if (i < len(Lists.verbs1)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs1.append(i)
        verb = Lists.verbs1[i]
    elif (a == 2):
        i = random.randint(0,len(Lists.verbs2)-1)
        while (i in RecentGen.verbs2):
            if (i < len(Lists.verbs2)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs2.append(i)
        verb = Lists.verbs2[i]
    elif (a == 3):
        i = random.randint(0,len(Lists.verbs3)-1)
        while (i in RecentGen.verbs3):
            if (i < len(Lists.verbs3)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs3.append(i)
        verb = Lists.verbs3[i]
    return(verb)
def nounGen(a): #Returns a noun/object for use in random phrase generation
    if (len(RecentGen.nouns1) >= len(Lists.nouns1) * 0.85):
        del RecentGen.nouns1[0]
    elif (len(RecentGen.nouns2) >= len(Lists.nouns2) * 0.85):
        del RecentGen.nouns2[0]
    if (a == 1):
        i = random.randint(0,len(Lists.nouns1)-1)
        while (i in RecentGen.nouns1):
            if (i < len(Lists.nouns1)-1):
                i += 1
            else:
                i = 0
        RecentGen.nouns1.append(i)
        noun = Lists.nouns1[i]
    elif (a == 2):
        i = random.randint(0,len(Lists.nouns2)-1)
        while (i in RecentGen.nouns2):
            if (i < len(Lists.nouns2)-1):
                i += 1
            else:
                i = 0
        RecentGen.nouns2.append(i)
        noun = Lists.nouns2[i]
    return(noun)
def phraseGen(): #Returns a random phrase that Henry's creators made him able to say
    if (len(RecentGen.phrases) >= len(Lists.phrases) * 0.85):
        del RecentGen.phrases[0]
    i = random.randint(0,len(Lists.phrases)-1)
    while (i in RecentGen.phrases):
            if (i < len(Lists.phrases)-1):
                i += 1
            else:
                i = 0
    RecentGen.phrases.append(i)
    phrase = Lists.phrases[i]
    return(phrase)
bot.run(os.getenv('TOKEN'))
