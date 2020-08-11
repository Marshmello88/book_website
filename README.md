                    <!-- <form action="{{ url_for('add_product') }}" method="POST">-->

@app.route('/add_product', methods=['POST'])
def add_product():
    #get user_id
    #product_id, quantity, via post method?
    #does the person have an existing cart?
    # if yes, update
    #if no create + update products.insert_one(request.form.to_dict())
    print("********")
    print(request.form)
    products = mongo.db.products 
    products.insert_one(request.form.to_dict())
    return redirect(url_for('shop'))