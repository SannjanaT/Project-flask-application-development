import re
import sqlite3
from flask import Flask, jsonify, json
from flask import render_template
from flask import request
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app = Flask(__name__, template_folder='Templates')

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email_address = request.form.get('email_address')
        password = request.form.get('password')

        # Insert form data into database
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO users (first_name, last_name, email_address, password) VALUES (?, ?, ?, ?)",
                      (first_name, last_name, email_address, password))
            conn.commit()

        # Redirect to thank-you page
        return render_template('thank_you.html')

    # If request method is not POST, render form template
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT distinct * FROM users WHERE email_address = ? AND password = ?', (email_address, password))
        user = c.fetchone()
        conn.close()
        if user:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')
