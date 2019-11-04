import sys
import random

def get_clean_words(file_name):
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: words(list)
    """
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
                char == ")"
            )])
            clean_words.append(clean_word)
        # make a list of whole words only containing letters
        clean_words_as_str = []
        for list_of_chars in clean_words:
            whole_word = ""
            clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str

def get_random_word(num):
    words_list = get_clean_words("/usr/share/dict/words")
    word = words_list[random.randint(0, len(words_list)-1)]
    return word

def make_sentence():
    sentence = ""
    for i in range(0, num):
        word = get_random_word(num)
        #print(i+1, word)
        if i == 0:
            sentence = word.capitalize()
        elif i != num - 1:
            sentence += " " + word
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            sentence += random.choice(punctuation)

    #output your sentence
    #print(sentence + "\t: " + str(num) + " words")

if __name__ == "__main__":
    #The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 2:
        print("Try again with 1 argument: he number of words to give!")
    else:
        #All parameters except the number of words will be hard-coded.
        num = int(sys.argv[1])
        #put the number of words requested together into a "sentence"
        make_sentence()