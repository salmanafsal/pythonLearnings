

class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.__logged_in = False  # Private attribute using double underscores

    def login(self, password):
        if password == self.password:
            self.__logged_in = True
            return self.__logged_in
        else:
            raise Exception("Incorrect Password")

    def logout(self):
        if not self.__logged_in:
            raise Exception("You cannot logout as you are not logged in")
        else:
            self.__logged_in = False


# Example Usage:
# user = User("user1", "password123", 25)
# user.login("password123")
# user.logout()
