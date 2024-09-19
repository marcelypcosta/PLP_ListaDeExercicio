package Aula03_ListaDeExercicio.Q06;

public class Q06_Car {
    private Q06_Motor motor;

    public Q06_Car(Q06_Motor motor) {
        this.motor = motor;
    }

    public void showCarDetails() {
        System.out.println("Carro com motor: " + motor.getType());
    }

    public static void main(String[] args) {
        Q06_Motor motor = new Q06_Motor("V8");
        Q06_Car car = new Q06_Car(motor);
        car.showCarDetails();
    }
}
