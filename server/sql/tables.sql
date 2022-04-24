CREATE DATABASE flags;

use flags;

CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  username VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

CREATE TABLE discussions
(
  discussion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  graph_number INT NOT NULL, 
  post TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
  ON DELETE CASCADE
);

SHOW COLUMNS FROM users;

--Altering the discussions table:
ALTER TABLE discussions 
ADD COLUMN discussion_sentiment INT(255) AFTER post;

-- Inserting data 
INSERT INTO users
VALUES (1, 'test', 'a1@yahoo.com', 'test');

INSERT INTO discussions
VALUES (2, 2, 1, 'This is Bayan');

DELETE FROM users WHERE user_id = 2;

Example projects: 
https://github.com/ravenusmc/blog_ratings/blob/master/sql/code.sql
https://github.com/ravenusmc/compost_finder/blob/master/db.py


    def pull_user_info(self, username):
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        return row

    #This method will return all the users by city. 
    def find_by_city(self, user):
        #pulling individuals who live in the same city as the user, do not have the users username 
        #and are opposite of the user-if user is gardener than pull queries where users are a 
        #neighbor
        query = ("""SELECT * FROM users WHERE city = %s AND username != %s AND type != %s""")
        self.cursor.execute(query, (user.city, user.username, user.person_type))
        rows = self.cursor.fetchall()
        return rows

    def update(self, username_original, username, email, address, city, state, zipcode, person_type):
        self._SQL = """UPDATE users SET username = %s, email = %s, address = %s, city = %s, state = %s, zipcode = %s, type = %s
        where username = %s"""
        self.cursor.execute(self._SQL, (username, email, address, city, state, zipcode, person_type, username_original))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

query = ("""SELECT u.user_id, u.username, d.post FROM discussions d
INNER JOIN users u ON u.user_id = d.user_id WHERE graph_number = %s""")

SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
INNER JOIN committees c ON c.name = m.name;

promise examples: 
https://github.com/ravenusmc/nasa_project/blob/main/client/src/store/modules/people.js
