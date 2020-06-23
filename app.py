#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

@app.route('/test')
def test():
    return ''

if __name__ == "__main__":
    app.run()
