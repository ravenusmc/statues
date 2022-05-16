# This file will handle the connection to the database

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime


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
        self.cursor.execute(self._SQL, (user.first_name,
                            user.last_name, user.email, user.username, hashed))
        self.conn.commit()
        return user_created

    # This method will check to ensure that the username is in the database.
    def check(self, username, password):
        # Setting up a user dictionary
        user = {}
        # encoding the password to utf-8
        password = password.encode('utf-8')
        # Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        # Here I check to see if the username is in the database.
        if str(row) == 'None':
            login_flag = False
            not_found = True
            password_no_match = False
        # If the user name is in the database I move here to check if the password
        # is valid.
        else:
            hashed = row[5].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == str(hashed, 'UTF-8'):
                user["id"] = row[0]
                user['first_name'] = row[1]
                user['last_name'] = row[2]
                user['email'] = row[3]
                user['username'] = row[4]
                login_flag = True
                not_found = False
                password_no_match = False
            # This is a final catch all area. Basically if the password does not match
            # the user is not getting in.
            else:
                login_flag = False
                not_found = False
                password_no_match = True
        return login_flag, not_found, password_no_match, user

    def get_specific_discussion_by_graph(self, selected_graph_number):
        query = ("""SELECT u.user_id, u.username, d.discussion_id, d.post, 
        d.discussion_sentiment, d.votes, d.created
        FROM discussions d
        INNER JOIN users u ON u.user_id = d.user_id WHERE graph_number = %s""")
        self.cursor.execute(query, (selected_graph_number,))
        graph_discussion_points = self.cursor.fetchall()
        return graph_discussion_points

    def get_specific_discussion_by_graph_order(self, post_data):
        query = ("""SELECT u.user_id, u.username, d.discussion_id, d.post, 
        d.discussion_sentiment, d.votes, d.created
        FROM discussions d
        INNER JOIN users u ON u.user_id = d.user_id 
        WHERE graph_number = %s
        ORDER BY """ +  post_data['column'] + ' ' + post_data['direction'])
        self.cursor.execute(query, (post_data['graph_number'],))
        graph_discussion_points = self.cursor.fetchall()
        print(graph_discussion_points)
        return graph_discussion_points

    def insert_new_discussion_point(self, post_data):
        initial_votes = 0
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._SQL = """insert into discussions
          (user_id, graph_number, post, discussion_sentiment, votes, created)
          values
          (%s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(
            self._SQL, (post_data['userid'], post_data['graph_number'], post_data['post'], post_data['sentiment_average'], initial_votes, timestamp))
        self.conn.commit()

    def delete_discussion_point(self, post_data):
        discussion_id = post_data['discussion_id']
        print(discussion_id)
        self._SQL = """DELETE FROM discussions WHERE discussion_id = %s"""
        self.cursor.execute(self._SQL, (discussion_id, ))
        self.conn.commit()

    def update_number_of_votes_on_discussion(self, post_data):
        self._SQL = """UPDATE discussions 
        SET votes =  %s
        where discussion_id = %s"""
        self.cursor.execute(
            self._SQL, (post_data['numberOfVotesCalculated'], post_data['discussionID']))
        self.conn.commit()
