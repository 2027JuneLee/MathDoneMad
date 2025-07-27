from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def index():
    is_login = False
    if 'username' in session:
        is_login = True
    return render_template('index.html', is_login=is_login)

@app.route('/ap')
def ap():
    return render_template('ap.html')

@app.route('/sat')
def sat():
    return render_template('sat.html')

@app.route('/playground')
def playground():
    return render_template('index2.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        graduation = request.form["graduation"]

        conn = sqlite3.connect('static/database.db')
        cursor = conn.cursor()

        command = "SELECT * FROM Users WHERE username = ?;"
        cursor.execute(command, (username, ))
        result = cursor.fetchone() # (testest,123,adf@gmail.com.)
        if result is None:
            command = "INSERT INTO Users (username, password,graduation) VALUES (?,?,?)"
            cursor.execute(command, (username,password,graduation,))
            conn.commit()
            conn.close()
        else: # when user fail to register
            flash('username already exists!')
            return render_template('signup.html')


        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=1867)
