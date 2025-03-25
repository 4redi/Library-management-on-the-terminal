import sqlite3

conn=sqlite3.connect('library.db')
cursor=conn.cursor()

def create_table():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Books(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL
        )
    ''')
    conn.commit()

def add_book(title,author,year,genre):
    cursor.execute('''
INSERT INTO Books(title,author,year,genre)
    VALUES(?,?,?,?)
                   
''',(title,author,year,genre))
    conn.commit()
    print(f"Book '{title}' added")

def view_books():
    cursor.execute('Select * from Books')
    books=cursor.fetchall()

    if books:
        cursor.execute('select count(title) from Books')
        count=cursor.fetchone()[0]
        print(f"{count} books in total")
        for book in books:
            print(f"ID: {book[0]},Title:{book[1]}, Author:{book[2]},Year:{book[3]},Genre:{book[4]}")
    else:
        print('No books found')

def delete_book(book_id):
    cursor.execute('select title from Books where id=?',(book_id,))
    book_to_delete=cursor.fetchone()
    if book_to_delete:
        cursor.execute('DELETE FROM Books where id=?',(book_id,))
        conn.commit()
        print(f'Book with {book_to_delete[0]} title has been deleted')
    else:
        print("book cant be found")

def update_book(book_id, title, author, year, genre):
    cursor.execute('SELECT * FROM Books WHERE id=?', (book_id,))
    book_to_update = cursor.fetchone()
    
    if book_to_update:
        cursor.execute('''
            UPDATE Books
            SET title = ?, author = ?, year = ?, genre = ?
            WHERE id = ?
        ''', (title, author, year, genre, book_id))
        conn.commit()
        print(f"Book with ID {book_id} updated successfully!")
    else:
        print(f"Book with ID {book_id} can't be found.")


def menu():
    create_table()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Delete a book")
        print("4. Update book details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter year of publication: "))
            genre = input("Enter genre: ")
            add_book(title, author, year, genre)
        
        elif choice == '2':
            view_books()
        
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        
        elif choice == '4':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author name: ")
            year = int(input("Enter new year of publication: "))
            genre = input("Enter new genre: ")
            update_book(book_id, title, author, year, genre)
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the menu
if __name__ == '__main__':
    menu()

# Close the connection
conn.close()