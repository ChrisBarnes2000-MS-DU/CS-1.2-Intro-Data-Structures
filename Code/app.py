from flask import Flask, render_template, request
from Nth_markov import Nth_Order_Markov
from markov import First_Order_Markov
from utils import get_clean_words
import histogram
import os

app = Flask(__name__)

SOURCE = "text_files/markov.txt"
word_list = get_clean_words(SOURCE)
num_words = request.args.get("num_words", default=10, type=int)
nth_order = request.args.get("nth_order", default=2, type=int)

# INITIALIZERS
histogram = histogram.Histogram()
markov_1 = First_Order_Markov()
nth_markov = Nth_Order_Markov(word_list, 2)

# CREATE LISTS
histogram_list = histogram.dictionary_histogram(SOURCE)
markov_dict = markov_1.chain(word_list)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('Histogram')
def Histogram():
    word = histogram.get_word_by_freq(histogram_list)
    histogram_sentence = histogram.make_sentence(histogram_list, num_words)
    return render_template('histo.html', word=word, histogram=histogram_list, histogram_sentence=histogram_sentence, num_words=num_words)

@app.route('First_order')
def First_order():
    markov_sentence = markov_1.generate_sentence(num_words, markov_dict, word_list)
    return render_template('First_markov.html', word_list=word_list, markov=markov_dict, markov_sentence=markov_sentence)

@app.route('Nth_order')
def Nth_order():
    markov_sentence = nth_markov.generate_sentence(num_words, nth_order)
    return render_template('Nth_markov.html', word_list=word_list, markov=markov_dict, markov_sentence=markov_sentence)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
