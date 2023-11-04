from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session
import sqlite3
import os
import datetime
import random
import string
import GPTCall as gpt
import db
import speechrecog as recorder

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/", methods=['GET', 'POST'])  # At the root, we just return the homepage
def index():
    if request.method == 'POST':
        caller = recorder.LangRecog()
        text = caller.listen_and_transcribe()
        return render_template("speech.html", result = text, name=session['name'])
    else:
        return render_template("speech.html")


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()