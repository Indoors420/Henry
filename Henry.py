import discord, random, asyncio, datetime, os, Lists
from discord.ext import commands
bot = commands.Bot(command_prefix="Henry, ")
@bot.event
async def on_ready():
    seconds = 3601
    while (not bot.is_closed):
        msg = shitpost()
        HENRYSSERVER = bot.get_server(os.getenv('HENRYS_TESTING_SERVER'))
        await bot.send_message(HENRYSSERVER.get_channel(os.getenv('HENRYS_TESTING_SERVER_GENERAL')), msg)
        print("Meme Sent")
        print("Waiting "+str(seconds)+" seconds...")
        for _ in range(0,seconds):
            await asyncio.sleep(1)
@bot.event
async def on_command_error(error: Exception, ctx: commands.Context):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        await asyncio.sleep(0.7)
        msg = Lists.commandError[random.randint(0,len(Lists.commandError)-1)]
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        print("ERROR!")
counter = 0
#"Recent" lists are used to store generated words/phrases and then to regenerate new gens so as not to be repetitive
Nrecent1 = []
Nrecent2 = []
Nrecent3 = []
Vrecent1 = []
Vrecent2 = []
Vrecent3 = []
Irecent1 = []
Irecent2 = []
Irecent3 = []
Precent = []
@bot.event
async def on_message(message): #Handles responding to messages
    global counter
    if ("Henry, help" in message.content):
        await asyncio.sleep(0.7)
        msg = Lists.rejected[random.randint(0,len(Lists.rejected)-1)]
        await bot.send_message(message.channel, msg)
        return
    if (message.content.startswith("Henry, ") and message.author.id not in Lists.blackList):
        await bot.process_commands(message)
    else:
        chance = random.randint(0,100)
        if (message.author == bot.user):
            return
        elif(message.author.bot == True and chance > 85):
            if (counter < 3): #Don't want bots to keep responding to eachother, 3 times is good
                if (chance < 75):
                    msg = retaliate(1) +" {0.author.mention}".format(message)
                else:
                    msg = retaliate(2).format(message)
                await asyncio.sleep(2) #wait 2 seconds before responding to a bot to prevent rapid fire responses between bots
                await bot.send_message(message.channel, msg)   
            else:
                await asyncio.sleep(30) #Wait 30 seconds and then reset counter, bot can respond to bots again
                counter = 0
        elif (chance > 98 or "henry" in message.content or "HENRY" in message.content or "Henry" in message.content or '<@472243513837355009>' in message.content):
            if (chance < 60):
                msg = retaliate(1) +" {0.author.mention}".format(message)
            else:
                msg = retaliate(2).format(message)
            await asyncio.sleep(0.7)
            await bot.send_message(message.channel, msg)   
@bot.command(pass_context = True)
async def clear(ctx, input):
    if (ctx.message.author.server_permissions.manage_messages == False):
        msg = Lists.noRights[random.randint(0, len(Lists.noRights)-1)]
        await asyncio.sleep(0.7)
        await bot.send_message(ctx.message.channel, msg)
        return
    elif (ctx.message.channel.server.me.server_permissions.manage_messages == False):
        msg = Lists.botOutrank[random.randint(0, len(Lists.botOutrank)-1)]
        await asyncio.sleep(0.7)
        await bot.send_message(ctx.message.channel, msg)
        return
    else:
        if (not input.isdigit()):
            msg = Lists.badArg[random.randint(0, len(Lists.badArg)-1)]
            await asyncio.sleep(0.7)
            await bot.send_message(ctx.message.channel, msg)
            return          
        input = int(input)
        if (input < 2):
            msg = Lists.badArg[random.randint(0, len(Lists.badArg)-1)]
            await asyncio.sleep(0.7)
            await bot.send_message(ctx.message.channel, msg)
            return
        elif (input <= 100): #Command can clear from 2 to 100 messages by default
            amount = input
            mgs = [] #Empty list to put all the messages in the log
            async for x in bot.logs_from(ctx.message.channel, limit = amount):
                mgs.append(x)
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
                async for x in bot.logs_from(ctx.message.channel, limit = amount):
                    mgs.append(x)
                if (len(mgs) > 0): #Don't try to delete messages that don't exist
                    await bot.delete_messages(mgs)
                    await asyncio.sleep(1)
            remain = [] #Empty list to put all the messages in the log
            async for r in bot.logs_from(ctx.message.channel, limit = remainder):
                remain.append(r)
            await asyncio.sleep(1)
            if (len(remain) > 0): #Don't try to delete messages that don't exist
                await bot.delete_messages(remain)
            else:
                return
        elif(input >= 1000):
            msg = Lists.clear1k[random.randint(0, len(Lists.clear1k)-1)]
            await bot.send_message(ctx.message.channel, msg)
@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    if (ctx.message.author.server_permissions.kick_members == False or user.id == "187656701380526080"):
        msg = Lists.noRights[random.randint(0, len(Lists.noRights)-1)]
        await asyncio.sleep(0.7)
        await bot.send_message(ctx.message.channel, msg)
    elif(ctx.message.server.me.top_role <= user.top_role):
        msg = Lists.botOutrank[random.randint(0, len(Lists.botOutrank)-1)]
        await asyncio.sleep(0.7)
        await bot.send_message(ctx.message.channel, msg)
    elif(ctx.message.author.top_role <= user.top_role):
        msg = Lists.authorOutrank[random.randint(0, len(Lists.authorOutrank)-1)]
        await asyncio.sleep(0.7)
        await bot.send_message(ctx.message.channel, msg)
    else:
        await bot.say('Okay {}, time to go.'.format(user.mention))
        await asyncio.sleep(3)
        await bot.kick(user)
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
    if (len(Irecent1) >= len(Lists.statementIntros)*0.9):
        del Irecent1[0]
    elif (len(Irecent2) >= len(Lists.questionIntros)*0.9):
        del Irecent2[0]
    elif (len(Irecent3) >= len(Lists.retaliationIntros)*0.9):
        del Irecent3[0]
    if (a == 1):
        i = random.randint(0, len(Lists.statementIntros)-1)
        while (i in Irecent1):
            i = random.randint(0, len(Lists.statementIntros)-1)
        intro = Lists.statementIntros[i]
        Irecent1.append(i)
    elif (a == 2):
        i = random.randint(0, len(Lists.questionIntros)-1)
        while (i in Irecent2):
            i = random.randint(0, len(Lists.questionIntros)-1)
        intro = Lists.questionIntros[i]
        Irecent2.append(i)
    elif (a == 3):
        i = random.randint(0, len(Lists.retaliationIntros)-1)
        while (i in Irecent3):
            i = random.randint(0, len(Lists.retaliationIntros)-1)
        intro = Lists.retaliationIntros[i]
        Irecent3.append(i)
    return(intro)
def verbGen(a): #Returns a verb for use in random phrase generation
    if (len(Vrecent1) >= len(Lists.verbs1)*0.9):
        del Vrecent1[0]
    elif (len(Vrecent2) >= len(Lists.verbs2)*0.9):
        del Vrecent2[0]
    elif (len(Vrecent3) >= len(Lists.verbs3)*0.9):
        del Vrecent3[0]
    if (a == 1):
        i = random.randint(0,len(Lists.verbs1)-1)
        while (i in Vrecent1):
            i = random.randint(0,len(Lists.verbs1)-1)
        verb = Lists.verbs1[i]
        Vrecent1.append(i)
    elif (a == 2):
        i = random.randint(0,len(Lists.verbs2)-1)
        while (i in Vrecent2):
            i = random.randint(0,len(Lists.verbs2)-1)
        verb = Lists.verbs2[i]
        Vrecent2.append(i)
    else:
        i = random.randint(0,len(Lists.verbs3)-1)
        while (i in Vrecent3):
            i = random.randint(0,len(Lists.verbs3)-1)
        verb = Lists.verbs3[i]
        Vrecent3.append(i)      
    return(verb)
def nounGen(a): #Returns a noun/object for use in random phrase generation
    if (len(Nrecent1) >= len(Lists.nouns1)*0.9):
        del Nrecent1[0]
    elif (len(Nrecent2) >= len(Lists.nouns2)*0.9):
        del Nrecent2[0]
    elif (len(Nrecent3) >= len(Lists.retaliationNouns)*0.9):
        del Nrecent3[0]
    if (a == 1):
        i = random.randint(0,len(Lists.nouns1)-1)
        while (i in Nrecent1):
            i = random.randint(0,len(Lists.nouns1)-1)
        noun = Lists.nouns1[i]
        Nrecent1.append(i)
    elif (a == 2):
        i = random.randint(0,len(Lists.nouns2)-1)
        while (i in Nrecent2):
            i = random.randint(0,len(Lists.nouns2)-1)
        noun = Lists.nouns2[i]
        Nrecent2.append(i)
    else:
        i = random.randint(0,len(Lists.retaliationNouns)-1)
        while (i in Nrecent3):
            i = random.randint(0,len(Lists.retaliationNouns)-1)
        noun = Lists.retaliationNouns[i]
        Nrecent3.append(i)
    return(noun)
def retaliate(a): #Returns a randomized threatening / offensive statement
    if (a == 1):
        response = introGen(3)+verbGen(1)+nounGen(3)
    elif(a == 2):
        response = phraseGen()
    return(response)
def phraseGen(): #Returns a random phrase that Henry's creators made him able to say
    if (len(Precent) >= len(Lists.phrases)*0.9):
        del Precent[0]
    i = random.randint(0,len(Lists.phrases)-1)
    while (i in Precent):
        i = random.randint(0,len(Lists.phrases)-1)
    phrase = Lists.phrases[i]
    Precent.append(i)
    return(phrase)
bot.run(os.getenv('TOKEN'))
