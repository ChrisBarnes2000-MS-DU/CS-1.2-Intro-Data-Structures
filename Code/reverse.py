"""Understanding/Code segments provied from
https://www.geeksforgeeks.org/reverse-words-given-string-python/
https://github.com/atleastzero/CS-1.2-How-Data-Structures-Work/blob/master/Code/reverse_string.py
"""

#Function to reverse letter of word
def reverse_word(string):
    new_word = ""

    for char_num in range(len(string)):
        new_word += string[len(string) - char_num - 1]

    return new_word

# Function to reverse words of string
def reverse_string(string):
    # split words of string separated by space
    inputWords = string.split(" ")

    # reverse list of words
    # So, inputWords[-1::-1] here we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    inputWords = inputWords[-1::-1]

    # now join words with space
    output = ' '.join(inputWords)

    return output

def tests():
    word = "Reverse"
    print("Before reversing, the word is: ", word)
    word = reverse_word(word)
    print("After reversing, the word is: ", word)
    sentence = "geeks quiz practice code"
    print("Before reversing, the sentence is: ", sentence)
    sentence = reverse_string(sentence)
    print("After reversing, the sentence is: ", sentence)
    numbers = "1 2 3 4 5 6"
    print("Before reversing, the numbers are: ", numbers)
    numbers = reverse_word(numbers)
    print("After reversing, the numbers are: ", numbers)


if __name__ == "__main__":
    tests()
