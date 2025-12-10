
import logging
from flask import Flask, request, jsonify, abort
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

# ----------------------------------------------------
# DB CONNECTION
# ----------------------------------------------------
def get_db():
    try:
        conn = mysql.connector.connect(
          #connection variables
        )
        if conn.is_connected():
            return conn
        raise RuntimeError("DB connection not established")
    except Error as e:
        logging.error(f"DB connection error: {e}")
        raise


# ----------------------------------------------------
@app.route("/employees", methods=["GET"])
def get_employees():
    logging.debug("GET /employees called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing SELECT query")
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500
@app.route("/employees/inner_join", methods=["GET"])
def get_employees_dept():
    logging.debug("GET /employees/inner_join called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing inner join query")
        cursor.execute("SELECT name,dept_name FROM employees e inner join departments d on e.dept_id=d.dept_id")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500
@app.route("/employees/left_join", methods=["GET"])
def get_employees_dept_left():
    logging.debug("GET /employees/left_join called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing inner join query")
        cursor.execute("SELECT name,dept_name FROM employees e left join departments d on e.dept_id=d.dept_id")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500
@app.route("/employees/right_join", methods=["GET"])
def get_employees_dept_right():
    logging.debug("GET /employees/right_join called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing inner join query")
        cursor.execute("SELECT name,dept_name FROM employees e right join departments d on e.dept_id=d.dept_id")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500
# ----------------------------------------------------
# POST EMPLOYEE
# ----------------------------------------------------
@app.route("/employees", methods=["POST"])
def add_employee():
    logging.debug("POST /employees called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "INSERT INTO employees (name, role, salary,dept_id) VALUES (%s, %s, %s,%s)"
        logging.debug(f"Executing INSERT: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"],data["dept_id"]))
        db.commit()
        db.close()

        logging.debug("POST completed")
        return "POST EXECUTED"
    except Exception as e:
        logging.error(f"Error in POST: {e}")
        return "POST ERROR", 500

# ----------------------------------------------------
# PUT EMPLOYEE
# ----------------------------------------------------
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    logging.debug(f"PUT /employees/{id} called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "UPDATE employees SET name=%s, role=%s, salary=%s WHERE id=%s"
        logging.debug(f"Executing UPDATE: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"], id))
        db.commit()
        db.close()

        logging.debug("PUT completed")
        return "PUT EXECUTED"
    except Exception as e:
        logging.error(f"Error in PUT: {e}")
        return "PUT ERROR", 500

# ----------------------------------------------------
# DELETE EMPLOYEE
# ----------------------------------------------------
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    logging.debug(f"DELETE /employees/{id} called")
    try:
        db = get_db()
        cursor = db.cursor()

        sql = "DELETE FROM employees WHERE id=%s"
        logging.debug(f"Executing DELETE: {sql}")

        cursor.execute(sql, (id,))
        db.commit()
        db.close()

        logging.debug("DELETE completed")
        return "DELETE EXECUTED"
    except Exception as e:
        logging.error(f"Error in DELETE: {e}")
        return "DELETE ERROR", 500

# ----------------------------------------------------
# RUN
# ----------------------------------------------------
if __name__ == "__main__":
    logging.debug("Starting Flask server...")
    app.run(debug=True)
