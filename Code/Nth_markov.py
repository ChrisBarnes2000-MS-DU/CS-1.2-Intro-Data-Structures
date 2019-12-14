from utils import time_it, get_clean_words
# from clean_tokenizer import tokenize
from dictogram import Dictogram
from queue import Queue
from random import sample, choice, randint
import sys


class Nth_Order_Markov():
    def __init__(self, words_list=None, nth_order=2):
        """Construct a Markov Chain model.
           Param: words_list(list of str)"""
        self.corpus = words_list
        self.total_words = len(self.corpus)
        self.transition = Queue(maxsize=nth_order+2)
        self.chain = self.populate_chain(nth_order)

    def populate_chain(self, nth_order):
        self.chain = Dictogram()
        Nth_len = self.total_words-nth_order
        # print("Total words: {}, {} words for Nth_order: {} word pairs".format(self.total_words, Nth_len, nth_order))
        for i in range(Nth_len):
            """Look through available words in the corpus relative to the window size"""
            cur = ""
            nxt = ""
            for pos in range(1, nth_order+1):
                self.transition.put(self.corpus[i+(pos-1)])
                self.transition.put(self.corpus[i+pos])
                if pos > 1:
                    cur += " "
                    nxt += " "
                cur += self.transition.get()
                nxt += self.transition.get()
            # print("Current pair: {} -->\t Next pair: {}\n".format(cur, nxt))
            if self.chain.get(cur, None) is None:
                # print("\n--Adding NEW--")
                self.chain[cur] = Dictogram([nxt])
            else:
                # print("\n--Adding to Count--")
                self.chain[cur].add_count(nxt)
            # print(self.chain)
        return self.chain

    def get_random_word(self, start_word):
        '''Takes given word and returns a random word in its markov list'''
        weight_options = self.chain[start_word]
        # print("weight_options: ", weight_options)

        total_links = 0
        # for link, count in weight_options.items():
        for count in weight_options.values():
            total_links += count
            # print(link, count)

        # print("{} has {} links to go to: {}".format(start_word, total_links, weight_options))

        choice = weight_options.sample()
        # print("New word pair: ", choice, "\n")
        return choice

    def generate_sentence(self, num_words, nth_order):
        sentence = ""
        start = ""
        pos = randint(0, len(self.corpus))
        for i in range(0, nth_order):
            if i >= 1:
                start += " "
            start += self.corpus[pos+i]
        # print("\n--start_word--\t", start)
        # start = start.capitalize()
        sentence += start
        word_pair = start

        for _ in range(1, num_words-nth_order+1):
            word_pair = self.get_random_word(word_pair)
            # print("\n--next_word-- \t", word)
            sentence += " " + word_pair.split()[nth_order-1]

        punctuation = [".", "!", "?", "..."]
        sentence += choice(punctuation)
        return sentence


if __name__ == "__main__":
        # The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 3:
        # print("Try again with 1 argument: the number of words to give!")
        num_words = 10
        Nth_order = 2
    else:
        #All parameters except the number of words will be hard-coded.
        num_words = int(sys.argv[1])
        Nth_order = int(sys.argv[2])

    # word_list = get_clean_words("text_files/markov.txt")
    # word_list = get_clean_words("text_files/second_markov.txt")
    # word_list = get_clean_words("text_files/fish.txt")
    # word_list = get_clean_words("text_files/zombie.txt")
    word_list = get_clean_words("text_files/corpus.txt")
    # source = open("text_files/excerpt.txt").read()
    # word_list = tokenize(source)
    # print("\t--word_list--\n", word_list)

    markov = Nth_Order_Markov(word_list, nth_order=Nth_order)
    # print("\n\t--Nth_order_markov--{}--\n".format(Nth_order), markov.chain)

    # sentence = markov.generate_sentence(num_words=num_words, nth_order=Nth_order)
    # print("\n\t--Random Sentence length {}--\n{}".format(num_words, sentence))
    # print("\t--Actuall length {}--".format(len(sentence.split())))


    for _ in range(5):
        sentence = markov.generate_sentence(num_words=num_words, nth_order=Nth_order)
        print(sentence)
