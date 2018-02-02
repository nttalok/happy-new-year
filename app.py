
from flask import Flask
from flask import render_template, url_for

import os
import socket


app = Flask(__name__)

@app.route("/")
def hello():
	return  render_template('index.html', name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
	app.run()
