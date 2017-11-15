# Author: Matthew Bowden bowdenm@spu.edu

import flask as fsk

app = fsk.Flask(__name__)


@app.route('/')
def show_songs():
    return 'List of songs'
