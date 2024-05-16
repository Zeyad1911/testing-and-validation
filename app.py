from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)


DATABASE_PATH = 'user_db.db'


class db:
    def connectdb():
        conn = sqlite3.connect(DATABASE_PATH)
        return conn


@app.route('/')
def root():
    return redirect("/register")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

        connection = db.connectdb()
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT UNIQUE NOT NULL,
                   name TEXT,
                   password_hash TEXT NOT NULL
               );''')

        cursor.execute(""" INSERT INTO user (email, name, password_hash)
                   VALUES (?,?,?)""", (name, email, password))

        connection.commit()

        
        return render_template('/passed_reg.html')
        return redirect('/passed_reg.html')  


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
