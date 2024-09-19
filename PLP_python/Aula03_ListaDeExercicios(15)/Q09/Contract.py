from abc import ABC, abstractmethod

class Printable(ABC):
    """
    Abstract class that defines the interface for printable objects.
    """
    @abstractmethod
    def print(self) -> None:
        """
        Abstract method to print the details of the object.
        Must be implemented in classes that inherit from Printable.
        """
        pass

class Report(Printable):
    """
    Class representing a report and implementing the Printable interface.
    """
    def __init__(self, title: str):
        """
        Initializes a new report with the provided title.
        """
        self.title = title

    def print(self) -> None:
        """
        Prints the title of the report.
        """
        print("Printing report: {}".format(self.title))

class Contract(Printable):
    """
    Class representing a contract and implementing the Printable interface.
    """
    def __init__(self, party_name: str):
        """
        Initializes a new contract with the name of the involved party.
        """
        self.party_name = party_name

    def print(self) -> None:
        """
        Prints the name of the party involved in the contract.
        """
        print("Printing contract with: {}".format(self.party_name))

if __name__ == "__main__":
    report = Report("Financial Report")
    contract = Contract("Company X")

    report.print()
    contract.print()
