import sqlite3

def get_db():
    DB_FILE = "speakeasy.db"
    db = sqlite3.connect(DB_FILE, check_same_thread = False)
    return db
    
def get_connection(db):
    conn = sqlite3.connect(db)
    return conn

def createTables(db):
    c = db.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS conversations(email TEXT, id INTEGER, dialogue TEXT, grade INTEGER, datetime TEXT, language TEXT, level TEXT, topic TEXT)""")
    
def fetchUserConversations(db, email):
    c = db.cursor()
    c.execute("""SELECT * FROM conversations WHERE email = ?""", (email,))
    
    conversations = c.fetchall()
    
    return conversations

def fetchConversationById(db, id):
    c = db.cursor()
    
    c.execute("""SELECT * FROM conversations WHERE id = ?""", (id,))
    conversation = c.fetchone()
    
    return conversation

def addConversation(db, email, id, dialogue, grade, datetime, language, level, topic):
    c = db.cursor()
    
    dialogue = convertListToString(dialogue)
    
    c.execute("""INSERT INTO conversations VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (email, id, dialogue, grade, datetime, language, level, topic))
    db.commit()

def convertListToString(conversation):
    
    dialogue = ""
    
    for line in conversation:
        dialogue += line + "~"
    
    return dialogue

def convertStringToList(dialogue):
    
    conversation = dialogue.split("~")
    
    return conversation

# DB_FILE = "P4.db"
# db_name = "P4.db"
# db = sqlite3.connect(DB_FILE, check_same_thread = False)
# c = db.cursor()


# create tables for users if the table is empty
