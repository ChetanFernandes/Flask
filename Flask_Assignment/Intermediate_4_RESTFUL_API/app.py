from flask import Flask, render_template , make_response, jsonify, request
app = Flask(__name__)

stock = {
    "fruit": {
        "apple": 30,
        "banana" : 45,
        "cherry": 1000
    }
}
# GET REQUEST 
@app.route("/qs") #Query string
def qs():
    if request.args:
        req = request.args
        return " , ".join(f"{k}:{v}" for k, v in req.items())
    return "no query"

@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock) ,200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):

    if collection in stock:
        res = make_response(jsonify(stock[collection]),200)
        return res

    else:
        res = make_response(jsonify({"message":"Collection not in stock"}), 400)
        return res

@app.route("/stock/<collection>/<member>")
def get_collection_member(collection,member):

    if collection in stock:
        member = stock[collection][member] # stock[collection].get(member)
        if member:
            res = make_response(jsonify(member),200)
            return res

        else:
            res = make_response(jsonify({"error":"Member not found"}) ,400)
            return res

    res = make_response(jsonify({"error":"Collection not found"}) ,400)
    return res

# POST - Create a collection
@app.route("/stock/<collection>", methods = ["POST"])
def create_collection(collection):
    req = request.get_json()

    if collection in stock:
        res = make_response(jsonify({"error":"collection already exist"}),400)
        return res

    stock.update({collection:req})
    res = make_response(jsonify({"message":"Collection created"}),200)
    return res

#GET and POST
@app.route("/add-collection", methods = ["GET","POST"])
def add_collection():
    if request.method == "POST":

        req = request.form   

        collection = req.get("collection")
        member = req.get("member")
        qty = req.get("qty")

        if collection in stock:
            message = "collection already exist"
            return render_template("add.html", stock = stock, message=message)

        stock[collection] = {member:qty}
        message = "collection created"
        return render_template("add.html", stock = stock, message=message)

    return render_template("add.html",stock = stock)


# PUT  a collection
@app.route("/stock/<collection>", methods = ["PUT"])
def put_collection(collection):
    req = request.get_json()
    #stock[collection] = req
    stock.update({collection:req})
    res = make_response(jsonify({"message":"Collection replaced/created"}) ,200)
    return res

# Patch  a collection
@app.route("/stock/<collection>", methods = ["PATCH"])
def patch_collection(collection):
    """
    updates or creates a collection. Expected body : {"member": qty}
    """
    req = request.get_json()
    if collection in stock:
        for k , v in req.items():
            stock[collection][k] = v
             
        res = make_response(jsonify({"message":"Collection updated"}) ,200)
        return res

    stock[collection] = req
    res = make_response(jsonify({"message":"Collection created"}) ,200)
    return res

# Patch  a collection and member
@app.route("/stock/<collection>/<member>", methods = ["PATCH"])
def patch_collection_member(collection,member):
    """
    updates or creates a collection. Expected body : {"member": qty}
    """
    req = request.get_json()
    if collection in stock:
        for k , v in req.items():
            if member in stock[collection]:
                stock[collection][k] = v
                res = make_response(jsonify({"message":"Collection updated"}) ,200)
                return res

            stock[collection][member] = v
            res = make_response(jsonify({"message":"Collection created"}) ,200)
            return res

    res = make_response(jsonify({"error":"Collection not found"}) ,400)
    return res

# DELETE  a collection 
@app.route("/stock/<collection>", methods = ["DELETE"])
def delete_collection(collection):
    """
    updates or creates a collection. Expected body : {"member": qty}
    """
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"message":"Collection deleted"}) ,204)
        return res
    res = make_response(jsonify({"error":"Collection not found"}) ,400)
    return res

@app.route("/stock/<collection>/<member>", methods = ["DELETE"] )
def delete_collection_member(collection,member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({}),204)
            return res
        
        res = make_response(jsonify({'error': "member not found"}),400)
        return res
    res = make_response(jsonify({'error': "collection not found"}),400)


if __name__ =='__main__':
    app.run(debug = True, host = "0.0.0.0", port = 5000)
