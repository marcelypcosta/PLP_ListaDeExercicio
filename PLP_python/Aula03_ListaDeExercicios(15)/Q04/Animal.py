class Animal:
    """
    Base class representing an Animal.
    """

    def make_sound(self):
        """
        Prints the sound of the animal.
        """
        raise NotImplementedError("Subclasses must implement this method.")
