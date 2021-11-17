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

SHOW COLUMNS FROM users;

INSERT INTO users
VALUES (1, 'test', 'a1@yahoo.com', 'test');

DELETE FROM users WHERE user_id = 2;