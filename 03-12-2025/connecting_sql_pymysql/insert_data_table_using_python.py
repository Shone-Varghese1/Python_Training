import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Emerging@2361',
    database='company_db')
# cursor=conn.cursor()
# cursor.execute('select * from employees')
# rows=cursor.fetchall()
# for row in rows:
#     print(row)
# cursor.close()
# conn.close()



try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO employees (emp_id,emp_name,email,salary,dept_id) VALUES (%s, %s,%s,%s,%s)"
        data = (107,"Tim david","tim@company.com",75000,10)
        cursor.execute(sql, data)
        conn.commit()
        print("Data inserted successfully")
except Exception as e:
    print(f"Error: {e}")