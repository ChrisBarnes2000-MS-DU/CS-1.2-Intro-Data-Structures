import random

def save_to_file(histogram_as_dict, filename):
    with open(filename, 'w+') as f:
        for key, value in histogram_as_dict.items():
            f.write("{}\t{}\n".format(key, value))

def get_clean_words(file_name):
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: words(list) """
    words = []
    with open(file_name, "r") as file:
        # make a list ofd words, contains non alphabetic chars
        words = file.read().split()
        # remove all occurrences of non-alpha chars from data
        clean_words = []
        for word in words:
            clean_word = ([char for char in word if not (
                char == "." or
                char == "?" or
                char == "!" or
                char == "," or
                char == ":" or
                char == ";" or
                char == "(" or
                char == ")" or
                char == "\""  # or
                #char == "'" or
                #char == "-"
            )])
            clean_words.append(clean_word)
        # make a list of whole words only containing letters
        clean_words_as_str = []
        for list_of_chars in clean_words:
            whole_word = ""
            clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str

def prob_count(histogram):
    probs = {}
    total_words = sum(histogram.values())
    for key, value in histogram.items():
        probability = int(value)/total_words
        probs[key] = probs.get(key, probability)
    return probs

def dictionary_histogram(filename):
    histogram = {}

    all_lines = get_clean_words(filename)
    #print("Seperated Input From Provided File: \t\n", all_lines, "\n")
    for index in range(0, len(all_lines)):
        sentence = all_lines[index]
        for i in sentence.split():
            histogram[i] = histogram.get(i, 0) + 1
    return histogram

def get_word_by_freq(histogram):
    #word = random.choice(list(histogram.keys()))
    word_ind = random.random()*10
    while word_ind > sum(histogram.values()):
        word_ind = random.random()*10
    total = 0.0
    for word, count in histogram.items():
        total += count
        #print("Our value is {}, Searching index: {}, thus the word will be {}".format("%.1f" %word_ind, total, word))
        if total >= word_ind:
            return word

def get_word_weighted(histogram, probs):
    word = random.choices(list(histogram.keys()), list(probs.values()))
    return str(word)

if __name__ == "__main__":
    histogram = dictionary_histogram("fish.txt")
    print("**__ORIGINAL_HISTOGRAM__**\n", histogram)
    probabilities = prob_count(histogram)
    print("**__ORIGINAL_PROBABILITIES__**\n", probabilities)

    count = 1
    num_runs = 8
    results = {}
    while(count <= num_runs):
        word = get_word_by_freq(histogram)
        #print(count, word)
        results[word] = results.get(word, 0) + 1
        count += 1
    print("\nRunning Word by Frequency {} times\n".format(num_runs))

    print("**__RESULTS_HISTOGRAM__**\n", results)
    prob_results = prob_count(results)
    print("**__RESULTS_PROBABILITIES__**\n", prob_results)
