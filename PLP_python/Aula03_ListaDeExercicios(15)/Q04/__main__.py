from Dog import Dog
from Cat import Cat

def main():
    animal1 = Dog()
    animal2 = Cat()

    animal1.make_sound()  # Output: Woof!
    animal2.make_sound()  # Output: Meow!

if __name__ == "__main__":
    main()
