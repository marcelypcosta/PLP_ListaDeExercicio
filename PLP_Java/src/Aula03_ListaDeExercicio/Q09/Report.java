package Aula03_ListaDeExercicio.Q09;

public class Report implements Printable {
    private String title;

    public Report(String title) {
        this.title = title;
    }

    @Override
    public void print() {
        System.out.println("Imprimindo relatório: " + title);
    }
}
