import os
import json
from datetime import date

def load_save_dump(filename, vocab, vocab_meta, proficiency):
    vocabs = load(filename)
    vocabs = save(vocabs, vocab, vocab_meta, proficiency)
    dump(filename, vocabs)

def load(filename):
    # check whether exist the dictionary json
    if not os.path.exists(filename):
        init = {}
        with open(filename, 'w') as outfile:
            json.dump(init, outfile)

    # load the dictionary json
    with open(filename) as infile:
        vocabs = json.load(infile)
    return vocabs

def save(vocabs, vocab, vocab_meta, proficiency=None, save_date=True):
    # save the new vocab to dictionary json
    meta = {}
    meta['mean'] = vocab_meta
    if proficiency != None:
        meta['proficiency'] = int(proficiency)
    if save_date:
        today = str(date.today())
        meta['date'] = today
    vocabs[vocab] = meta
    return vocabs

def dump(filename, vocabs):
    # save the dictionary json
    with open(filename, 'w') as outfile:
        json.dump(vocabs, outfile, indent=4)