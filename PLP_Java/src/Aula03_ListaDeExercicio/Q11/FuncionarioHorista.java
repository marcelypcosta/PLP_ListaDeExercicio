package Aula03_ListaDeExercicio.Q11;

public class FuncionarioHorista extends Funcionario {
    private double hourlyRate;
    private int hoursWorked;

    public FuncionarioHorista(String name, double hourlyRate, int hoursWorked) {
        super(name);
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    @Override
    public double calcularSalario() {
        return hourlyRate * hoursWorked;
    }
}
