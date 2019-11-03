from flask import Flask, request, render_template
import histogram
import os

app = Flask(__name__)

histogram = histogram.Histogram()
histogram_list = histogram.dictionary_histogram("fish.txt")

@app.route('/')
def index():
    word = histogram.get_word_by_freq(histogram_list)
    return render_template('index.html', word=word, histogram=histogram_list)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
