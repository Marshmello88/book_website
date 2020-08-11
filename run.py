import os
import json
from flask import Flask, render_template, request, flash, session, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__) 
app.config["MONGO_DBNAME"] = 'plantstoreDB'
app.config["MONGO_URI"] = 'mongodb+srv://marshmello88:Thecharlie88@plantcluster.nhl30.mongodb.net/plantstoreDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
     return render_template("login.html")

    if request.method == 'POST':
      users = mongo.db.users
      try:
        login_user = users.find_one({'name' : request.form['username']})
        print(login_user, "++++++++++++++++++")
        user_id = str(login_user["_id"])
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
          session['username'] = request.form['username']
          #session["user_id"] = login_user[user_id]
          print(session, "+++++++++++session")
          flash('You were successfully logged in', 'message') 
          return redirect(url_for('index'))
        else:
          flash('Invalid password provided', 'error')
          return render_template("login.html")
      except:
          flash('Not a known user', 'error')
          return render_template("login.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
      if request.form['password'] != request.form['cpassword']:
        flash('Passwords are not the same', 'error') 
        render_template('register.html')

      else:
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']}) # search within collection users whether there is no double
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt() ) #not storing plaintext but storing hash version of it so more secure
            users.insert({'name' : request.form['username'], 'password' : hashpass}) #insert everything to users collection
            flash("You're account has been registered", 'message')
            return redirect(url_for('login'))
        else: 
          flash('That username already exists', 'error') 

    return render_template('register.html')



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/account')
def account():
    return render_template("account.html")


@app.route('/plantcare')
def plantcare():
    return render_template("plantcare.html")



@app.route('/shop')
def shop():
    #check the users cart + templating
    catalogue = mongo.db.catalogue.find({})
    return render_template("shop.html", all_products=catalogue)
    
    

# shopping cart
@app.route("/cart", methods=['GET'])
def shopping_cart():
    all_products = []
    user = session["username"]
    user_cart = mongo.db.cart.find({"action": user}) #db.collection.find(query, projection) Former specifies selection filter, latter. Former specifies the fields to return in the documents that match the query filter. 
    print(user_cart, "++++++++++++all user's cart")
    for product in user_cart:
        print(product, "++++++++++++++++++++")
        print(ObjectId(oid=str(product["product_id"])))
        cart_product = mongo.db.catalogue.find({"_id": ObjectId(oid=str(product["product_id"]))})
        all_products.append(cart_product)
    print(all_products, "+++++all products in cart")
# check if the user is in session 
# get the users cart
# pass it to render template

    return render_template("cart.html", products=all_products)

   
 
@app.route('/add_cart', methods=['POST'])
def add_cart():
    #insert into cart collection + redirect to /cart
    #fetch user_id from session
    #to fetch items of the cart collection use mongodb '.find({user_id:...})' then loop through each cart item and fetch the product using '.find_one' with the product id.
    print(request.form)
    user = session["username"] #fetch user from session
    print(user, "++++++++++++logged in user")
    cart_request = request.form.to_dict() #to_dict returns a dictionary
    print(cart_request["product_id"])
    cart_request['action'] = user #add to a dictionary by specifying the key and value (['key'] = value )
    print(cart_request, "+++++++++cart")
    cart = mongo.db.cart 
    cart.insert_one(cart_request)
    return redirect(url_for('shop'))
 

# Route for handling the login page logic https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/

if __name__ == '__main__':
    app.secret_key = 'mysecret'

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)