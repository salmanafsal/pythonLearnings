

class Scooter:
    next_serial = 1  # Class variable for tracking serial numbers

    def __init__(self, station):
        self.station = station
        self.serial = 1
        self.serial += 1
        self.charge = 100
        self.is_broken = False
        self.scooter_users = []  # List to track users who have rented the scooter

    def rent(self, user):
        if self.charge > 20 and not self.is_broken:
            if user in self.scooter_users:
                print("Scooter already rented")
            else:
                self.scooter_users.append(user)
                print("Scooter is rented")
        elif self.charge <= 20:
            raise Exception("Scooter needs to charge")
        elif self.is_broken:
            raise Exception("Scooter needs repair")

    def dock(self, station):
        if self.scooter_users:
            self.scooter_users.pop()  # Remove the last user from the list
            self.station = station
            print("Scooter is docked")
        return self