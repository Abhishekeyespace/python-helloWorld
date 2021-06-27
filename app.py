from flask import Flask
import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"