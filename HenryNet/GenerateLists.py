from ControlChars import stopChar, shitpostChar, retaliateChar
from os import path
import sys
import random

sys.path.append("../")

from Lists import statementIntros, questionIntros, retaliationIntros
from Lists import verbs1, verbs2, verbs3
from Lists import nouns1, nouns2, retaliationNouns
from Lists import phrases

SAMPLES = 20000

def get_data():
    shitposts = []
    retaliations = []

    # Structure 1
    intro_punctuation_statements = list(zip(statementIntros, ["." for i in range(len(statementIntros))]))
    intro_punctuation_questions = list(zip(questionIntros, ["?" for i in range(len(questionIntros))]))
    intro_with_punctuation = intro_punctuation_statements + intro_punctuation_questions
    for intro in intro_with_punctuation:
        for verb in verbs1:
            for noun in nouns1:
                shitposts.append(intro[0] + verb + noun + intro[1])

        for verb in verbs2:
            for noun in nouns2:
                shitposts.append(intro[0] + verb + noun + intro[1])

        for verb in verbs3:
            shitposts.append(intro[0] + verb + intro[1])

    # Structure 2
    for phrase in phrases:
        shitposts.append(phrase)

    # Structure 3
    for intro in retaliationIntros:
        for verb in verbs1:
            for noun in retaliationNouns:
                retaliations.append(intro + verb + noun)

    return (shitposts, retaliations)


shitposts, retaliations = get_data()
print("Calculated " + str(len(shitposts)) + " shitposts and " + str(len(retaliations)) + " retaliations")

delimited_shitposts = [shitpostChar + shitpost + stopChar for shitpost in shitposts]
delimited_retaliations = [retaliateChar + retaliation + stopChar for retaliation in retaliations]

print("Random shitpost: " + random.choice(shitposts))
print("Random retaliation: " + random.choice(retaliations))

# combined = delimited_shitposts + delimited_retaliations
# random.shuffle(combined)

random.shuffle(delimited_shitposts)
random.shuffle(delimited_retaliations)

n_shitposts = delimited_shitposts[:SAMPLES]
n_retaliations = delimited_retaliations[:SAMPLES]

# data = "".join(combined[:SAMPLES])

sps = ''.join(n_shitposts)
rs = ''.join(n_retaliations)

with open("shitposts.txt", "w+", encoding='utf-8') as f:
    f.write(sps)

with open("retaliations.txt", "w+", encoding='utf-8') as f:
    f.write(rs)
