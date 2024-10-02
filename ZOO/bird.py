from abc import ABC

from animal import Animal


class Bird(Animal):
    """
    the class bird inherit from animal.
    """
    pass

    def __init__(self, color: str, bird_type: str):
        super().__init__()
        self._color = color
        self._bird_type = bird_type

    """
    the constructor with the 2 PROTECTED attributes: color and bird_type.
    """

    def move(self, distance: float) -> None:
        print(f" The bird flies for {distance} meters")

    def get_number_of_legs(self) -> int:
        return 2

    """
    :return the number of legs of the bird(2).
    """

    def print_details(self) -> None:
        print(f"Bird {self.get_id()} is of type {self._bird_type} and its color is {self._color}.")


"""
The Bird class implements the 2 abstract methods of Animal
move and print details.

"""

"""
Guidelines:
1. The Bird class inherits from Animal class.
2. The Bird class receives 2 parameters in its' constructor:
    * color is string.
    * bird_type is string.
3. The Bird class has 2 PROTECTED attributes: color and bird_type.
4. The Bird class implements the 2 abstract methods of Animal:
    4.1 move - receives a single float parameter `distance`, 
             * prints the following message:
                The bird flies for <distance> meters
             * Where:
                * <distance> - should be the distance received parameter.
    4.2 get_number_of_legs- receives no parameters and returns the number of legs of the bird (2) as an integer.
    4.3 print_details - receives no parameters, prints data for the bird:
            * The method prints the following text:
                Bird #<id> is of type <bird_type> and its color is <color>.
            * Where:
                * <id> - should be the bird's id (use get_id method)
                * <bird_type> - should be the bird's type
                * <color> - should be the bird's color.
5. Make sure you add type hints and documentation to the class and to all its' methods!

---
Task 3.1
---
Create bird.py file with the Bird class according to the guidelines above.

"""
