from flask import Flask, url_for, request, redirect, abort, jsonify
from StockDAO import stockDAO

app  = Flask(__name__, static_url_path='', static_folder='.')

##################################################################
# create()
#
# Action = Create a stock item in the DB
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Category\": \"Stationary\", \"Name\":\"Handbook\", \"Quantity\":10 }" "http://127.0.0.1:5000/Stock"

@app.route('/stock', methods=['POST'])
def create():
    #return "in create"

    if not request.json:
        abort(400)
    
    # id - Auto increment 
    Stock = {
        "Category": request.json['Category'],
        "Name": request.json['Name'],
        "Quantity": request.json['Quantity'] 
    }

    # Make the tuple for DB
    values = (Stock['Category'], Stock['Name'], Stock['Quantity'])
    newId = stockDAO.create(values)
    Stock['id'] = newId

    return jsonify(Stock)


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)