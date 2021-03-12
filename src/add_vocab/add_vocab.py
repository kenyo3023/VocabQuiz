import os
import json

from load_save_dump import load_save_dump

vocab = input('Enter the vocab: ')
vocab_meta = {}
a_list = ['n', 'v', 'a', 'ad', 'c']
while True:
    mean = input('Enter the mean of vocab: ')
    if mean == 'quit':
        break

    speech = input('Enter the speech of vocab: ')
    if speech == 'quit':
        break

    if speech not in a_list:
        print("The speech must conform to ", a_list)
        continue

    vocab_meta[speech] = mean
    keep = input('Any other meanings? [y or n]: ')
    if keep in ['No', 'no', 'N', 'n']:
        break

filename = '../dictionary/dictionary.json'
load_save_dump(filename, vocab, vocab_meta, proficiency=1)
print('added new vocab %s'%(vocab))
for speech, mean in vocab_meta.items():
    print('(%s.) %s'%(speech, mean))