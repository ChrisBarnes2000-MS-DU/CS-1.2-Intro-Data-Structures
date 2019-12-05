import random
import timeit
from clean import get_clean_words

class Histogram():

    def prob_count(self, histogram):
        """TODO: Running time: O(n) loops through number of items in provided histogram"""
        probs = {}
        total_words = sum(histogram.values())
        for key, value in histogram.items():
            probability = int(value)/total_words
            probs[key] = probs.get(key, probability)
        return probs

    def dictionary_histogram(self, filename):
        histogram = {}

        all_lines = get_clean_words(filename)
        # print("Seperated Input From Provided File: \t\n", all_lines, "\n")
        for index in range(0, len(all_lines)):
            sentence = all_lines[index]
            for i in sentence.split():
                histogram[i] = histogram.get(i, 0) + 1
        return histogram

    def list_of_words(self, length):
        dict_words = '/usr/share/dict/words'
        words_str = open(dict_words, 'r').read()
        all_words = words_str.split("\n")
        return all_words[0:length]

    def find(self, item, hgram):
        """TODO: Running time: O(n) loops through number of items in provided histogram"""
        for index, pair in enumerate(hgram):
            if pair[0] == item:
                return index
        return None

    def tuple_histogram(self, words):
        hgram = []                           # create a new list called hgram
        for word in words:                   # for each word in the list of words
            index = self.find(word, hgram)        # check if word is in hgram already
            if index == None:                # if word is not in histogram
                hgram.append((word, 1))      # add a new word-count pair to hgram
            else:                            # if word is already in hgram
                count = hgram[index][1]      # find its current count
                new_pair = (word, count + 1)  # make a new word-count pair
                hgram[index] = new_pair      # replace word-count pair
        return hgram                         # return the hgram

    def count(self, word, hgram):
        """TODO: Running time: O(n) loops through number of items in provided histogram"""
        index = self.find(word, hgram)     # 1. call the find function; 2. assign variable
        if index:                          # 3. evaluate conditional
            word_count_pair = hgram[index] # 4. access list element; 5. assign variable
            return word_count_pair[1]      # 6. access list element
        else:
            return 0

    def get_word_by_freq(self, histogram):
        # word = random.choice(list(histogram.keys()))
        word_ind = random.random()*10
        while word_ind > sum(histogram.values()):
            word_ind = random.random()*10
        total = 0.0
        for word, count in histogram.items():
            total += count
            # print("Our value is {}, Searching index: {}, thus the word will
            #       be {}".format("%.1f" %word_ind, total, word))
            if total >= word_ind:
                return word

    def get_word_weighted(self, histogram, probs):
        word = random.choices(list(histogram.keys()), list(probs.values()))
        return str(word)

    def make_sentence(self, histogram, num_words):
        sentence = ""
        for i in range(0, num_words):
            word = self.get_word_by_freq(histogram)
            # print(i+1, word)
            if i == 0:
                sentence = word.capitalize()
            elif i != num_words - 1:
                sentence += " " + word
            else:
                punctuation = [".", "!", "?", "...", "!?"]
                sentence += random.choice(punctuation)
        # output your sentence
        # print(sentence + "\t: " + str(num_words) + " words")
        return sentence

if __name__ == "__main__":
    implemented_dictionary_histogram = False
    if implemented_dictionary_histogram:
        histogram_class = Histogram()
        histogram = histogram_class.dictionary_histogram("text_files/fish.txt")
        print("**__ORIGINAL_HISTOGRAM__**\n", histogram)
        probabilities = histogram_class.prob_count(histogram)
        print("**__ORIGINAL_PROBABILITIES__**\n", probabilities)

        count = 1
        num_runs = 8
        results = {}
        while(count <= num_runs):
            word = histogram_class.get_word_by_freq(histogram)
            # print(count, word)
            results[word] = results.get(word, 0) + 1
            count += 1
        print("\nRunning Word by Frequency {} times\n".format(num_runs))

        print("**__RESULTS_HISTOGRAM__**\n", results)
        prob_results = histogram_class.prob_count(results)
        print("**__RESULTS_PROBABILITIES__**\n", prob_results)

    implemented_tuple_histogram = False
    if implemented_tuple_histogram:
        histo = Histogram()
        word_list = histo.list_of_words(5)
        # => [('A', 1), ('a', 1), ('aa', 1), ...]
        hgram = histo.tuple_histogram(word_list)
        print("FIND: aal = 3", histo.find('aal', hgram) == 3)      # => True
        print("FIND: zoo = None", histo.find('zoo', hgram) == None)   # => True

        word_list.append('aal')
        word_list.append('a')
        word_list.append('a')
        # => [('A', 1), ('a', 3), ('aa', 1), ...]
        hgram = histo.tuple_histogram(word_list)
        print("COUNT: a = 3", histo.count('a', hgram) == 3)      # => True
        print("COUNT: aal = 2", histo.count('aal', hgram) == 2)    # => True
        print("COUNT: aalii = 1", histo.count('aalii', hgram) == 1)  # => True
        print("COUNT: zoo = 0", histo.count('zoo', hgram) == 0)    # => True

    implemented_benchmarking = False
    if implemented_benchmarking:
        histo = Histogram()
        hundred_words = histo.list_of_words(100)
        # ten_thousand_words = histo.list_of_words(10000)

        hundred_hgram = histo.tuple_histogram(hundred_words)
        # ten_thousand_hgram = histo.tuple_histogram(ten_thousand_words)

        hundred_search = hundred_words[-1]
        # ten_thousand_search = ten_thousand_words[-1]

        stmt = "count('{}', hundred_hgram)".format(hundred_search)
        setup = "from __main__ import hundred_hgram"
        timer = timeit.Timer(stmt, setup=setup)

        iterations = 10000
        result = timer.timeit(number=iterations)
        print("count time for 100-word histogram: " + str(result))
