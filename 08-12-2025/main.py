from flask import Flask, request, Flask,jsonify

app = Flask(__name__)
items=["apple","banana","orange"]

@app.route('/items', methods=['GET'])
def get_item():
    return jsonify(items)
@app.route('/create-item', methods=['POST'])
def create_item():
    return "POST EXECUTED"
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    item=data.get("item")
    items.append(item)
    return "POST EXECUTED"
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    new_value=data.get("item")
    items[index]=new_value
    return "PUT EXECUTED"
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    items.pop(index)
    return "DELETE EXECUTED"
if __name__ == '__main__':
    app.run()