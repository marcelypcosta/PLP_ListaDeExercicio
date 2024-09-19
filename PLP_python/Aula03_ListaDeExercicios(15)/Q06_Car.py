class Motor:
    def __init__(self, motor_type):
        self.motor_type = motor_type

class Car:
    def __init__(self, motor):
        self.motor = motor

    def show_car_details(self):
        """
        Displays the details of the car, specifically its motor type.
        """
        print("Carro com motor: {}".format(self.motor.motor_type))

if __name__ == "__main__":
    motor = Motor("V8")
    car = Car(motor)
    car.show_car_details()