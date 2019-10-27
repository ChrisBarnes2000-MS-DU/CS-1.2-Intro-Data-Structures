#import dictionary_words
from collections import Counter
import rearrange
import random
import sys

def anagram(params):
    for val in range(len(params) - 1, 0, -1):
        j = random.randint(0, val + 1)
        params[val], params[j] = params[j], params[val]
    return params

# Check if two strings are anagrams
def check_anagram(input1, input2):
    return Counter(input1) == Counter(input2)

def terminal_input():
    if len(sys.argv) != 2:
        print("Try again with 1 argument: he number of words to give!")
    else:
        word = sys.argv[1]
        # turns the word string into a list stored in the variable name letter_list
        letter_list = list(word)
        print(word)
        ang_word = ''.join(anagram(letter_list))
        print(ang_word)
        if check_anagram(word, ang_word):
            print("These are anagrams!!")
        else:
            print("They are not anagrams :(")

if __name__ == "__main__":
    terminal_input()
