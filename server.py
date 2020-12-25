from flask import Flask, url_for, request, redirect, abort

app  = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return redirect(url_for('Login'))

@app.route('/login')
def Login():
    abort(401)
    return "serverd by Login"

@app.route('/user')
def getUser():
    return "Activated by getUser"


@app.route('/user/<int:id>')
def findByIdUser(id):
    return "activated by findByIdUser with id = " + str(id)


@app.route('/user', methods=['POST'])
def CreateUser():
    return "Activated by createUser"

@app.route("/demo_url_for")
def demoURLFor():
    returnString = "Usl for indexis " + url_for('index')
    returnString += "<br>"
    returnString += "url for findByID USER " + url_for('findByIdUser', id=123)
    return returnString

@app.route("/demo_request", methods=['POST', 'GET', 'DELETE'])
def demoRequest():
    return request.method


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)