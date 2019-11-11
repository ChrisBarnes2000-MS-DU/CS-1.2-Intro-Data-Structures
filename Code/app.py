from flask import Flask, render_template, request
from markov import markov, generate_sentence
from clean import get_clean_words
import histogram
import os

app = Flask(__name__)

histogram = histogram.Histogram()
histogram_list = histogram.dictionary_histogram("text_files/markov.txt")
word_list = get_clean_words("text_files/markov.txt")
markov_dict = markov(word_list)

@app.route('/')
def index():
    num_words = request.args.get("num_words", default=10, type=int)
    word = histogram.get_word_by_freq(histogram_list)
    histogram_sentence = histogram.make_sentence(histogram_list, num_words)
    
    markov_sentence = generate_sentence(num_words, markov_dict, word_list)
    
    return render_template('index.html', word_list=word_list, markov=markov_dict, markov_sentence=markov_sentence, word=word, histogram=histogram_list,histogram_sentence=histogram_sentence, num_words=num_words)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
