# This file will handle the connection to the database

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector


class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='flags')
        self.cursor = self.conn.cursor()

    def encrypt_pass(self, post_data):
        password = post_data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed

    # This method will insert a new user into the database.
    def insert(self, user, hashed):
        user_created = True
        self._SQL = """insert into users
          (firstName, lastName, email, username, password)
          values
          (%s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.first_name, user.last_name, user.email, user.username, hashed))
        self.conn.commit()
        return user_created
