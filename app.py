#!/usr/bin/python
import os

import mysql.connector
from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_session import Session
# from tempfile import mkdtemp
# # from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# # from werkzeug.security import check_password_hash, generate_password_hash

from helper import login_required, nospace


# DATABASE
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "KingOfBeasts",
    database = "ncserver",
)
my_cursor = mydb.cursor()

app = Flask(__name__)


# Secret Key For Session
app.secret_key = os.urandom(16)


# Index page (Home Page)
@app.route("/")
def index():
    return render_template("index.html")


# Register
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        # Get the register Code
        sql_register_code = "SELECT registercode FROM register"
        my_cursor.execute(sql_register_code)

        register_code = my_cursor.fetchall()[0][0]

        # MySQL code (DATABASE)
        sql = "SELECT * FROM users WHERE username = %s"
        username = (request.form.get("username"), )

        # Execute MySQL code (DATABASE)
        my_cursor.execute(sql, username)
        rows = my_cursor.fetchall()

        # Check user input exsit
        if rows:
            return 'Username already taken'

        # check username and password field is not empty
        elif not request.form.get('username') or not request.form.get('password') or not request.form.get('register-code'):
            return "Please provide information"

        # Username length check
        elif len(request.form.get('username')) < 7:
                return "Username must be more than 7 characters"
            # Password length check
        elif len(request.form.get('password')) < 10:
                return "Please enter a strong password"

        # check the password and confirm password is similar
        elif request.form.get('password') != request.form.get('confirm-password'):
            return "Password is not matched"

        # check register code matches
        elif request.form.get('register-code') == register_code:
                return "Code is already registered or invalid code"

        # DATABASE insert user register details
        username_input = nospace(request.form.get('username'))
        password_input = generate_password_hash(request.form.get('password'))
        insert = "INSERT INTO users (username, password, useradmin) VALUES (%s, %s, %s)"
        insertSQL = (username_input, password_input, "admin")

        my_cursor.execute(insert, insertSQL)
        mydb.commit()

        message = True
        return redirect('/login', message=message)


# Login
@app.route("/login", methods=['POST', 'GET'])
def login():

    # Clear all session
    session.clear()

    # Check if its submitted via post
    if request.method == 'POST':

        # Authantication checks
        if not request.form.get('username_log') and not request.form.get('password_log'):
            return "Invalid username or password"

        # MySQL code (DATABASE)
        sql = "SELECT * FROM users WHERE useradmin = %s"
        useradmin = (request.form.get("user"), )
        # Execute MySQL code (DATABASE)
        my_cursor.execute(sql, useradmin)
        rows = my_cursor.fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0][2], request.form.get("password_log")):
            return "invalid username and/or password"

        # Remember which user has logged in
        session["user_id"] = rows[0][0]

        # Check username
        # MySQL code (DATABASE)
        sqluseradmin = "SELECT useradmin FROM users WHERE userID = %s"
        ID = (session['user_id'], )
        # Execute MySQL code (DATABASE)
        my_cursor.execute(sqluseradmin, ID)
        admin = my_cursor.fetchall()

        # if useradmin is admin redirct to admin page else redirect to management page
        if admin[0][0] == 'admin':
            return redirect('/home')
        else:
            return redirect('/manage_home')
    else:
        return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    # Forget the session
    session.clear()
    # Redirect from current page
    return redirect("login")


@app.route("/home", methods=['POST', 'GET'])
@login_required
def home():
    # Check if user input via post
    if request.method == 'POST':
        # MySQL code (DATABASE)
        sql = "SELECT * FROM users WHERE useradmin = %s"
        useradmin = (request.form.get("user"), )
        # Execute MySQL code (DATABASE)
        my_cursor.execute(sql, useradmin)
        rows = my_cursor.fetchall()

        # Check user input exsit
        if rows:
            # update the users table if useradmin has already exist
            password_input = generate_password_hash(request.form.get('management'))
            updaterows = "UPDATE users SET password = %s WHERE useradmin = manage"
            # Execute MySQL code (DATABASE)
            my_cursor.execute(updaterows, password_input)
            mydb.commit()

            return jsonify('True')
        else:
            # Get the admin username
            # MySQL code (DATABASE)
            sql = "SELECT username FROM users WHERE userID = %s"
            userID = (session['user_id'], )
            # Execute MySQL code (DATABASE)
            my_cursor.execute(sql, userID)
            username = my_cursor.fetchall()

            # Insert into users table
            password_input = generate_password_hash(request.form.get('management'))
            insert = "INSERT INTO users (username, password, useradmin) VALUES (%s, %s, %s)"
            insertSQL = (username[0][0], password_input, "manage")
            # Execute MySQL code (DATABASE)
            my_cursor.execute(insert, insertSQL)
            mydb.commit()

            return jsonify('True')
    else:
        return render_template("home.html")


@app.route('/manage_home', methods=['POST', 'GET'])
@login_required
def manage_home():
    return render_template("manage_home.html")


if __name__ == "__main__":
    app.run(debug=True)
