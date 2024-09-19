class Car:
    def __init__(self, brand, model, year):
        """
        The constructor for Car class.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        """
        Prints the details of the car.
        """
        print('Brand: {}, Model: {}, Year: {}'.format(self.brand, self.model, self.year))


# Instantiating three objects of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

# Displaying the details of each car
car1.display_details()
car2.display_details()
car3.display_details()
