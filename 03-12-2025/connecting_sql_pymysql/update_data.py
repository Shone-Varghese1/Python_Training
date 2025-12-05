
import pymysql

from db import get_conn

conn = get_conn()



try:
   with conn.cursor() as cursor:
       sql = "UPDATE employees SET email = %s WHERE  emp_name= %s"
       data = ("updated_email@example.com", "Tim david")
       cursor.execute(sql, data)
       conn.commit()
       print("Data updated successfully")
except Exception as e:
   print(f"Error: {e}")