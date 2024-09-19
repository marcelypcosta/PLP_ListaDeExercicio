class Q02_Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # Speed initialized to 0

    def display_details(self):
        """
        Prints the details of the car.
        """
        print('Brand: {}, Model: {}, Year: {}'.format(self.brand, self.model, self.year))

    def accelerate(self, amount):
        """
        Increases the speed of the car by a given amount.
        """
        self.speed += amount

    def brake(self, amount):
        """
        Decreases the speed of the car by a given amount, ensuring it doesn't go below 0.
        """
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def display_speed(self):
        """
        Displays the current speed of the car.
        """
        print('Current speed: {} km/h'.format(self.speed))


# Instantiating a car object
car = Q02_Car("Toyota", "Corolla", 2020)

# Using the methods
car.display_details()
car.accelerate(50)
car.display_speed()
car.brake(20)
car.display_speed()
car.brake(40)
car.display_speed()
