import abc


class Animal(abc.ABC):
    """
    the class "animal"  inherit from abstract  class
    """

    _id_counter = 0

    def __init__(self):
        Animal._id_counter += 1
        self._animal_id = Animal._id_counter

    """
        static to id's
        """

    def get_id(self) -> int:
        """
        Returns the animal's id.
        :return: Returns the animal's id.
        """
        return self._animal_id

    @abc.abstractmethod
    def move(self, distance: float) -> None:
        pass

    @abc.abstractmethod
    def get_number_of_legs(self) -> int:
        pass

    """
    return:return the number of legs of the animal.
    """

    @abc.abstractmethod
    def print_details(self) -> None:
        pass

    """
    print the data of the animal.
    """
    """
   Add 3 ABSTRACT methods to the class:
    - move - receives a single float parameter `distance`, returns nothing.
    - get_number_of_legs - receives no parameters, returns the number of legs of the animal as integer.
    - print_details - receives no parameters, prints data for the animal.
"""
