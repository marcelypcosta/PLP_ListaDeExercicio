class Employee:
    """
    Represents an employee with name, position, and salary.
    """
    def __init__(self, name, position, salary):
        """
        Initializes the employee with name, position, and salary.
        """
        self.name = name
        self.position = position
        self.salary = salary


class Company:
    """
    Represents a company that aggregates a list of employees.
    """
    def __init__(self, company_name):
        """
        Initializes the company with a name and an empty list of employees.
        """
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        """
        Adds an employee to the company.
        """
        self.employees.append(employee)

    def show_employees(self):
        """
        Displays the details of all employees working at the company.
        """
        print("Employees of {}:".format(self.company_name))
        for employee in self.employees:
            print("{} - {} - R${}".format(employee.name, employee.position, employee.salary))


if __name__ == "__main__":
    company = Company("Tech Solutions")

    employee1 = Employee("Alice", "Developer", 5000)
    employee2 = Employee("Bob", "Designer", 4000)

    company.add_employee(employee1)
    company.add_employee(employee2)

    company.show_employees()
