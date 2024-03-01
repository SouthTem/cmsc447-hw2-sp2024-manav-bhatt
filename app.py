import sqlite3
from flask import Flask, g, render_template, request

DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM STUDENT')    
    return render_template("main.html", rows = cursor.fetchall())

@app.route("/", methods=["POST"])
def values():
    if(request.method == "POST"):
        add = request.form.get("add")
        remove = request.form.get("delete")
        update = request.form.get("update")
        search = request.form.get("search")
        reset = request.form.get("reset")
        name = request.form.get("name")
        id = request.form.get("id")
        points = request.form.get("points")

        if(reset is not None):
            reset_table()
        
        elif(name == "" or id == "" or points == ""):
            return render_template("error.html")

        if(add is not None):
            add_element(name, id, points)
            print("yes")
        elif(update is not None):
            update_table(name, id, points)
            print("yes1")
        elif(remove is not None):
            remove_element(name, id, points)
            print("yes2")
        elif(search is not None):
            value = search_table(name, id, points)
            return value


    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM STUDENT')    
    return render_template("main.html", rows = cursor.fetchall())


def add_element(name, id, points):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO STUDENT (name,ID,points) VALUES (?,?,?)',(name, id, points)
        )   
        db.commit()
    except Exception as e:
        print("ERROR: ", e)
        return render_template("error.html")

    return

def remove_element(name, id, points):
    try:
        print(name, id, points)
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'DELETE FROM STUDENT WHERE ID = ?;',(id,)
        )   
        db.commit()
    except Exception as e:
        print("ERROR: ", e)
        return render_template("error.html")

    return

def update_table(name, id, points):
    try:
        print(name, id, points)
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE STUDENT SET name = ?, points = ? WHERE ID = ?',(name, points, id)
        )   
        db.commit()
        
    except Exception as e:
        print("ERROR: ", e)
        return render_template("error.html")

    return

def search_table(name, id, points):
    try:
        print(name, id, points)
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'SELECT name, ID, points FROM STUDENT WHERE ID == ?',(id,)
        )   

        return render_template("main.html", rows=cursor.fetchall())
    except Exception as e:
        print("ERROR: ", e)
        return render_template("error.html")


def reset_table():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM STUDENT"
        )   
        db.commit()
    except Exception as e:
        print("ERROR: ", e)
        return render_template("error.html")

    return
