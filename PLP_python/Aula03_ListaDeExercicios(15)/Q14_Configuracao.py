class Q014_Configuracao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Q014_Configuracao, cls).__new__(cls)
            cls.setting = "Configuração padrão"
        return cls._instance

if __name__ == "__main__":
    config1 = Q014_Configuracao()
    config2 = Q014_Configuracao()

    print(config1 is config2)
    config1.setting = "Nova Configuração"
    print(config2.setting)
