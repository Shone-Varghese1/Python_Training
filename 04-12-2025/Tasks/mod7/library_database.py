# Project 3: Library Database + Python Search
#
# Create MySQL tables for books and members
# Insert sample data
# Build Python script to search books by name/author
# Track borrow and return dates

from datetime import date

  # e.g., 2025-12-04


from db import get_conn2
conn = get_conn2()

print("#"*25 ,"Library Management System","#"*25)

def view_members():
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from members')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def view_books():

    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from books')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def search_book_name(name1):
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from books where book_name = %s', (name1,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")

def search_book_author(author1):
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from books where author = %s', (author1,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def show_transactions(id1):
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from transactions where member_id = %s', (id1,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
def borrow_book(mem_id,b_id,b_date):
    try:
        with conn.cursor() as cursor:
            count="select no_of_copies from books where book_id = %s;"
            cursor.execute(count,(b_id,))
            result=cursor.fetchone()
            if result and result[0]>0:
                sql = "INSERT INTO transactions (member_id, book_id, borrow_date)  VALUES (%s, %s,%s)"
                data = ( mem_id, b_id, b_date)
                cursor.execute(sql, data)
                # Update book copies
                update_query = "UPDATE books SET no_of_copies = no_of_copies - 1 WHERE book_id = %s;"
                cursor.execute(update_query, (b_id,))
                conn.commit()
                print("Data inserted successfully")

            else:
                print("book unavaliable right now check back later")
                return
    except Exception as e:
        print(f"Error: {e}")
def return_book(id1,id2):
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE transactions SET return_date = %s WHERE  member_id= %s and book_id= %s"
            today = date.today()
            data1 = (today,id1,id2 )
            cursor.execute(sql, data1)
            conn.commit()
            print("Data updated successfully")
    except Exception as e:
        print(f"Error: {e}")

str1="""
            operations
            1. view members
            2. View books
            3. search book by name
            4. search book ny author
            5. transactions for a user
            6. borrow a book
            7.return book
            8.exit
"""
while True:
    choice=int(input(f"{str1} Enter your choice"))
    if choice==1:
        view_members()
    elif choice==2:
        view_books()
    elif choice==3:
        name1=input("Enter Book name to search :")
        search_book_name(name1)
    elif choice==4:
        name1 = input("Enter author name to search :")
        search_book_author(name1)
    elif choice==5:
        id_m=int(input("Enter member id to know transaction history:"))
        show_transactions(id_m)
    elif choice==6:

        id1=int(input("Enter your member id:"))
        id2 = int(input("Enter book id to borrow:"))
        b_date=input("Enter your borrow date:")

        borrow_book(id1,id2,b_date)
    elif choice==7:
        m_id=int(input("Enter member id:"))
        b_id=int(input("Enter book id you want to return:"))
        return_book(m_id,b_id)
    elif choice==8:
        break



