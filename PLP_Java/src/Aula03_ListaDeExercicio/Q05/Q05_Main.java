package Aula03_ListaDeExercicio.Q05;

public class Q05_Main {
    /**
     * Receives a list of Animal objects and calls the makeSound method of each one.
     */
    public static void makeSounds(Q05_Animal[] animals) {
        for (Q05_Animal animal : animals) {
            animal.makeSound();
        }
    }

    public static void main(String[] args) {
        Q05_Animal dog = new Q05_Dog();
        Q05_Animal cat = new Q05_Cat();
        Q05_Animal[] animals = {dog, cat};

        makeSounds(animals);
    }
}
