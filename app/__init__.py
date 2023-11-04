from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session
import sqlite3
import os
import datetime
import random
import string
from GPTCall import GPT
import db
import speechrecog as recorder

app = Flask(__name__)
app.secret_key = os.urandom(16)
lang = "Spanish"
gpt = GPT([{"role": "assistant", "content": "You are a coach helping a studnet learn a new language. Converse with "
                                            "them in " + lang + "in 1 sentence long responses. Tell the user when "
                                                                "they say something incorrect"}])

@app.route("/", methods=['GET', 'POST'])  # At the root, we just return the homepage
def index():
    if request.method:
        caller = recorder.LangRecog("en_US")
        text = caller.listen_and_transcribe()

        print(gpt.makeCall(message=text, model="gpt-4"))
        return render_template("speech.html", result=text)
    else:
        return render_template("speech.html")


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
