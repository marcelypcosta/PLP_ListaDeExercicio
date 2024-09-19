package Aula03_ListaDeExercicio.Q12_Conveniencia;

class Produto {
    private String name;
    private double price;

    public Produto(String name, double price) {
        this.name = name;
        this.price = price;
    }

    // Método que soma o preço de dois produtos
    public double sumPrices(Produto other) {
        return this.price + other.price;
    }

    // Getter para o nome do produto
    public String getName() {
        return name;
    }

    // Getter para o preço do produto
    public double getPrice() {
        return price;
    }
}
