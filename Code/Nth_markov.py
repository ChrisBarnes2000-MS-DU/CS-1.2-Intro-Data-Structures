from utils import time_it, get_clean_words
from dictogram import Dictogram
from queue import Queue
from random import sample, choice
import sys

class Nth_Order_Markov():
    def __init__(self, words_list=None, nth_order=2):
        """Construct a Markov Chain model.
           Param: words_list(list of str)"""
        self.corpus = words_list
        self.transition = Queue(maxsize=nth_order+2)
        self.chain = self.populate_chain(nth_order)

    def populate_chain(self, nth_order):
        self.chain = Dictogram()
        for i in range(len(self.corpus)-nth_order):
            # print(i)
            while not self.transition.empty():
                self.transition.get()
            for j in range(nth_order+1):
                self.transition.put(self.corpus[i+j])
            # print(self.transition.queue)
            cur = self.transition.get(), self.transition.queue[0]
            nxt = self.transition.get(), self.transition.get()

            # print(cur, "\n", nxt)
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

    def generate_sentence(self, num_words=9):
        sentence = ""
        start = "I", "went"
        # print("\n--start_word-- \t", start)
        sentence += "{} {}".format(start[0].capitalize(), start[1])
        word_pair = start

        for _ in range(1, num_words):
            word_pair = self.get_random_word(word_pair)
            # print("\n--next_word-- \t", word)
            sentence += " " + word_pair[1]

        punctuation = [".", "!", "?", "..."]
        sentence += choice(punctuation)
        return sentence

if __name__ == "__main__":
        #The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 2:
        # print("Try again with 1 argument: the number of words to give!")
        num_words = 10
    else:
        #All parameters except the number of words will be hard-coded.
        num_words = int(sys.argv[1])

    # word_list = get_clean_words("text_files/markov.txt")
    word_list = get_clean_words("text_files/second_markov.txt")
    # word_list = get_clean_words("text_files/fish.txt")
    print("\t--word_list--\n", word_list)

    markov = Nth_Order_Markov(word_list, nth_order=2)
    # print("\n\t--Nth_order_markov--2ND--\n", markov.chain)
    # print("\n")
    sentence = markov.generate_sentence(num_words=num_words)
    print("\n\t--Random Sentence length {}--\n".format(num_words), sentence)
