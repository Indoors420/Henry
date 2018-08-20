import random, typing
import Lists, RecentGen

def respond(message: typing.AnyStr, gen_type: int=1) -> str:
    if gen_type == 1:
        return msg_response(message)
    elif gen_type == 2:
        return Lists.errorMsgGen(1)


def msg_response(message: typing.AnyStr) -> str:
    question_type = classify(message)
    if question_type == "why":
        msg = Lists.introGen(3, 1)+Lists.nounGen(1)+" "+Lists.verbGen(1)+" "+Lists.nounGen(1)
    elif question_type == 'how':
        msg = Lists.introGen(3, 2)+Lists.nounGen(1)+" "+Lists.verbGen(1)+"s "+Lists.nounGen(1)
    elif question_type == 'who' or question_type == 'what':
        msg = Lists.nounGen(1)
    elif question_type == 'when':
        msg = Lists.timeGen()
    else:
        chance = random.randint(0,1)
        if (chance == 0):
            msg = Lists.phraseGen(1)
        else:
            msg = retaliate()
    
    return msg


def classify(message: typing.AnyStr) -> str:
    if "why" in message: return "why"
    elif "how" in message: return "how"
    elif "who" in message: return "who"
    elif "what" in message or "which" in message: return "what"
    elif "when" in message: return "when"
    
    return None


def shitpost():  # Uses returned intros, verbs, and nouns to create a coherent shitpost
    a = random.randint(0,10)
    if a < 5:
        intro = Lists.introGen(1, None)
        end = "."
    else:
        intro = Lists.introGen(2, None)
        end = "?"
    b = random.randint(0,100)
    if b < 50:
        verb = Lists.verbGen(1)+" "
        noun = Lists.nounGen(1)
    elif 68 > b > 50:
        verb = Lists.verbGen(2)+" "
        noun = Lists.nounGen(2)
    elif 90 > b > 68:
        shit = Lists.phraseGen(1)
        return(shit)       
    else:
        verb = Lists.verbGen(3)  # ends without noun
        noun = ""
    shit = intro+verb+noun+end
    return(shit)


def retaliate():
    chance = random.randint(0,100)
    if chance < 45:
        retaliation = "You are "+Lists.adjectiveGen(1)
    elif 45 <= chance <= 85:
        retaliation = Lists.introGen(4, None)+Lists.verbGen(1)+" your "+Lists.nounGen(3)
    elif chance > 85:
        retaliation = Lists.phraseGen(2)
    return retaliation