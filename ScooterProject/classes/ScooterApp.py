from classes.Scooter import Scooter
from classes.User import User


class ScooterApp:
    def __init__(self):
        self.stations = {
            "Location1": [],
            "Location2": [],
            "Location3": [],
        }
        self.registered_users = {}

    def register_user(self, username, password, age):
        if username in self.registered_users:
            raise Exception("User already registered.")
        if age < 18:
            raise Exception("Too young to register.")
        user = User(username, password, age)
        self.registered_users[username] = user
        return user

    def login_user(self, username, password):
        user = self.registered_users.get(username)
        if not user or user.password != password:
            raise Exception("Username or password is incorrect.")
        user.login()
        print("User has been logged in.")

    def logout_user(self, username):
        user = self.registered_users.get(username)
        if not user:
            raise Exception("Username is incorrect.")
        user.logout()
        print("User has been logged out.")

    def create_scooter(self, station):
        if station not in self.stations:
            raise Exception("No such station.")
        scooter = Scooter(station)
        self.stations[station].append(scooter)
        print(f"Created new scooter {scooter.serial} at {station}.")
        return scooter

    def dock_scooter(self, scooter, station):
        if station not in self.stations:
            raise Exception("No such station.")
        for location, scooters in self.stations.items():
            if scooter in scooters:
                raise Exception("Scooter already at station.")
        self.stations[station].append(scooter)
        scooter.dock(station)

    def rent_scooter(self, scooter, user):
        if not user:
            raise Exception("No such user.")
        for location, scooters in self.stations.items():
            if scooter in scooters:
                scooters.remove(scooter)  # Remove the scooter from the station
                break
        scooter.rent(user)

    def print_inventory(self):
        for username in self.registered_users:
            print(f"{username} - User details")
        for location, scooters in self.stations.items():
            count = len(scooters)
            print(f"Total Count of scooters {count} at location {location}")


# Assuming the `User` and `Scooter` classes are defined elsewhere:
# from User import User
# from Scooter import Scooter
