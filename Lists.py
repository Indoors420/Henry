import RecentGen, random, datetime
blackList = [ #People not allowed to use Henry's commands
    "150420859683733504", # @Lunar
]
whitelist = [
    "187656701380526080", # @Christ Himself
]
def errorMsgGen(a):
    rejected = [
        "nah lol",
        "no",
        "maybe later",
        "don't feel like it",
        "ask someone else",
        "Never interupt me eating beans and watching Cars 2 ever a-fucking-gain",
        "nah man I don't really feels like it right now lmfao",
        "I mean I could if I wanted to, but why the fuck would I LMAO",
        "don't ever ask me that ever again",
        "sorry I don't speak gay retard",
        "I'll bet you'd really like me to do that, now wouldn't you?",
        "The fact that you think that I'd do that for you is really fucking dumb lol",
        "shut up nerd",
        "fuck you idiot, always askin me to do shit, do it yourself you worthless fucking idiot",
        "Ok retard, I can't just do everything around here.",
    ]
    commandError = [ #If someone calls a command that doesn't exist
        "Are you sure you typed that correctly retard?",
        "I don't know what the fuck you want from me.",
        "Take your time, try again.",
        "I don't understand, try being slightly less retarted.",
    ]
    noRights = [ #If someone doesn't have server permission to use a command
        "Sorry, but you don't have any rights.",
        "Nah lol.",
        "You are not tall enough to ride this ride.",
        "You are not authorized retard",
        "I would, but I won't",
        "Bitch, shutcho ass up",
        "Hey chief, I'm not capable of doing that for you",
        "Nah nigga you gay HAHA",
        "Nah nigga you ain't cool enough for that shit",
        "You the type of nigga to call other niggas king, get the fuck outta here lmfao",
        "Maybe if the people on this server liked you enough, you'd be able to do that",
        "If you ever ask that again I will have sex with your dad",
    ]
    badArg = [ #If a command doesn't get the required or correct argument
        "Do not waste my time",
        "Come on now retard, lets be serious.",
        "What kind of surface were you dropped head-first onto as a child?",
    ]
    clear1k = [ #Henry won't clear more than 999 messages at a time
        "Do you really fucking expect me to clear that many messages right now?",
        "Yeah you can piss right off, I'm not clearing that many messages.",
        "I am not emotionally capable of clearing any more than 999 messages at a time.",
        "I am way too lazy to even think of doing that.",
        "If you were smart you'd just ask me to clear 999 multiple times, but no.",
        "If you think I can do that then you are just another shit idiot.",
        "Why don't you clear all those messages yourself you fucking nerd?",
        "No. I refuse.",
    ]
    botOutrank = [ #If Henry isn't a high enough rank
        "I'm not physically capable of doing that.",
        "Would if I could",
        "Tried and failed",
        "They're too powerful",
    ]
    authorOutrank = [ #If someone tries to use Henry's rank to kick someone higher than them...
        "Sorry but it don't work like that.",
        "Clever but no",
        "Nice try",
        "I want to, but I'd probably get in trouble.",
    ]
    if (a == 1):
        errorMsg = rejected[random.randint(0,len(rejected)-1)]
    elif (a == 2):
        errorMsg = commandError[random.randint(0,len(commandError)-1)]
    elif (a == 3):
        errorMsg = noRights[random.randint(0,len(noRights)-1)]
    elif (a == 4):
        errorMsg = badArg[random.randint(0,len(badArg)-1)]
    elif (a == 5):
        errorMsg = clear1k[random.randint(0,len(clear1k)-1)]
    elif (a == 6):
        botOutrank = botOutrank[random.randint(0,len(botOutrank)-1)]
    elif (a == 7):
        errorMsg = authorOutrank[random.randint(0,len(authorOutrank)-1)]
    else:
        print("")
        print("")
        print("What the fuck?")
        print("")
        print("")
    return(errorMsg)
def introGen(a, b): #Returns a sentence starter for use in random phrase generation
    statementIntros = [
        "I ",
        "Well god fucking damn, I cannot believe that these niggas don't want to ",
        "I doubt these niggas will appreciate it when I ", 
        "My creator told me that I’m not allowed to ",
        "I don’t think ya’ll understand the fact that I could ",
        "I don’t think ya’ll understand the fact that I really want to ",
        "I literally can’t even ",
        "Hot damn it's time to ",
        "I really think that is time for me to ",
        "I'm finna ",
        "If y'all don't stop, I might just ",
        "Howdy folks, in today's video we are going to ",
        "These niggas won't be laughing when I ",
        "Shit, I really just might have to ",
        "These niggas don't understand that I'm just tryna ",
        "I'm going to make a genuine effort to ",
        "Step 1: ",
        "Step 2: ",
        "Step 3: ",
        "Step 4: ",
        "Step 5: ",
        "Fuck it, I'm just gonna ",
        "I think it would be best if everyone could just ",
        "I'm tryna ",
        "I need 5 people to help me ",
        "Idea: ",
        "I'm finna fake being sick so I can ",
    ]
    questionIntros = [
        "Okay, so when should I ",
        "Who dares me to ",
        "Why don't y'all just ",
        "Anyone care if I ",
        "Why does everyone get mad when I ",
        "Y'all mind if I ",
        "Can anyone help me ",
        "What if we all just ",
        "Who's tryna ",
        "Anyone wanna ",
        "Anyone down to ",
    ]
    answerIntros1 = [
        "Because ",
    ]
    answerIntros2 = [
        "Well basically ",
    ]
    retalIntros = [
        "I will ",
        "I could ",
        "I might have to ",
        "Don't make me ",
        "I have the urge to ",
    ]
    if (len(RecentGen.intros1) >= len(statementIntros) * 0.85):
        del RecentGen.intros1[0]
    elif (len(RecentGen.intros2) >= len(questionIntros) * 0.85):
        del RecentGen.intros2[0]
    elif (len(RecentGen.intros4) >= len(retalIntros) * 0.85):
        del RecentGen.intros4[0]
    if (a == 1):
        i = random.randint(0, len(statementIntros)-1)
        while (i in RecentGen.intros1):
            if (i < len(statementIntros)-1):
                i += 1
            else:
                i = 0
        RecentGen.intros1.append(i)
        intro = statementIntros[i]
    elif (a == 2):
        i = random.randint(0, len(questionIntros)-1)
        while (i in RecentGen.intros2):
            if (i < len(questionIntros)-1):
                i += 1
            else:
                i = 0
        RecentGen.intros2.append(i)
        intro = questionIntros[i]
    elif (a == 3):
        if (b == 1):
            i = random.randint(0, len(answerIntros1)-1)
            while (i in RecentGen.intros3):
                if (i < len(answerIntros1)-1):
                    i += 1
                else:
                    i = 0
            intro = answerIntros1[i]
        elif (b == 2):
            i = random.randint(0, len(answerIntros2)-1)
            while (i in RecentGen.intros3):
                if (i < len(answerIntros2)-1):
                    i += 1
                else:
                    i = 0
            intro = answerIntros2[i]
        RecentGen.intros3.append(i)  
    elif (a == 4):
        i = random.randint(0, len(retalIntros)-1)
        while (i in RecentGen.intros4):
            if (i < len(retalIntros)-1):
                i += 1
            else:
                i = 0
        RecentGen.intros4.append(i)
        intro = retalIntros[i]
    return(intro)
def verbGen(a): #Returns a verb for use in random phrase generation
    verbs1 = [
        'dox', 
        'publish', 
        'delete', 
        'tickle', 
        'weld', 
        'twist', 
        'soil', 
        'relocate', 
        'submerge', 
        'climb', 
        'focus on', 
        'hide from', 
        'penetrate', 
        'shred', 
        'go beast mode on', 
        'permanently disable', 
        'deep fry', 
        'obliterate', 
        'systematically oppress', 
        'flood', 
        'rob', 
        'compress', 
        'bless', 
        'invent', 
        'chew', 
        'lick', 
        'castrate', 
        'eat', 
        'view', 
        'consume', 
        'shwamp', 
        'assassinate', 
        'burn', 
        'capture', 
        'fuck', 
        'undress', 
        'sodomize', 
        'drown', 
        'bully', 
        'build', 
        'avoid', 
        'crawl into', 
        'vaporize', 
        'criticize', 
        'beat', 
        'slap', 
        'grill', 
        'donate', 
        'bite', 
        'assault', 
        'rewind', 
        'prank',
    ]
    verbs2 = [ #verbs2 verbs are concatinated with nouns3 nouns
        "look into",
        "try",
        "invest in",
        "check out",
        "look at some",
    ]
    verbs3 = [ #verbs3 verbs are not concatinated with a noun
        "cuddle",
        "do the 'in my feelings' challenge",
        "cry",
        "crawl",
        "undress",
        "start some shit",
        "sodomize a disabled walrus",
        "assault the disabled",
        "pillage",
        "die",
        "evolve",
        "condensate",
        "pillage",
        "bust a move",
        "do it to 'em",
        "stabilize the economy",
        "restart Isis",
        "commit insurance fraud",
        "get on some hee hee haw haw shit",
    ]
    if (len(RecentGen.verbs1) >= len(verbs1) * 0.85):
        del RecentGen.verbs1[0]
    elif (len(RecentGen.verbs2) >= len(verbs2) * 0.85):
        del RecentGen.verbs2[0]
    elif (len(RecentGen.verbs3) >= len(verbs3) * 0.85):
        del RecentGen.verbs3[0]
    if (a == 1):
        i = random.randint(0,len(verbs1)-1)
        while (i in RecentGen.verbs1):
            if (i < len(verbs1)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs1.append(i)
        verb = verbs1[i]
    elif (a == 2):
        i = random.randint(0,len(verbs2)-1)
        while (i in RecentGen.verbs2):
            if (i < len(verbs2)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs2.append(i)
        verb = verbs2[i]
    elif (a == 3):
        i = random.randint(0,len(verbs3)-1)
        while (i in RecentGen.verbs3):
            if (i < len(verbs3)-1):
                i += 1
            else:
                i = 0
        RecentGen.verbs3.append(i)
        verb = verbs3[i]
    return(verb)
def adverbGen():
    adverbs = [
        "mega ",
        "very ",
        "quite ",
        "extremely ",
        "astonishingly ",
        "surprisingly ",
        "really ",
        "pretty ",
    ]
    if len(RecentGen.adverbs) >= len(adverbs) * 0.8:
        del adverbs[0]
    i = random.randint(0,len(adverbs))
    while i in RecentGen.adverbs:
        if (i < len(adverbs)-1):
            i += 1
        else:
            i = 0
    adverb = adverbs[i]
    return(adverb)
def nounGen(a): #Returns a noun/object for use in random phrase generation
    nouns1 = [
        "this sandwich",
        "the CarFax™",
        "the cheese tub",
        "Harvard",
        "the president",
        "an orphanage",
        "some battery acid",
        "some farm animals",
        "some shit",
        "these cheez-its™",
        "the economy",
        "the man-man",
        "the weird kid",
        "the IRS",
        "these legos™",
        "the neighbor boy",
        "my neighbor's boat",
        "some foreigners",
        "the cats that live under my grandmas house",
        "the milkman",
        "Bitcoin",
        "these niggas",
        "Alexa",
        "the christian minority in Afghanistan",
        "some catholic priests",
        "minecraft",
        "Russ",
        "Wal-Mart customer service",
        "Fortnite",
        "my neighbor's teenage son",
        "the rap game",
        "communism",
        "the fellas",
        "Dwayne Johnson",
        "Allah",
        "a microwave",
        "an adult polar bear",
        "a pirated copy of Shrek 2",
        "some alphabet soup",
    ]
    nouns2 = [ #"Interest" nouns
        "juicing",
        "cryptocurrency",
        "sexual harassment",
        "wakeboarding",
        "golf",
        "arson",
        "dentistry",
        "Karate",
        "Baseball",
        "Heroin",
        "scientology",
        "Judaism",
        "Islam",
    ]
    retalNouns = [
        "toes",
        "pee pee",
        "teeth",
        "rib-cage",
        "forehead",
        "limbs",
        "feet",
        "tiddy",
        "shoulders",
        "possessions",
        "family",
        "dog",
        "skin",
        "borger",
        "face",
        "financial opportunities"
    ]
    if (len(RecentGen.nouns1) >= len(nouns1) * 0.85):
        del RecentGen.nouns1[0]
    elif (len(RecentGen.nouns2) >= len(nouns2) * 0.85):
        del RecentGen.nouns2[0]
    if (a == 1):
        i = random.randint(0,len(nouns1)-1)
        while (i in RecentGen.nouns1):
            if (i < len(nouns1)-1):
                i += 1
            else:
                i = 0
        RecentGen.nouns1.append(i)
        noun = nouns1[i]
    elif (a == 2):
        i = random.randint(0,len(nouns2)-1)
        while (i in RecentGen.nouns2):
            if (i < len(nouns2)-1):
                i += 1
            else:
                i = 0
        RecentGen.nouns2.append(i)
        noun = nouns2[i]
    elif (a == 3):
        i = random.randint(0,len(retalNouns)-1)
        while (i in RecentGen.nouns3):
            if (i < len(retalNouns)-1):
                i += 1
            else:
                i = 0
        RecentGen.nouns3.append(i)
        noun = retalNouns[i]
    return(noun)
def adjectiveGen(a):
    negative = [
        "gay ",
        "rarted ",
        "stickey ",
        "small ",
        "deformed ",
        "fat ",
        "insignificant ",
        "dumb ",
        "stupid ",
        "goofy ",
        "bad ",
        "awful ",
        "terrible ",
        "outrageous ",
        "vast ",
        "immense ",
        "long ",
        "curved ",
        "bitter ",
        "lil ",
        "whack ",
        "insane ",
    ]
    positive = [
        "cool ",
        "sick ",
        "rad ",
        "zesty ",
        "sweet ",
        "tasty ",
        "holy ",
        "new ",
        "gentle ",
        "good ",
        "massive ",
    ]
    neutral = [
        "big ",
        "slippery ",
        "squishy ",
        "moist ",
        "empty ",
        "juicy ",
    ]
    if len(RecentGen.adjectives1) >= len(negative) * 0.8:
        del RecentGen.adjectives1[0]
    elif len(RecentGen.adjectives2) >= len(positive) * 0.8:
        del RecentGen.adjectives2[0]
    elif len(RecentGen.adjectives3) >= len(neutral) * 0.8:
        del RecentGen.adjectives3[0]
    if a == 1:
        i = random.randint(0, len(negative)-1)
        while (i in RecentGen.adjectives1):
            if (i < len(negative)-1):
                i += 1
            else:
                i = 0
        adj = negative[i]
        RecentGen.adjectives1.append(i)
    elif a == 2:
        i = random.randint(0, len(positive)-1)
        while (i in RecentGen.adjectives2):
            if (i < len(positive)-1):
                i += 1
            else:
                i = 0
        adj = positive[i]
        RecentGen.adjectives2.append(i)
    elif a == 3:
        i = random.randint(0, len(neutral)-1)
        while (i in RecentGen.adjectives3):
            if (i < len(neutral)-1):
                i += 1
            else:
                i = 0
        adj = neutral[i]
        RecentGen.adjectives3.append(i)

    return(adj)
def phraseGen(a): #Returns a random phrase that Henry's creators made him able to say
    phrases = [
        "obanacare you bitch, lol",
        "Girls don't want luxury handbags and expensive clothes they want frag grenades and illegal firearms",
        "Girls think it's sweet when u throw a fucking flash bang grenade thru their window in the morning to wake them up for work",
        "White people be like 'oh yea ur cruisin for a bruisin bud.'",
        "When I say we gonna eat, I mean me and my tapeworm",
        "F.R.E.E. that spells free, credit report .com baby",
        "In this world you either crank that soulja boy or it cranks you",
        "Democracy Time",
        "Eat spicy goodness like a boss.",
        "I don't trust like that.",
        "How do I rotate text in paint?",
        "You just gotta straight up eat the lettuce.",
        "I am a gamer",
        "Respect the pouch.",
        "One fortnite burger please",
        "I'm your dad Luke.",
        "Dang gummit...",
        "If barraco barner is our president why is he getting involved with Russia, scary.",
        "Tip: turn your location services off to save battery life",
        "mmmmmmmmmmm, nice",
        "*snap* Yup, this is going in my cringe compilation.",
        "EPIC FAIL, the bitch had IOS 7 on the iPhone 4.",
        "Milk taste better when it go lumpy",
        "When Chief Keef said 'we removed ya post cuz it violated community guidelines', I really felt that.",
        "Peen = Ween",
        "I might pistol whip myself",
        "Hit the Quan.",
        "Gang practice at 8:30 tonight, bring your weapons.",
        "Water is cancelled.",
        "If Chick Fil A sold bath bombs white people would break the economy.",
        "I'm wearing Old Navy again.",
        "When I'm out of the cheese, I can't handle it.",
        "Who's REALLY responsible for Ｔｈｅ Ｃｏｌｏｓｓａｌ Ｐｉｌｌａｒ ｏｆ Ｗａｓｐ Ｅｇｇｓ?",
        "Tonight's the night that I confront the tall, black, ominous figure that stands at the foot of my bed at while I sleep.",
        "New cop: a 50-gallon barrel of molten Crayola™ crayons.",
        "Cool beans man.",
        "Cool and Good.",
        "Why do girls throw their pee away?",
        "And I freaked it.",
        "Big body whats yo build boy", 
        "Uzi not again.", 
        "My chain, my pants, my pants with the chain.", 
        "Who them YBN Niggas why they always stuntin?",
        "Bounce out with that fo fo.", 
        "Have you called your mother yet today and told her you loved her?",
        "School is very hard.", 
        "Fuck fuck fuck a beat haha yes I am trying to beat a case.", 
        "[Verse 3: Young Thug] Nigga I'm a crack addict.", 
        "Why you pussy niggas at home watching house wives re-runs?",
        "Ya'll ever paint piss mosaics in the jimmy john bathroom?", 
        "Ok be honest here who the fuck took all my chocolate covered almonds? It isn't funny guys I really want them back.",
        "Don't you open up that window.", 
        "Shawty know I kill people.", 
        "Fun fact about me: My dad hits me with his belt at least twice a week.", 
        "Hard to accept truth: silverware is NOT to be used in the 17th sector.", 
        "Bro I can't believe your grandma died I'm so sorry, btw get on fortnite.", 
        "Which one of you cock suckers told my little brother that the moon is made of philly cheesesteaks?",
        "Hey guys I can't get on xbox tonight my mom said I have to do my homework.", 
        "My mom just walked in on me watching Seinfeld oh my god I'm so dead.", 
        "I'm trying out for the varsity fortnite team, wish me luck.", 
        "[Verse 1: Jay Z] I'm addicted to buying unbelievably expensive custom helicopters (yeeeeeeaaahhhh) In a brief moment of lucidity I went to the helicopter dealership and told them 'Do not, under any circumstances, sell me more helicopters' I was back there half an hour later, wearing a fake moustache, and I said 'Hello gentlemen, I am Ray Z, a man you have never met before. Give me 10,000 helicopters covered in diamonds.'",
        "You fucking idiots pissed me off and now I'm gonna have to go beast mode.", 
        "shit poopy pee pee.",
        "damn gravy u snapped.",
        "damn it's really a vibe up in here right now.",
        "Beast Mode is loading, I'll you guys know when it's activated.", 
        "Latinas get a software update for their ass every month.", 
        "This ain't it chief.",
        "My girl mad at me cuz I been straight keeping the cubes bruh lmao.", 
        "WNBA be like: 'Wow a new record for loads of laundry done and sandwiches made in a single game!'",
    ]
    retalPhrases = [
        "die",
        "fuck you",
        "I will tell mom",
        "coward",
        "bitch",
        "okay retard",
        "shut the fuck",
    ]
    if (len(RecentGen.phrases) >= len(phrases) * 0.85):
        del RecentGen.phrases[0]
    if (a == 1):
        i = random.randint(0,len(phrases)-1)
        while (i in RecentGen.phrases):
                if (i < len(phrases)-1):
                    i += 1
                else:
                    i = 0
        RecentGen.phrases.append(i)
        phrase = phrases[i]
    elif (a == 2):
        i = random.randint(0,len(retalPhrases)-1)
        while (i in RecentGen.phrases2):
                if (i < len(retalPhrases)-1):
                    i += 1
                else:
                    i = 0
        RecentGen.phrases2.append(i)
        phrase = retalPhrases[i]
    return(phrase)
def timeGen():
    times = [
        "now",
        "later",
        "in a few",
        "another time",
        "not yet",
        "tomorrow",
        "last week",
    ]
    chance = random.randint(0,10)
    if (chance > 5):
        year = random.randint(2018, 2040)
        month = random.randint(1, 12)
        day = random.randint(1, 28) #need logic for limit of days for each month because the Gregorian calender is mega gay
        time = datetime.datetime(year, month, day).strftime('%d %B, %Y')
    else:
        time = times[random.randint(0, len(times)-1)]
    return(time)