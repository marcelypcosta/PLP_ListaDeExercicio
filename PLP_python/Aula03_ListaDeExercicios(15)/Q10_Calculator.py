class Q10_Calculator:
    def sum_two(self, a: int, b: int) -> int:
        """
        Sums two numbers.
        """
        return a + b

    def sum_three(self, a: int, b: int, c: int) -> int:
        """
        Sums three numbers.
        """
        return a + b + c

if __name__ == "__main__":
    calculator = Q10_Calculator()

    result1 = calculator.sum_two(10, 20)
    print("Sum of two numbers:", result1)

    result2 = calculator.sum_three(10, 20, 30)
    print("Sum of three numbers:", result2)
