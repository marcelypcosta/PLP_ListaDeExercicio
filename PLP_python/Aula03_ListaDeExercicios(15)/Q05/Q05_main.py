from Q05_dog import Dog
from Q05_cat import Cat


def make_sounds(animals):
    """
    Receives a list of Animal objects and calls the make_sound method of each one.

    Args:
        animals (list): List of Animal objects.
    """
    for animal in animals:
        animal.make_sound()


def main():
    dog = Dog()
    cat = Cat()
    animals = [dog, cat]

    make_sounds(animals)


if __name__ == "__main__":
    main()
