package Aula03_ListaDeExercicio;

public class Q01_Car {
    // Class attributes
    private String brand;
    private String model;
    private int year;

    // Class constructor
    public Q01_Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Method to display car details
    public void displayDetails() {
        System.out.println("Brand: " + brand + ", Model: " + model + ", Year: " + year);
    }

    // Main method to test the class
    public static void main(String[] args) {
        Q01_Car car1 = new Q01_Car("Toyota", "Corolla", 2020);
        Q01_Car car2 = new Q01_Car("Honda", "Civic", 2019);
        Q01_Car car3 = new Q01_Car("Ford", "Mustang", 2021);

        car1.displayDetails();
        car2.displayDetails();
        car3.displayDetails();
    }
}
