import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for
#imports
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/account')
def account():
    return render_template("account.html")

# Route for handling the login page logic https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)




app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)