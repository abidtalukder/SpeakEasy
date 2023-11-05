from flask import Flask, render_template
from db import get_db, fetchUserConversations

app = Flask(__name__)

@app.route('/')
def index():
    db = get_db()
    email = 'abidtalukder12@email.com'
    conversations = fetchUserConversations(db, email)
    return render_template('History.html', conversations=conversations)

if __name__ == '__main__':
    app.run(debug=True)
