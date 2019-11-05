from flask import Flask, render_template
import histogram
# import os

app = Flask(__name__)

histogram = histogram.Histogram()
histogram_list = histogram.dictionary_histogram("fish.txt")


@app.route('/')
def index():
    word = histogram.get_word_by_freq(histogram_list)
    sentence = histogram.make_sentence(histogram_list, 10)
    return render_template('index.html', word=word, histogram=histogram_list,
                           sentence=sentence)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
