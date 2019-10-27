import dictionary_words
import random

#histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
#sentence = "one fish two fish red fish blue fish"
histogram = {}

#all_lines = dictionary_words.get_file_line("sherlock_homes.txt")
all_lines = dictionary_words.get_file_line("Zombie.txt")

for index in range(0, len(all_lines)):
    sentence = all_lines[index]
    for i in sentence.split():
        histogram[i] = histogram.get(i, 0) + 1

        most_value = max(histogram, key=histogram.get)
    #print ("{} : {}".format(most_value, histogram[most_value]))
print(histogram)

#print(all_lines[random.randint(0, len(all_lines)-1)])
