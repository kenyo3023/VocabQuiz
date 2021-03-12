import os
import json

from load_save_dump import load, dump

rm = input('Enter the vocab you want to delete: ')
filename = '../dictionary/dictionary.json'
vocabs = load(filename)

try:
    del vocabs[rm]
    dump(filename, vocabs)
    print('%s had deleted'%rm)
except:
    print('make sure %s is in dictionary'%rm)

