import os
os.environ['CUDA_VISIBLE_DEVICES']="-1"

from textgenrnn import textgenrnn, utils

stopChar = chr(95)
shitpostChar = chr(123)
retaliateChar = chr(125)

dirname = os.path.dirname(__file__)

def get_gen(name):
    name = "henrynet_" + name
    weights_path = name + "_weights.hdf5"
    vocab_path = name + "_vocab.json"
    config_path = name + "_config.json"

    weights_path = os.path.join(dirname, weights_path)
    vocab_path = os.path.join(dirname, vocab_path)
    config_path = os.path.join(dirname, config_path)

    return textgenrnn(
        weights_path=weights_path,
        vocab_path=vocab_path,
        config_path=config_path,
        name=name
    )


shitpostGen = get_gen("shitpost")
retaliateGen = get_gen("retaliation")

max_gen_length = 300

def generate(gen, prefix, temperature):
    model = gen.model
    vocab = gen.vocab
    indices_char = gen.indices_char
    max_length = gen.config['max_length']

    next_char = ''
    text = list(prefix)
    while next_char != stopChar and len(text) < max_gen_length:
        encoded_text = utils.textgenrnn_encode_sequence(text[-max_length:], vocab, max_length)

        next_index = utils.textgenrnn_sample(
            model.predict(encoded_text, batch_size=1)[0],
            temperature
        )
        next_char = indices_char[next_index]
        text += [next_char]

    text = text[len(prefix):-1]
    return ''.join(text)

def shitpost(trigger, temperature=0.5):
    return generate(shitpostGen, trigger + stopChar + shitpostChar, temperature)


def retaliate(trigger, temperature=0.5):
    return generate(retaliateGen, trigger + stopChar + retaliateChar, temperature)

#print("Shitpost: " + generate_shitpost("sup my boi"))
#print("Retaliation: " + generate_retaliation("hey frick you henry"))