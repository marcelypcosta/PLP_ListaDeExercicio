package Aula03_ListaDeExercicio.Q09;

public class Main {
    public static void main(String[] args) {
        Printable report = new Report("Relatório Financeiro");
        Printable contract = new Contract("Empresa X");

        report.print();
        contract.print();
    }
}
