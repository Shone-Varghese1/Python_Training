import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Emerging@2361',
    database='company_db')
try:
    with conn.cursor() as cursor:
        sql = "DELETE FROM employees WHERE emp_id = %s"
        data = (103,)
        cursor.execute(sql, data)
        conn.commit()
        print("Data deleted successfully")
except Exception as e:
    print(f"Error: {e}")