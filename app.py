from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to flask!"

@app.route('/hello/<name>')
def hello(name):
    return f"hello, {name}!"

@app.route('/data',methods=['get']) 
def get_data():
    data=request.json
    return {"data":data, "message": "send a post request with json data"}

@app.route('/data',methods=['post'])
def handle_data():
    data = request.json
    return {"message": "data received", "data": data}

@app.route('/update/<int:item_id>', methods=['put'])
def update_item(item_id):
    return {"message": f"Item (item_id) updated"}

@app.route('/delete/<int:item_id>',methods=["Delete"])
def delete_item(item_id):
    return {"message": f"item {item_id} deleted"}

if __name__ == '_main_':
    app.run(debug=true)
