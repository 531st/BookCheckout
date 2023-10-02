import uuid
from datetime import datetime
import sqlite3

class Record:

    def __init__(self, book_id, name, author, operation, carrier):

        self.operation_id = str(uuid.uuid4())
        self.book_id = book_id
        self.name = name
        self.author = author
        self.operation = operation
        self.carrier = carrier
        self.date = datetime.now().strftime("%d-%m-%y %H:%M")


    def record(self):
        # Add log record
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO logs (uuid, book_name, author, operation, carrier, operation_date)
         VALUES (?, ?, ?, ?, ?, ?)""", 
         (self.operation_id, self.name, self.author, self.operation, self.carrier, self.date))

        # Execute a SELECT query to find the row by its ID
        cursor.execute("SELECT * FROM books WHERE uuid = ?", (self.book_id,))
        row = cursor.fetchone()

        # If the row is found, update its columns
        if row:
            # Execute an UPDATE query to change the columns
            cursor.execute("UPDATE books SET status = ?, carrier = ?, last_change =? WHERE uuid = ?", 
            (self.operation, self.carrier, self.date, self.book_id,))
            print(f"Row {self.book_id} updated successfully.")

        else:
            cursor.execute("""INSERT INTO books (uuid, book_name, author, status, carrier, last_change)
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (self.book_id, self.name, self.author, "In Stock", self.carrier, self.date))
            print(f"New book {self.name} added to DB.")
        
        conn.commit()
        conn.close()
    
    # Alternative class instance creation
    @classmethod
    def from_qr_string(cls, string, operation, carrier):
        
        data_list = string
        data_list = string.strip('[]')
        data_list = data_list.split(', ')
        data_list = [s.strip() for s in data_list]

        return cls(data_list[0], data_list[1], data_list[2], operation, carrier)  