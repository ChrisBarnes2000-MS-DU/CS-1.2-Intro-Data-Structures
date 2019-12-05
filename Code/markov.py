# help provided by aucoeur @ https://github.com/aucoeur/CS-1.2-Intro-Data-Structures/blob/master/Code/markov_chain.py

import dictogram
from utils import time_it, get_clean_words
from random import choice, randint
import sys

def markov(corpus):
    '''Creates word pairs and puts them into a markov dictionary'''
    pairs = []
    markov_dict = {}

    # create linked pairs
    for i in range(len(corpus)-1):
        pairs.append((corpus[i], corpus[i+1]))
    # sort through connections and make a dictionary of routes
    for first, second in pairs:
        if first in markov_dict.keys():
            markov_dict[first].append(second)
        else:
            markov_dict[first] = [second]
    return markov_dict

def get_random_word(markov, start_word):
    '''Takes given word and returns a random word in its markov list'''
    total_links = len(markov[start_word])
    # print("{} has {} links to go to: {}".format(start_word, total_links, markov[start_word]))
    if total_links >= 2:
        random = randint(0, total_links-2)
        if total_links == 1:
            random = randint(0, 1)
        chain = markov[start_word][random]
    else:
        chain = markov[start_word][0]
    return chain

def generate_sentence(num_words, markov, word_list):
    sentence = ""

    start_word = choice([word for word in word_list if word != word_list[-1]])
    # print("\n--start_word-- \t", start_word)
    sentence += start_word.capitalize()
    word = start_word

    for _ in range(1, num_words):
        word = get_random_word(markov, word)
        # print("\n--next_word-- \t", word)
        sentence += " " + word

    punctuation = [".", "!", "?", "...", "!?"]
    sentence += choice(punctuation)
    return sentence

if __name__ == "__main__":
    # num_words = sys.argv[1]
    word_list = get_clean_words("text_files/markov.txt")
    # print("\t--word_list--\n", word_list)
    
    markov = markov(word_list)
    # print("\t--markov--\n", markov)

    num_words = 10
    sentence = generate_sentence(int(num_words), markov, word_list)
    print("\nFinal Sentence of length {} is\n{}".format(num_words, sentence))
