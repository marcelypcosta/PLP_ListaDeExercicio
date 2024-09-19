package Aula03_ListaDeExercicio.Q09;

public class Contract implements Printable{
    private String partyName;

    public Contract(String partyName) {
        this.partyName = partyName;
    }

    @Override
    public void print() {
        System.out.println("Imprimindo contrato com: " + partyName);
    }
}
