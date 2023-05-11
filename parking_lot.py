class ParkingLotSystem:
    def __init__(self, level, spot_number):
        self.level = level
        self.spot_number = spot_number
        self.vehicle_number = None

    def is_empty(self):
        return self.vehicle_number is None


class ParkingLot:
    def __init__(self):
        # Create spots for level A and B
        spots_A = [ParkingLotSystem('A', i + 1) for i in range(20)]
        spots_B = [ParkingLotSystem('B', i + 1) for i in range(20)]

        # Combine the spots into a single list
        self.spots = spots_A + spots_B

    def assign_spot(self, vehicle_number):
        for spot in self.spots:
            if spot.is_empty():
                # If the spot is empty, assign it to the vehicle and return its spota
                spot.vehicle_number = vehicle_number
                return {'level': spot.level, 'spot': spot.spot_number}
            
        # If no empty spots are found, return None
        return None

    def retrieve_spot(self, vehicle_number):
        for spot in self.spots:
            if spot.vehicle_number == vehicle_number:
                # If the vehicle is found, return its spot
                return {'level': spot.level, 'spot': spot.spot_number}
            
        # If the vehicle is not found, return None
        return None