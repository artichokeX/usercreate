import sqlite3
import json



class ApiService:

    def __init__(self, db):
        self.db = db
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        
    def database(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS user(
                ID integer PRIMARY KEY,
                First_Name text NOT NULL,
                Last_Name text NOT NULL,
                Age integer,
                Department text
            );
        """)
        self.connection.commit()

    def insert(self, fname,lname,age,dept):
        self.database()
        insert = "INSERT INTO user(First_Name, Last_Name, Age, Department) VALUES (?,?,?,?)"
        self.connection.execute(insert, (fname,lname,age,dept))
        self.connection.commit()
        print("Entry added.")

    def remove(self, identifier):
        remove = f"DELETE FROM user WHERE ID = {identifier}"
        self.connection.execute(remove)
        self.connection.commit()
        print("Entry Removed.")

    def fetch(self):
        fetch = "SELECT * FROM user"
        array = self.connection.execute(fetch)
        payload = []
        for row in array:
            obj = list(row)
            payload.append(obj)
        return payload

    def quit(self):
        self.connection.close()
