from os import path
from textgenrnn import textgenrnn

def train(type, data_dir, resume=False):
    model_name = 'henrynet_' + type

    train_cfg = {
        'line_delimited': False,
        'num_epochs': 10,
        'gen_epochs': 2,
        'batch_size': 1024,
        'train_size': 0.8,
        'dropout': 0.0,
        'max_gen_length': 300,
        'validation': False,
        'is_csv': False,

    }

    if resume:
        textgen = textgenrnn(
            name=model_name,
            weights_path=model_name + "_weights.hdf5",
            vocab_path=model_name + "_vocab.json",
            config_path=model_name + "_config.json"
        )
    else:
        textgen = textgenrnn(
            name=model_name
        )

    textgen.train_from_largetext_file(
        file_path=path.abspath(data_dir),
        new_model=(not resume),
        num_epochs=train_cfg['num_epochs'],
        gen_epochs=train_cfg['gen_epochs'],
        batch_size=train_cfg['batch_size'],
        train_size=train_cfg['train_size'],
        dropout=train_cfg['dropout'],
        max_gen_length=train_cfg['max_gen_length'],
        validation=train_cfg['validation']
    )