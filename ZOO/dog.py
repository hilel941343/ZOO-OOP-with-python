from animal import Animal


class Dog(Animal):
    """
   the class dog inherit from animal.
    """
    pass

    def __init__(self, owner_name: str, age: int):

        """
        setting of constructor:
        :param owner_name: the owner name of the dog
        :param age: the age of the dog
        """
        super().__init__()
        """
        calling the  super class constructor.
        """
        self._owner_name = owner_name
        self._age = age

        """
        declaring 2 PROTECTED attributes: owner_name and age.
        """

    def move(self, distance: float) -> None:
        print(f" {self._owner_name} walks with the dog for {distance} meters")

    """
        implement of method move (print the distance that owner walks with the dog).
    """

    def get_number_of_legs(self) -> int:
        return 4
    """
    :return the number of legs of the dog (4).
    """

    def print_details(self) -> None:
        print(f" Dog {self.get_id()} is {self._age} years old and is owned by {self._owner_name}.")
    """
    print method is print the details of dog(the id,the age,the owner name)
"""

    """ 
    Add a constructor to Dog class:
- Call the super class constructor.
- The constructor should receive 2 parameters: 
    * owner_name is string.
    * age is an integer.
- The constructor should declare 2 PROTECTED attributes: owner_name and age.
  Those attributes are initialized using the received parameters.
- Make sure you add type hints and documentation to the constructor.
    """
