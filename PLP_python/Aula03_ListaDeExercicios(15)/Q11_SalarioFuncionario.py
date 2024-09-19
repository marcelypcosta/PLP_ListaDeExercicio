from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class FuncionarioAssalariado(Funcionario):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

if __name__ == "__main__":
    horista = FuncionarioHorista("João", 50, 160)
    assalariado = FuncionarioAssalariado("Maria", 3000)

    print("Salário de João: R$ {}".format(horista.calculate_salary()))
    print("Salário de Maria: R$ {}".format(assalariado.calculate_salary()))
