class Car():
    print("Driving a car.")
    pass

class Bike():
    print("Driving a bike.")
    pass

class Truck():
    print("Driving a truck.")
    pass



class VehicleFactory:
    def get_vehicle(vehicle_type):
        match vehicle_type:
            case 'car':
                return Car()
            case 'bike':
                return Bike()
            case 'truck':
                return Truck()
            case _:
                raise ValueError("Unknown vehicle type")
    
