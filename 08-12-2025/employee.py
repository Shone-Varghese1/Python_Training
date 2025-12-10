from flask import Flask, request, Flask,jsonify

app = Flask(__name__)
employee=[
    {"name":"Shone","age":22,"emp_id":101},
    {"name":"Hari","age":23,"emp_id":102},
    {"name":"Shiva","age":20,"emp_id":103}
]

@app.route('/employee', methods=['GET'])
def get_employee():
    return jsonify(employee)
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    item=data.get("item")
    employee.append(item)
    return "POST EXECUTED"
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee_name(emp_id):
    data = request.get_json()
    new_value = data.get("item")
    for item in employee:
        if item["emp_id"] == emp_id:
            item["name"] = new_value
    # data = request.get_json()
    # new_value=data.get("item")
    # employee[index]=new_value
    return "PUT EXECUTED"
@app.route('/employee/<int:index>', methods=['DELETE'])
def delete_employee(index):
    employee.pop(index)
    return "DELETE EXECUTED"
if __name__ == '__main__':
    app.run()