import os
import json
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__) 
app.config["MONGO_DBNAME"] = 'plantstoreDB'
app.config["MONGO_URI"] = 'mongodb+srv://marshmello88:Thecharlie88@plantcluster.nhl30.mongodb.net/plantstoreDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']}) # search within collection users whether there is no double
 # looking for a name where a name is same as the username from our form
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt()) #not storing plaintext but storing hash version of it so more secure
            users.insert({'name' : request.form['username'], 'password' : hashpass}) #insert everything to users collection
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


#@app.route('/register')
#def register():
 #   return render_template("register.html")

@app.route('/account')
def account():
    return render_template("account.html")


@app.route('/plantcare')
def plantcare():
    return render_template("plantcare.html")


@app.route('/shop')
def shop():
    return render_template("shop.html")
    

# Route for handling the login page logic https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
#@app.route('/login', methods=['GET', 'POST'])
#def login():
 #   error = None
   # if request.method == 'POST':
    #    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
     #       error = 'Invalid Credentials. Please try again.'
      #  else:
       #     return redirect(url_for('home'))
    #return render_template('account.html', error=error)


#@app.route("/register", methods = ['GET', 'POST'])
#def register():
  #  if request.method == 'POST':   
   #     password = request.form['password']
    #    email = request.form['email']
#
 #       user_id =  plantCluster.insert({
  #          'email' : email,
   #         'password' : password,
    #    })
#new_user = plantCluster.find_one({'_id' : user_id})

#result = {'email' : new_user['email'] + 'registered'}

#return jsonify ({'result' : result})

if __name__ == '__main__':
    app.secret_key = 'mysecret'

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)