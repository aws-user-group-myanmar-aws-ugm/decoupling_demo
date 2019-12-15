from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import sqlite3

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/frequency_play', methods=['GET'])
@cross_origin()
def collect():
    conn = sqlite3.connect('play_stats.db')
    c = conn.cursor()

    c.execute("SELECT title, count(*) FROM stats WHERE type='PLAY' GROUP BY title")
    response = c.fetchall()
    conn.close()

    data = []

    for song in response:
        data.append({'title': song[0], 'count': song[1]})

    return json.dumps(data)


@app.route('/frequency_finish', methods=['GET'])
@cross_origin()
def frequency_finish():
    conn = sqlite3.connect('play_stats.db')
    c = conn.cursor()

    c.execute("SELECT title, count(*) FROM stats WHERE type='FINISH' GROUP BY title")
    response = c.fetchall()
    conn.close()

    data = []

    for song in response:
        data.append({'title': song[0], 'count': song[1]})

    return json.dumps(data)
