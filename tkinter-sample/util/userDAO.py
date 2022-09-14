import sqlite3
from .entities.user import User

class UserDAO():
    def insertUser(self, user: User):
        query = "INSERT INTO User (firstName, lastName, age, email, phone) VALUES (?,?,?,?,?)"
        values = (user.getFirstName(), user.getLastName(), user.getAge(), user.getEmail(), user.getPhone())
        # Start sql connection
        con = sqlite3.connect("demo.db")
        cur = con.cursor()
        # Execute query
        try:
            cur.execute(query, values)
            print("query executed successfully")
            # Always commit the transaction after executing INSERT.
            con.commit()
        # If an error occurs, then print error message
        except sqlite3.OperationalError as error:
            print(error)
        con.close()    
    
    def listUsers(self):
        users = []
        query = "SELECT * FROM User ORDER BY id"
        # Start sql connection
        con = sqlite3.connect("demo.db")
        cur = con.cursor()
        # Execute query
        try:
            cur.execute(query)
            print("query executed successfully")
        # If an error occurs, then print error message
        except sqlite3.OperationalError as error:
            print(error)
        # Show data
        for row in cur:
            user = User(row[1],row[2],int(row[3]),row[4],row[5])
            users.append(user)
        # Close connection
        con.close()
        return users
        
    def listUser(self, id):
        query = "SELECT * FROM User WHERE id = ? ORDER BY id"
        values = (id)
        # Start sql connection
        con = sqlite3.connect("demo.db")
        cur = con.cursor()
        # Execute query
        try:
            cur.execute(query, values)
            print("query executed successfully")
        # If an error occurs, then print error message
        except sqlite3.OperationalError as error:
            print(error)
        # Show data
        for row in cur:
            user = User(row[1],row[2],int(row[3]),row[4],row[5])
        con.close() 
        return user
    
    def deleteUser(self, id : str):
        query = "DELETE FROM User WHERE id = ?"
        values = (id)
        # Start sql connection
        con = sqlite3.connect("demo.db")
        cur = con.cursor()
        # Execute query
        try:
            cur.execute(query, values)
            print("query executed successfully")
            # Always commit the transaction after executing DELETE.
            con.commit()
        # If an error occurs, then print error message
        except sqlite3.OperationalError as error:
            print(error)
        con.close()
        
    def editUser(self, user : User, id : str):
        query = "UPDATE User SET firstName = ?, lastName = ?, age = ?, email = ?, phone = ? WHERE id = ?"
        values = (user.getFirstName(), user.getLastName(), user.getAge(), user.getEmail(), user.getPhone(), id)
        # Start sql connection
        con = sqlite3.connect("demo.db")
        cur = con.cursor()
        # Execute query
        try:
            cur.execute(query, values)
            print("query executed successfully")
            # Always commit the transaction after executing DELETE.
            con.commit()
        # If an error occurs, then print error message
        except sqlite3.OperationalError as error:
            print(error)
        con.close()