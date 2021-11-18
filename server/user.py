# This file will have the class that will create the user object

class User():

    # Here I describe all the properties that each user object will have
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username 
        self.password = password
