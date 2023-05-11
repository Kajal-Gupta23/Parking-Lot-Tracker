from parking_lot import ParkingLot

def main():
    parking_lot = ParkingLot()

    # Display the main menu
    while True:
        print('Please select an option:')
        print('1. Assign parking space to a new vehicle')
        print('2. Retrieve the parking spot of a vehicle')
        print('3. Exit')
        choice = input('> ')

        if choice == '1':
            # Assign a parking spot to a new vehicle
            vehicle_number = input('Enter vehicle number: ')
            spot = parking_lot.assign_spot(vehicle_number)
            if spot is not None:
                print(f'Vehicle parked at level {spot["level"]} spot {spot["spot"]}')
            else:
                print('Sorry, no spots available.')

        elif choice == '2':
            # Retrieve the parking spot of a vehicle
            vehicle_number = input('Enter vehicle number: ')
            spot = parking_lot.retrieve_spot(vehicle_number)
            if spot is not None:
                print(f'{{"level": {spot["level"]}, "spot": {spot["spot"]}}}')

            else:
                print('Vehicle not found.')

        elif choice == '3':
            # Exit the program
            print('Bye!')
            break

        else:
            # Invalid input, display an error message
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
