package Aula03_ListaDeExercicio.Q11;

public class Main {
    public static void main(String[] args) {
        Funcionario horista = new FuncionarioHorista("João", 50, 160);
        Funcionario assalariado = new FuncionarioAssalariado("Maria", 3000);

        System.out.println("Salário de João: R$" + horista.calcularSalario());
        System.out.println("Salário de Maria: R$" + assalariado.calcularSalario());
    }
}
