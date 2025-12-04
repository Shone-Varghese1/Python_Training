
import pandas as pd
import pymysql

from db import get_conn

conn = get_conn()


def add_employee(id1,name1,mail,salary1,dept):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO employees (emp_id,emp_name,email,salary,dept_id) VALUES (%s, %s,%s,%s,%s)"
            data = (id1, name1, mail, salary1, dept)
            cursor.execute(sql, data)
            conn.commit()
            print("Data inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
def view_all_employee():
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from employees')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def update_salary(id1,sal):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE employees SET salary = %s WHERE  emp_id= %s"
            data = (sal,id1 )
            cursor.execute(sql, data)
            conn.commit()
            print("Data updated successfully")
    except Exception as e:
        print(f"Error: {e}")
def delete_employee(id1):
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM employees WHERE emp_id = %s"
            data = (id1,)
            cursor.execute(sql, data)
            conn.commit()
            print("Data deleted successfully")
    except Exception as e:
        print(f"Error: {e}")
def search_name(name1):
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from employees where emp_name = %s',(name1,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def to_csv():


    df = pd.read_sql("SELECT * FROM employees", con=conn)
    df.to_csv("employee.csv", index=False, encoding="utf-8")


print("*"*10,"welcome to employee management dashboard","*"*10)
str1="""
            operations
            1. Add employee
            2. View employee
            3. Update salary
            4.Delete employee
            5. Search by name
            6. Export to CSV
            7.exit
"""
while True:
    choice=int(input(f"{str1} Enter your choice"))
    if choice==1:
        name=input("Enter employee name:")
        emp_id=int(input("Enter employee id:"))
        salary=int(input("Enter salary:"))
        dep=int(input("Enter department:"))
        email=input("Enter email address:")
        add_employee(emp_id,name,email,salary,dep)
    elif choice==2:
        view_all_employee()
    elif choice==3:
        emp_id = int(input("Enter employee id you want to change salary :"))
        salary = int(input("New salary:"))
        update_salary(emp_id,salary)
    elif choice==4:
        emp_id = int(input("Enter employee id you need to delete:"))
        delete_employee(emp_id)
    elif choice==5:
        name = input("Enter employee name whose record to be pulled :")
        search_name(name)
    elif choice==6:
        to_csv()
    elif choice==7:
        break





