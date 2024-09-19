package Aula03_ListaDeExercicio.Q04;

public class Main {
    public static void main(String[] args) {
        Q04_Animal dog = new Q04_Dog();
        Q04_Animal cat = new Q04_Cat();

        dog.makeSound();  // Output: Woof!
        cat.makeSound();  // Output: Meow!
    }
}