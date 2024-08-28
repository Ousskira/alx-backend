#!/usr/bin/env python3
"""
A basic Flask application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route to display the welcome message.
    Returns the rendered index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
