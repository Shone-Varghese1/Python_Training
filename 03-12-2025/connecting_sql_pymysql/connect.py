
import pymysql

from db import get_conn

conn = get_conn()
cursor=conn.cursor()
cursor.execute('select * from employees')
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()