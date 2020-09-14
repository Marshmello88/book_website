import os
import json
from flask import Flask, render_template, request, flash, session, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

#print(os.environ)
for k, v in os.environ.items():
    print(f'{k}={v}')

app = Flask(__name__) 
app.config["MONGO_DBNAME"] = 'plantstoreDB'
app.config["MONGO_URI"] = os.environ['MONGO_URI']
SECRET_KEY = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plantsforbeginners')
def plantsforbeginners():
    return render_template('plantsforbeginners.html')

# Route for handling the login page logic https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
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
          print(session, "+++++++++++session")
          flash('You were successfully logged in', 'message') 
          return redirect(url_for('index'))
        else:
          flash('Invalid password or username provided', 'error')
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
@app.route("/cart", methods=['GET', 'POST', 'PUT'])
def shopping_cart():
    user = session.get("username")
    if not user:
        flash("Please login to view your cart", 'message')
        return redirect(url_for("login"))
    if request.method == 'GET':
        all_products = []
    #retrieve the user from cart collection:
        user_cart = mongo.db.cart.find({"action": user}) 
    #loop through each cart item, fetch product with find_one
        for product in user_cart:
            cart_product = mongo.db.catalogue.find_one({"_id": ObjectId(oid=str(product["product_id"]))})
            cart_product["quantity"] = int(product["quantity"])
            all_products.append(cart_product)
        return render_template("cart.html", products=all_products)
    if request.method == 'POST':
        req = request.form.to_dict()
        quantity = req.get("quantity")
        product_id = request.args.get('product_id')
        if not quantity:
            mongo.db.cart.delete_one({"action": user, "product_id": product_id})
            return redirect(url_for('shopping_cart'))
        mongo.db.cart.update_one({"product_id": product_id, "action": user}, {"$set": {"quantity": quantity}}) #set does the updating, set the quantity to a particular value
        flash('Your cart was updated', 'message')
        return redirect(url_for('shopping_cart'))

   
 
@app.route('/add_cart', methods=['POST'])
def add_cart():
    #insert into cart collection 
    #fetch user_id from session
    #insert username into cart collection through name attribute
    #to fetch items of the cart collection:  mongodb '.find({user_id:...})' 
    user = session.get("username")
    if not user:
        flash("Please login in order to make a purchase", 'message')
        return redirect(url_for("login"))
    cart_request = request.form.to_dict() #returns a dictionary
    product = mongo.db.cart.find_one({"product_id": cart_request["product_id"], "action": user}) # fetch items of the cart collection
    if product is None:
        flash("Item(s) added to cart", 'message')
    if product:
        flash('Already added to cart', 'message')
        return redirect(url_for('shop')) 
    cart_request['action'] = user 
    cart = mongo.db.cart 
    cart.insert_one(cart_request)
    return redirect(url_for('shop'))
 


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)