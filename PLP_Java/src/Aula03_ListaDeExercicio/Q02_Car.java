package Aula03_ListaDeExercicio;

// Defining the Car class
public class Q02_Car {
    // Class attributes
    private String brand;
    private String model;
    private int year;
    private int speed; // Speed initialized to 0

    // Class constructor
    public Q02_Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0; // Initial speed set to 0
    }

    // Method to display car details
    public void displayDetails() {
        System.out.println("Brand: " + brand + ", Model: " + model + ", Year: " + year);
    }

    // Method to accelerate the car
    public void accelerate(int amount) {
        this.speed += amount;
    }

    // Method to brake the car
    public void brake(int amount) {
        this.speed -= amount;
        if (this.speed < 0) {
            this.speed = 0; // Ensure the speed doesn't go below 0
        }
    }

    // Method to display the current speed
    public void displaySpeed() {
        System.out.println("Current speed: " + this.speed + " km/h");
    }

    // Main method to test the class
    public static void main(String[] args) {
        // Instantiating a car object
        Q02_Car car = new Q02_Car("Toyota", "Corolla", 2020);

        // Using the methods
        car.displayDetails();
        car.accelerate(50);
        car.displaySpeed();
        car.brake(20);
        car.displaySpeed();
        car.brake(40);
        car.displaySpeed();
    }
}
