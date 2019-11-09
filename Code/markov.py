import dictogram
from clean import get_clean_words
import random
import sys

def generate_sentence(histogram, num_words):
    sentence = ""
    for i in range(0, num_words):
        word = histogram.sample()
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
    word_list = get_clean_words("text_files/markov.txt")
    histogram = dictogram.Dictogram(word_list)
    num_words = sys.argv[1]
    print(generate_sentence(histogram, int(num_words)))
