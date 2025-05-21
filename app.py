import csv
from flask import Flask, render_template
import os

app = Flask(__name__)

def load_words():
    words = []
    path = os.path.join('data', 'words.csv')
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            words.append(row)
    return words

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/words')
def words():
    word_list = load_words()
    return render_template('words.html', words=word_list)

if __name__ == '__main__':
    app.run(debug=True)
