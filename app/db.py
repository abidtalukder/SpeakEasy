import sqlite3
import random
import datetime

def generateRandomNumber():
    return random.randint(0, 1000000)

def get_db():
    DB_FILE = "speakeasy.db"
    db = sqlite3.connect(DB_FILE, check_same_thread = False)
    return db
    
def get_connection(db):
    conn = sqlite3.connect(db)
    return conn

def createTables(db):
    c = db.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS conversations(email TEXT, id INTEGER, dialogue TEXT, grade INTEGER, datetime TEXT, language TEXT, level INTEGER, topic TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS vocabulary(language TEXT, topic TEXT, url TEXT)""")
    populateVocabularyTable(db)
    fetchAllVocabulary()
    
def read_file_and_parse(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by the specified delimiter '~'
            line.replace('\n', '')
            data = line.split('*')
            if data[0] == ['\n']:
                continue
            for (line) in data:
                line.replace('\n', '')
            
            # Append the split data as a list to the result list
            result.append(data)

    return result

def createVocabularyEntry(db, lang, topic, url):
    c = db.cursor()
    
    c.execute("""INSERT INTO vocabulary VALUES (?, ?, ?)""", (lang, topic, url))
    db.commit()
    
def populateVocabularyTable(db):
    c = db.cursor()
    
    c.execute("""SELECT * FROM vocabulary""")
    result = c.fetchall()
    
    if (len(result) < 60):
        vocabulary = read_file_and_parse("LinkData.txt")
        
        for line in vocabulary:
            #print(line)
            createVocabularyEntry(db, line[0], line[1], line[2])

def searchVocabulary(db, lang, topic):
    c = db.cursor()
    
    c.execute("""SELECT * FROM vocabulary WHERE language = ? AND topic = ?""", (lang, topic))
    result = c.fetchall()
    
    return result

def fetchAllVocabulary():
    db = get_db()
    c = db.cursor()
    c.execute("""SELECT * FROM vocabulary""")
    result = c.fetchall()
    print(result)
    

def fetchUserConversations(db, email):
    c = db.cursor()
    c.execute("""SELECT * FROM conversations WHERE email = ?""", (email,))
    
    conversations = c.fetchall()
    
    return conversations

def fetchConversationById(db, id):
    c = db.cursor()
    
    c.execute("""SELECT * FROM conversations WHERE id = ?""", (id,))
    conversation = c.fetchall()
    
    return conversation

def validId(db, id):
    conversation = fetchConversationById(db, id)
    
    if (conversation == None):
        return True
    else:
        return False

def addConversation(db, email, dialogue, grade, language, level, topic):
    c = db.cursor()
    #dialogue = convertListToString(dialogue)
    
    date = datetime.datetime.now()
    
    id = generateRandomNumber()
    while (validId(db, id)==True):
        id = generateRandomNumber()
        
    
    c.execute("""INSERT INTO conversations VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (email, id, dialogue, grade, date, language, level, topic))
    db.commit()

def convertListToString(conversation):
    
    dialogue = ""
    
    for line in conversation:
        dialogue += line + "~"
    
    return dialogue

def convertStringToList(dialogue):
    
    conversation = dialogue.split("~")
    
    return conversation

db = get_db()
createTables(db)
#fetchAllVocabulary()

# addConversation(db, "abidtalukder12@gmail.com", ["Hello", "How are you?"],80, "English", 1, "Greetings")

# print(fetchUserConversations(db, "abidtalukder12@gmail.com"))


# DB_FILE = "P4.db"
# db_name = "P4.db"
# db = sqlite3.connect(DB_FILE, check_same_thread = False)
# c = db.cursor()


# create tables for users if the table is empty
