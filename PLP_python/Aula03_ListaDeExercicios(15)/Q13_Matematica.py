class Q013_Matematica:

    @staticmethod
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * Q013_Matematica.fatorial(n - 1)


if __name__ == "__main__":
    print("O fatorial de 5 é: {}".format(Q013_Matematica.fatorial(5)))
    print("O fatorial de 0 é: {}".format(Q013_Matematica.fatorial(0)))
