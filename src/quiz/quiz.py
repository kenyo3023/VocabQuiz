import json
import os
import random
from argparse import ArgumentParser

def check_score(correct, wrong):
    return (correct / (correct + wrong)) * 100

class Quiz():
    def __init__(self, vocabs, num_option=4, seed=0):
        self.vocabs = vocabs
        self.vocabs_list = list(vocabs.keys())
        self.num_option = num_option
        self.seed = seed
        self.correct = 0
        self.wrong = 0
    
    def generate_options_answer(self):
        # random.seed(0)
        self.options_list = random.choices(self.vocabs_list, k=self.num_option) 
        self.answer = random.choice(self.options_list)
        self.options_index = [i for i in range(len(self.options_list))]
        self.option_min = self.options_index[0]
        self.option_max = self.options_index[-1]
        
    def enter_answer(self):
        isvalid = False
        while isvalid == False:
            self.input_ = input('input your answer: ')
            if self.input_.isdigit():
                self.input_ = int(self.input_)
                if self.input_ not in self.options_index:
                    print('Please enter the index [%d-%d]'%(self.option_min, self.option_max))
                    continue
                isvalid = True
            else:
                print('Please enter the index [%d-%d]'%(self.option_min, self.option_max))
        
    def check_answer(self, input_):
        self.input_answer = self.options_list[input_]
        print('Your Input is "%s"'%self.input_answer)
        print('The Correct Answer is "%s"'%self.answer)
        if self.input_answer == self.answer:
            self.correct += 1
            print('Correct !!!')
        else:
            self.wrong += 1
            if save_penalty:
                self.vocabs[self.answer]['proficiency'] += 1
            print('Wrong Answer')

    def generate_question(self):
        self.generate_options_answer()
        self.answer_meta = self.vocabs[self.answer]
        self.answer_mean = self.answer_meta['mean']
        print('\nQuestion:', self.answer_mean)
        for i in self.options_index:
            print('(%s) %s'%(i, self.options_list[i]))
        isvalid = self.enter_answer()
        self.check_answer(self.input_)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--n", help="number of questions.", default=5, type=int)
    parser.add_argument("--filename", help="the filename of the vocabulary.", default='../../dictionary/dictionary_test.json')
    parser.add_argument("--save_penalty", help="whether to save the wrong vocabs in this quiz.", action='store_true')
    parser.add_argument("--scope", help="the vocab scope is based on the date of storage", default=None)
    args = parser.parse_args()

    n = args.n
    filename = args.filename
    save_penalty = args.save_penalty
    scope = args.scope

    with open(filename) as infile:
        vocabs = json.load(infile)

    if scope is not None:
        vocabs = {key:value for key, value in vocabs.items() if value['date'] == scope}
        if len(vocabs) == 0:
            raise ValueError('Your vocabulary in "%s" is empty'%scope)
    quiz = Quiz(vocabs)
    for i in range(n):
        quiz.generate_question()
    score = check_score(quiz.correct, quiz.wrong)
    print('\nYour Score: %d'%score)

    if save_penalty:
        # save the dictionary json
        with open(filename, 'w') as outfile:
            json.dump(vocabs, outfile, indent=4)
    