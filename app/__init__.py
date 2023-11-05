import pathlib
from flask import Flask, abort  # facilitate flask webserving
from flask import render_template, redirect  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session
import os
import datetime
import random
import string
import speechrecog as recorder
from GPTCall import GPT
import db

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
#import speechrecog as recorder

app = Flask(__name__)

app.secret_key = "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"


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = "116824999490-2v8691iltgn318dsmeugp7gbhi21s4ha.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost/callback"
)

caller = recorder.LangRecog("en_US")
lang = "English"
gpt = GPT([{"role": "assistant", "content": "You are a coach helping a student learn a new language. Converse with "
                                            "them in " + lang + " in 1 sentence long responses. Tell the user when "
                                                                "they say something incorrect and also tell them to "
                                                                "only speak in " + lang + " when they say somthing in "
                                                                                          "a different language"}])

gpt2 = GPT([{"role": "assistant", "content": "Every time we input a sentence, you have to give me a 1 word topic for "
                                             "the whole conversation that it falls under."}])


# def login_is_required(function):
#     def wrapper(*args, **kwargs):
#         if "google_id" not in session:
#             return abort(401)  # Authorization required
#         else:
#             return function()

#     return wrapper

# @app.route("/conversations", methods=['GET', 'POST'])
# def addConversation():
#     if request.method == 'POST':
#         email = session["google_id"]
#         dialogue = request.form.get("dialogue")
#         grade = request.form.get("grade")
#         language = request.form.get("language")
#         level = request.form.get("level")
#         topic = request.form.get("topic")
        
#         db.addConversation(db.get_db(), email, dialogue, grade, language, level, topic)
        
#         return redirect("/conversations")
#     else:
#         return render_template("addConversation.html")

@app.route("/userResponse", methods=['GET', 'POST'])
def userResponse():
    speech, time = caller.listen_and_transcribe()
    
    if (speech == ""):
        return "None"
    
    #gpt.makeCall("gpt-4", speech)
    #gpt2.makeCall("gpt-4", speech)
    return speech

@app.route("/gptResponse", methods=['GET', 'POST'])
def gptResponse():
    if request.method == 'POST':
        speech = request.form.get("speech")
        #print(speech + " GPT RESPONSE")
        
        text = gpt.makeCall("gpt-4", speech)
        
        return text
    else:
        return "Internal Server Error"
        
    

@app.route("/", methods=['GET', 'POST'])  # At the root, we just return the homepage
def index():
    # return render_template("index.html")
    return redirect("/speech")

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback2", methods=['GET', 'POST'])
def callback2():
    
    session['name'] = "Abid Talukder"
    session["google_id"] = "abidtalukder12@gmail.com"
    
    return render_template("speech.html", name=session['name'])

@app.route("/speech", methods=['GET', 'POST'])
def speech():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return render_template("chat2.html")
    else:
        return render_template("chat2.html")
    
    
@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/")


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['name'] = request.form['name']
#         return render_template("speech.html", name=session['name'])
#     else:
#         return render_template("login.html")
    
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/")



if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
