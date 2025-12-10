from flask import Flask, request, Flask,jsonify
import pymysql.cursors
app = Flask(__name__)

from db import get_conn



@app.route('/employee', methods=['GET'])
def get_employee():
    conn=None
    try:
        conn = get_conn()
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('select * from employees')
            rows = cursor.fetchall()
            return jsonify(rows)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

@app.route('/employee', methods=['POST'])
def add_employee():
    conn = None
    data = request.get_json()
    item=data.get("item")
    name1=item.get("name")
    dept=item.get("department")
    salary1=item.get("salary")
    mail=item.get("email")
    id1=item.get("emp_id")
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            sql = "INSERT INTO employees (emp_id,emp_name,email,salary,dept_id) VALUES (%s, %s,%s,%s,%s)"
            data = (id1, name1, mail, salary1, dept)
            cursor.execute(sql, data)
            conn.commit()
            print("Data inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
    return "POST EXECUTED"
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee_name(emp_id):
    conn = None
    data = request.get_json()
    new_value = data.get("item")
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            sql = "UPDATE employees SET emp_name = %s WHERE  emp_id= %s"
            data = (new_value, emp_id)
            cursor.execute(sql, data)
            conn.commit()
            print("Data updated successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
    return "POST EXECUTED"
@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            sql = "DELETE FROM employees WHERE emp_id = %s"
            data = (emp_id,)
            cursor.execute(sql, data)
            conn.commit()
            print("Data deleted successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
    return "DELETE EXECUTED"
if __name__ == '__main__':
    app.run()