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

--Table modified 
CREATE TABLE discussions
(
  discussion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  graph_number INT NOT NULL, 
  post TEXT NOT NULL,
  discussion_sentiment INT,
  votes INT, 
  created TIMESTAMP, 
  FOREIGN KEY (user_id) REFERENCES users(user_id)
  ON DELETE CASCADE
);

SHOW COLUMNS FROM users;

--Altering the discussions table:
ALTER TABLE discussions 
ADD COLUMN discussion_sentiment INT(255) AFTER post;

--Altering column type: 
ALTER TABLE discussions 
MODIFY COLUMN discussion_sentiment DEC(3,2);

--Altering Discussions Table:
ALTER TABLE discussions 
ADD COLUMN votes INT(255) AFTER discussion_sentiment;

--Altering Discussions Table:
Alter TABLE discussions 
ADD COLUMN created TIMESTAMP AFTER votes;



-- Inserting data 
INSERT INTO users
VALUES (1, 'test', 'a1@yahoo.com', 'test');

INSERT INTO discussions
VALUES (2, 2, 1, 'This is Bayan');

DELETE FROM users WHERE user_id = 2;
DELETE FROM discussions where discussion_id = 1;

Example projects: 
https://github.com/ravenusmc/blog_ratings/blob/master/sql/code.sql
https://github.com/ravenusmc/compost_finder/blob/master/db.py



promise examples: 
https://github.com/ravenusmc/nasa_project/blob/main/client/src/store/modules/people.js

def double_column_create(self, table_name, value1, data_type_1, value2, data_type_2):
    sql = '''CREATE TABLE ''' + table_name + ''' (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
        ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL' ''' ) '''

def get_single_row_data(self, table, id):
    query = ('''select * from ''' + table + ''' where id = %s ''')
    self.cursor.execute(query, (id, ))
    row = self.cursor.fetchone()
    return row