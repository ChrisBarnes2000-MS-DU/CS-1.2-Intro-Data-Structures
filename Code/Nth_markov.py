
from utils import time_it, get_clean_words
from dictogram import Dictogram
import hashtable
import queue

class Nth_Order_Markov():
    def __init__(self, words_list=None):
        """Construct a Markov Chain model.
           Param: words_list(list of str)"""
        self.corpus = words_list
        self.chain = self.populate_chain()

    def populate_chain(self):
        self.chain = Dictogram()
        for i in range(len(self.corpus)-3):
            cur = self.corpus[i], self.corpus[i+1]
            nxt = self.corpus[i+1], self.corpus[i+2]
            if self.chain.get(cur, None) is None:
                self.chain[cur] = Dictogram([nxt])
            else:
                self.chain[cur].add_count(nxt)
        return self.chain



if __name__ == "__main__":
    word_list = get_clean_words("text_files/second_markov.txt")
    print("\t--word_list--\n", word_list)

    markov = Nth_Order_Markov(word_list)
    print("\n\t--second/Nth_order_markov--Populated--\n", markov.chain)



""" Working Model for 2nd Gen

    def populate_chain(self):
        self.chain = Dictogram()
        for i in range(len(self.corpus)-3):
            cur = self.corpus[i], self.corpus[i+1]
            nxt = self.corpus[i+1], self.corpus[i+2]
            if self.chain.get(cur, None) is None:
                self.chain[cur] = Dictogram([nxt])
            else:
                self.chain[cur].add_count(nxt)
        return self.chain
"""
