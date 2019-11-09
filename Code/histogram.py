import random
from clean import get_clean_words

class Histogram():

    def prob_count(self, histogram):
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

if __name__ == "__main__":
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
