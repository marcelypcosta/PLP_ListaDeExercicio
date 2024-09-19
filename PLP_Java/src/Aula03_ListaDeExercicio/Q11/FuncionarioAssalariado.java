package Aula03_ListaDeExercicio.Q11;

public class FuncionarioAssalariado extends Funcionario {
    private double salary;

    public FuncionarioAssalariado(String name, double salary) {
        super(name);
        this.salary = salary;
    }

    @Override
    public double calcularSalario() {
        return salary;
    }
}
