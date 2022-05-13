--How to update:
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

--So I'd need to do this: 
UPDATE discussions
SET votes = 
WHERE discussion_id = ;

def update_username_and_email(self, post_data):
        self._SQL = """UPDATE users SET username = %s, email = %s
        where user_id = %s"""
        self.cursor.execute(self._SQL, (post_data['username'], post_data['email'], post_data['id']))
        self.conn.commit()
