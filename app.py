#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

@app.route('/x')
def x():
    return flask.render_template("x.html")

@app.route('/test')
def test():
    return ''

@app.route('/bootstrap_test.html')
def bootstrap_test():
    return flask.render_template("bootstrap_test.html")

@app.route('/cover.html')
def cover():
    return flask.render_template("cover.html")

@app.route('/hello_world.html')
def hello_world():
    return flask.render_template("hello_world.html")

if __name__ == "__main__":
    app.run()
