import sys
import random

def get_file_line(filename):
    #open the given file to read
    file = open(filename, 'r')
    #pull out all lines as written in the file
    all_lines = file.readlines()
    #clean up the list of words obtained
    all_lines = [line.strip() for line in all_lines]
    #Close the file to save space/run time
    file.close()
    #return cleaned up list 
    return all_lines

def get_random_word(num):
    words_list = get_file_line("/usr/share/dict/words")
    word = words_list[random.randint(0, len(words_list)-1)]
    return word

def make_sentence():
    sentence = ""
    for i in range(0, num):
        word = get_random_word(num)
        print(i+1, word)
        if i == 0:
            sentence = word.capitalize()
        elif i != num - 1:
            sentence += " " + word
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            sentence += random.choice(punctuation)

    #output your sentence
    print(sentence + "\t: " + str(num) + " words")

if __name__ == "__main__":
    #The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 2:
        print("Try again with 1 argument: he number of words to give!")
    else:
        #All parameters except the number of words will be hard-coded.
        num = int(sys.argv[1])
        #put the number of words requested together into a "sentence"
        make_sentence()
