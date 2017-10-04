from flask import Flask
from flask import jsonify
from operator import itemgetter
import pandas as pd
import spacy

codes = pd.read_csv('acra_codes.csv')
app = Flask(__name__)

nlp = spacy.load('en')

@app.route('/<string:term>')
def hello_world(term, codes=codes):
    distances = []

    for index, row in codes.iterrows():
        entry = {}
        entry['code'] = row.code
        entry['title'] = row.title
        entry['similarity'] = nlp(row.title).similarity(nlp(term))
        distances.append(entry)

    sorted_distances = sorted(distances, key=itemgetter('similarity'), reverse=True)
    return jsonify(sorted_distances[0:19])
