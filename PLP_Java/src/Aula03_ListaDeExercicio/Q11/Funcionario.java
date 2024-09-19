package Aula03_ListaDeExercicio.Q11;

abstract class Funcionario {
    String name;

    public Funcionario(String name) {
        this.name = name;
    }

    // Método abstrato calcularSalario
    public abstract double calcularSalario();
}