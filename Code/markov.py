import dictogram
from clean import get_clean_words
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

def get_random_word(markov, word_list):
    '''Takes given word and returns a random word in its markov list'''
    start_word = choice([word for word in word_list if word != word_list[-1]])
    total_links = len(markov[start_word])
    if total_links >= 2:
        # janky fix to avoid picking last word
        random = randint(0, total_links-2)
        if total_links == 1:
            random = randint(0, 1)
        chain = markov[start_word][random]
    else:
        chain = markov[start_word][0]
    return chain

def generate_sentence(num_words, markov, word_list):
    sentence = ""
    for i in range(0, num_words):
        word = get_random_word(markov, word_list)
        # print(i+1, word)
        if i == 0:
            sentence = word.capitalize()
        elif i != num_words - 1:
            sentence += " " + word
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            sentence += choice(punctuation)
    # output your sentence
    # print(sentence + "\t: " + str(num_words) + " words")
    return sentence


if __name__ == "__main__":
    word_list = get_clean_words("text_files/markov.txt")
    histogram = dictogram.Dictogram(word_list)
    num_words = sys.argv[1]
    markov = markov(word_list)
    print(generate_sentence(num_words, markov, word_list))
