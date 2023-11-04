from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session
import sqlite3
import os
import datetime
import random
import string

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/", methods=['GET', 'POST'])  # At the root, we just return the homepage
def index():
    return render_template("index.html")


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()