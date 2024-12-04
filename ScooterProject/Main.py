# Import classes here
from classes.Scooter import Scooter
from classes.User import User
from classes.ScooterApp import ScooterApp

def main():
    # You can run any of your classes here to test the outputs
    app = ScooterApp()

    # Uncomment and modify the following as needed to test different features
    # my_user = app.register_user('salman1', '1234', 30)
    # app.login_user('salman1', '1234')
    # app.logout_user('salman1')

    # Create scooters
    scooter1 = app.create_scooter('Location1')
    scooter2 = app.create_scooter('Location1')

    # Dock scooters
    #app.dock_scooter(scooter1, 'Location1')
    #app.dock_scooter(scooter2, 'Location1')

    # Try docking the same scooter again (should throw an error or handle gracefully)
    try:
        app.dock_scooter(scooter1, 'Location1')
    except Exception as e:
        print(e)

    # Print inventory and status
    app.print_inventory()

if __name__ == "__main__":
    main()
