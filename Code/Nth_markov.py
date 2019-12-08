
from utils import time_it, get_clean_words
from dictogram import Dictogram
import hashtable
from queue import Queue

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

if __name__ == "__main__":
    word_list = get_clean_words("text_files/second_markov.txt")
    print("\t--word_list--\n", word_list)

    markov = Nth_Order_Markov(word_list, nth_order=2)
    print("\n\t--Nth_order_markov--2ND--\n", markov.chain)

    # markov = Nth_Order_Markov(word_list, nth_order=3)
    # print("\n\t--Nth_order_markov--3rd--\n", markov.chain)
