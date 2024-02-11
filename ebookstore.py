# This is an ebookstore project developed in Python with SQLite3. It can be used by a bookstore clerk to:
  # 1) add new books to the database (called 'ebookstore.db' with a table called 'books')
  # 2) view books in the database
  # 3) update book information
  # 4) create a backup database
  # 5) delete books from the database
  # 6) search the database to find specific books


# Import the SQLite3 module from the Python Standard Library:
import sqlite3

# Create a database called 'ebookstore.db' and connect to it (use ':memory:' for trial):
db = sqlite3.connect('ebookstore.db')

# Get a cursor object:
cursor = db.cursor()

# Create the table called 'books':
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, quantity INTEGER)')
    
create_table()

# Populate the table:
sample_book_list = [
(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
(3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
(3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
(3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

cursor.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", sample_book_list)
db.commit()

# Add data to the database:
def data_entry():
    while True:
        try:        
            data_entery_option = input('Would you like to entry data (yes/no)? \n').lower()
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
        if data_entery_option == 'yes':
            while True:
                try:
                    input_id = int(input('Please enter "id": '))
                except ValueError:
                    print('Invalid input. Please try again.')
                    continue
                list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                if input_id in list_id:
                    print('The id already exists. Please try another one.')
                else:
                    break
            while True:
                try:
                    input_title = input('Please enter "title": ').title()
                    if input_title == '':
                        raise Exception()
                except:
                    print('No input found. Please try again.')
                    continue
                else:
                    break
            while True:
                try: 
                    input_author = input('Please enter "author": ').title()
                    if input_author == '':
                        raise Exception()
                except:
                    print('No input found. Please try again.')
                    continue
                else:
                    break
            while True:
                try:
                    input_quantity = int(input('Please enter "quantity": '))
                except ValueError:
                    print('Invalid input. Please try again.')
                    continue
                else:
                    break
        elif data_entery_option == 'no':
            return user_option   
        else:
            print('Invalid input. Please try again.')
            continue
        cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?)", (input_id, input_title, input_author, input_quantity))
        print('The book has been added.')
        db.commit()

# View data in the database:
def view_data():
    cursor.execute('SELECT * FROM books')
    data = cursor.fetchall()
    for i in data:
        print(i)

# Update data in the database:
def update_data():
    while True:
        try: 
            update_data_option = input("Would like to update data: 'yes' or 'no'? \n").lower()
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
        if update_data_option == 'yes':
            while True:
                try: 
                    what_to_update = input("What would like to update: 'title', 'author' or 'quantity'? \n").lower()
                except ValueError:
                    print("Invalid input. Please enter 'title', 'author' or 'quantity'.")
                if what_to_update == 'title':
                    while True:
                        try:
                            input_id = int(input('Please enter "id": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue
                        list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                        if input_id not in list_id:
                            print('The id you entered does not exist. Please try again.')
                        else:
                            break       
                    while True:
                        try:
                            updated_title = input('Please enter "new title": ')
                            if updated_title == '':
                                raise Exception()
                        except:
                            print('No input found. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("UPDATE books SET title = ? WHERE id = ?", (updated_title, input_id))
                    db.commit()
                    print('The data have been updated.')
                    return user_option
                elif what_to_update == 'author':
                    while True:
                        try:
                            input_id = int(input('Please enter "id": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue
                        list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                        if input_id not in list_id:
                            print('The id you entered does not exist. Please try again.')
                        else:
                            break
                    while True:
                        try:
                            updated_author = input('Please enter "new author": ').title()
                            if updated_author == '':
                                raise Exception()
                        except:
                            print('No input found. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("UPDATE books SET author = ? WHERE id = ?", (updated_author, input_id))
                    db.commit()
                    print('The data have been updated.')
                    return user_option
                elif what_to_update == 'quantity':
                    while True:
                        try:
                            input_id = int(input('Please enter "id": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue
                        list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                        if input_id not in list_id:
                            print('The id you entered does not exist. Please try again.')
                        else:
                            break
                    while True:
                        try:
                            updated_quantity = int(input('Please enter "new quantity": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("UPDATE books SET quantity = ? WHERE id = ?", (updated_quantity, input_id))
                    db.commit()
                    print('The data have been updated.')
                    return user_option
                else:
                    print('Invalid input. Please try again.')
                    break
        elif update_data_option == 'no':
            return user_option
        else:
            print('Invalid input. Please try again.')
            continue

# Create a backup database:
def backupdb():
    backup_db = sqlite3.connect('ebookstore_backup.db') 
    db.backup(backup_db)
    backup_db.close()

# Delete data in the database:
def delete_data():
    while True:
        try:
            delete_data_option = input("Would you like to delete data: 'yes' or 'no'? ").lower()
        except ValueError:
            print('Invalid input. Please try again.')
        if delete_data_option == 'yes':
            while True:
                try:
                    input_id = int(input('Please enter "id": '))
                except ValueError:
                    print('Invalid input. Please try again.')
                    continue
                list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                if input_id not in list_id:
                    print('The id you entered does not exist. Please try again.')
                else:
                    break
            cursor.execute("DELETE FROM books WHERE id = ?", (input_id,))
            db.commit()
            print('The book has been deleted.')
        elif delete_data_option == 'no':
            return user_option
        else:
            print('Invalid input. Please try again.')
            continue

# Search data in the database:
def search_data():
    while True:
        try:
            search_data_option = input("Would you like to search data: 'yes' or 'no'? ").lower()
        except ValueError:
            print('Invalid input. Please try again.')
        if search_data_option == 'yes':
            while True:
                try: 
                    what_to_search_by = input("What would you like to search by: 'id', 'title', 'author' or 'quantity'? \n").lower()
                    if what_to_search_by == '':
                        raise Exception()
                except:
                    print('No input found. Please try again.')
                    continue
                if what_to_search_by == 'id':
                    while True:
                        try:
                            input_id = int(input('Please enter "id": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue  
                        list_id = [i[0] for i in cursor.execute('SELECT id FROM books')]
                        if input_id not in list_id:
                            print('The id you entered does not exist. Please try again.')
                        else:
                            break
                    cursor.execute("SELECT * FROM books WHERE id = ?", (input_id,))
                    data = cursor.fetchone()
                    print(data)
                    db.commit()
                    return user_option
                if what_to_search_by == 'title':
                    while True:
                        try:
                            input_title = input('Please enter "title": ').lower()
                            if input_title == '':
                                raise Exception()
                        except:
                            print('No input found. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("SELECT * FROM books WHERE title = ?", (input_title,))
                    data = cursor.fetchone()
                    print(data)
                    db.commit()
                    return user_option
                if what_to_search_by == 'author':
                    while True:
                        try:
                            input_author = input('Please enter "author": ').lower()
                            if input_author == '':
                                raise Exception()
                        except:
                            print('No input found. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("SELECT * FROM books WHERE author = ?", (input_author,))
                    data = cursor.fetchone()
                    print(data)
                    db.commit()
                    return user_option
                if what_to_search_by == 'quantity':
                    while True:
                        try:
                            input_quantity = int(input('Please enter "quantity": '))
                        except ValueError:
                            print('Invalid input. Please try again.')
                            continue
                        else:
                            break
                    cursor.execute("SELECT * FROM books WHERE quantity = ?", (input_quantity,))
                    data = cursor.fetchone()
                    print(data)
                    db.commit()
                    return user_option
        elif search_data_option == 'no':
            return user_option
        else:
            print('Invalid input. Please try again.')
            continue

# Create a menu for the user to execute the functions above:
while True:
    user_option = input('''\nPlease select from one of the following options: 
            a - Add books
            v - View books
            u - Update books 
            c - Create a backup database
            d - Delete books
            s - Search books
            e - Exit the program
            \n''').lower()
    if user_option == 'a':
        data_entry()
    elif user_option == 'v':
        view_data()
    elif user_option == 'u':
        update_data()
    elif user_option == 'c':
        backupdb()
    elif user_option == 'd':
        delete_data()
    elif user_option == 's':
        search_data()
    elif user_option == 'e':
        print('Goodbye!')
        break
    else:
        print('Invalid option. Please try again.')
        continue

# Close the database connection:
db.close()