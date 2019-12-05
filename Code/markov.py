# help provided by aucoeur @ https://github.com/aucoeur/CS-1.2-Intro-Data-Structures/blob/master/Code/markov_chain.py

from utils import time_it, get_clean_words
from random import choice, randint
import dictogram
import hashtable
import queue
import sys

class First_Order_Markov():
    def __init__(self):
        '''Creates word pairs and puts them into a markov dictionary'''
        self.pairs = []
        self.markov_dict = {}

    def markov(self, corpus):
        # create linked pairs
        for i in range(len(corpus)-1):
            self.pairs.append((corpus[i], corpus[i+1]))
        # sort through connections and make a dictionary of routes
        for first, second in self.pairs:
            if first in self.markov_dict.keys():
                self.markov_dict[first].append(second)
            else:
                self.markov_dict[first] = [second]
        return self.markov_dict

    def get_random_word(self, markov, start_word):
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

    def generate_sentence(self, num_words, markov, word_list):
        sentence = ""

        start_word = choice([word for word in word_list if word != word_list[-1]])
        # print("\n--start_word-- \t", start_word)
        sentence += start_word.capitalize()
        word = start_word

        for _ in range(1, num_words):
            word = self.get_random_word(markov, word)
            # print("\n--next_word-- \t", word)
            sentence += " " + word

        punctuation = [".", "!", "?", "...", "!?"]
        sentence += choice(punctuation)
        return sentence

class Nth_Order_Markov():
    def __init__(self):
        self.markov_hash = hashtable.HashTable()
        self.transition = queue.Queue(maxsize=2)

    def markov(self, corpus):
        # create linked pairs
        for i in range(len(corpus)-1):
            #if empty add first two then jump to add to hashtable
            if self.transition.empty():
                # print("adding {} to tansition".format(corpus[i]))
                self.transition.put(corpus[i])
                # print("adding {} to tansition".format(corpus[i+1]))
                self.transition.put(corpus[i+1])
                print(self.transition.queue)
            #Transition not empty so update it 
            else:
                self.transition.get()
                # remove = self.transition.get()
                # print("removing {} to tansition".format(remove))
                # print("adding {} to tansition".format(corpus[i+1]))
                self.transition.put(corpus[i+1])
                # self.transition.put(corpus[i])
                print(self.transition.queue)

            #Sort through Transitions and make a HASHTABLE of routes
            #Add the current set of transitions to the hash table
            key = (self.transition.queue[0], self.transition.queue[1])
            # key = self.transition.queue[0]
            if self.markov_hash.contains(key):
                self.markov_hash.set(key, self.markov_hash.get(key)+1)
            else:
                self.markov_hash.set(key, 1)

        # for first, second in self.pairs:
        #     if first in self.markov_dict.keys():
        #         self.markov_dict[first].append(second)
        #     else:
        #         self.markov_dict[first] = [second]

        return self.markov_hash


if __name__ == "__main__":
    #The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 2:
        # print("Try again with 1 argument: the number of words to give!")
        num_words = 10
    else:
        #All parameters except the number of words will be hard-coded.
        num_words = int(sys.argv[1])

    #Used for any of the Markovs
    # word_list = get_clean_words("text_files/markov.txt")
    word_list = get_clean_words("text_files/second_markov.txt")
    print("\t--word_list--\n", word_list)

    implement_first_order_markov = False
    if implement_first_order_markov:
        first_markov_class = First_Order_Markov()

        markov = first_markov_class.markov(word_list)
        print("\t--markov--\n", markov)

        # sentence = first_markov_class.generate_sentence(num_words, markov, word_list)
        # print("\nFinal Sentence of length {} is\n{}".format(num_words, sentence))

    implement_Nth_order_markov = True
    if implement_Nth_order_markov:
        markov_class = Nth_Order_Markov()

        markov = markov_class.markov(word_list)
        print("\n\t--markov--\n", markov)

        # sentence = markov_class.generate_sentence(num_words, markov, word_list)
        # print("\nFinal Sentence of length {} is\n{}".format(num_words, sentence))
