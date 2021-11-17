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
