import histogram
from flask import Flask

app = Flask(__name__)

histogram = histogram.Histogram()
histogram_list = histogram.dictionary_histogram("fish.txt")

@app.route('/')
def index():
    word = histogram.get_word_by_freq(histogram_list)
    return word # histogram_list
    #print("**__ORIGINAL_HISTOGRAM__**\n", histogram)
