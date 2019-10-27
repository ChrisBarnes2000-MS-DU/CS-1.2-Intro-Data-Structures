import dictionary_words
import random

def dictionary_histogram(filename):
    #histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    #sentence = "one fish two fish red fish blue fish"
    histogram = {}

    all_lines = dictionary_words.get_file_line(filename)

    for index in range(0, len(all_lines)):
        sentence = all_lines[index]
        for i in sentence.split():
            histogram[i] = histogram.get(i, 0) + 1

            most_value = max(histogram, key=histogram.get)
    print(histogram)
    save_to_file(histogram, filename + "_histogram.txt")
    print ("The word with the highest frequency count is: {} with: {} occurrences".format(most_value, histogram[most_value]))

def find_unique_words(words_list):
    """Record all unique words in a list of strings."""
    # record all unique words
    unique_words = []
    for word in words_list:
        if word.lower() not in unique_words:
            unique_words.append(word.lower())
    return unique_words

def list_histogram(words_list):
    """Return a list of word and the number of appearances
       they make in a list.
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    # count up appearances of each unique word, then make tuple in histogram
    for word in unique_words:
        appearances = 0
        for word_from_text in words_list:
            if word == word_from_text.lower():
                appearances += 1
        histogram.append([word, appearances])
    return histogram

def save_to_file(histogram_as_dict, filename):
    with open(filename, 'w+') as f:
        for key, value in histogram_as_dict.items():
            f.write("{}\t{}\n".format(key, value))

if __name__ == "__main__":
    #dictionary_histogram("sherlock_homes.txt")
    dictionary_histogram("Zombie.txt")

    #sentence = "one fish two fish red fish blue fish"
    #sentence = sentence.split()
    #print(list_histogram(sentence))
