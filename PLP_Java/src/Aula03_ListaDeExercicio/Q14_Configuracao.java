package Aula03_ListaDeExercicio;

class Q14_Configuracao {
    private static Q14_Configuracao instance;
    private String setting;

    // Construtor privado para impedir a criação de múltiplas instâncias
    private Q14_Configuracao() {
        this.setting = "Configuração padrão";
    }

    // Método estático que retorna a única instância
    public static Q14_Configuracao getInstance() {
        if (instance == null) {
            instance = new Q14_Configuracao();
        }
        return instance;
    }

    // Getters e setters
    public String getSetting() {
        return setting;
    }

    public void setSetting(String setting) {
        this.setting = setting;
    }

    public static void main(String[] args) {
        Q14_Configuracao config1 = Q14_Configuracao.getInstance();
        Q14_Configuracao config2 = Q14_Configuracao.getInstance();

        System.out.println(config1 == config2);
        config1.setSetting("Nova Configuração");
        System.out.println(config2.getSetting());
    }
}


