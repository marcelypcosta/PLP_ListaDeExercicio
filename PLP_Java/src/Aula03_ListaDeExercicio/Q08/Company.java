package Aula03_ListaDeExercicio.Q08;

import java.util.ArrayList;
import java.util.List;

public class Company {
    private String companyName;
    private List<Employee> employees;

    public Company(String companyName) {
        this.companyName = companyName;
        this.employees = new ArrayList<>();
    }

    public void addEmployee(Employee employee) {
        employees.add(employee);
    }

    public void showEmployees() {
        System.out.println("Employees of " + companyName + ":");
        for (Employee employee : employees) {
            System.out.println(employee.getName() + " - " + employee.getPosition() + " - R$" + employee.getSalary());
        }
    }

    public static void main(String[] args) {
        Company company = new Company("Tech Solutions");

        Employee employee1 = new Employee("Alice", "Developer", 5000);
        Employee employee2 = new Employee("Bob", "Designer", 4000);

        company.addEmployee(employee1);
        company.addEmployee(employee2);

        company.showEmployees();
    }
}
