import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Emerging@2361',
    database='company_db')



try:
   with conn.cursor() as cursor:
       sql = "UPDATE employees SET email = %s WHERE  emp_name= %s"
       data = ("updated_email@example.com", "Tim david")
       cursor.execute(sql, data)
       conn.commit()
       print("Data updated successfully")
except Exception as e:
   print(f"Error: {e}")