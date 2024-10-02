from typing import List

from animal import Animal
from dog import Dog
from bird import Bird

###################################
# Part 0 - Personal Details
###################################
print("318143062")
print("Hillel Touitou")
print("hilel941343@gmail.com")

print("207319484")
print("Dvir Gamliel")
print("dvirg1998@gmail.com")

###################################
# Part 5.1 - HW1 main
###################################

print("Welcome to advanced python course - HW 1 - ANIMALS and FUN")

"""
The animals list
"""
animals_list: List[Animal] = []
"""
The main loop
"""
while True:
    command = input("please enter a command: ")

    if command == "dog":
        pass
        """
                             Receive owner_name
        """
        owner_name = input("Please insert the owner name of the dog: ")
        """
                           Receive age
        """
        age_dog = int(input("Please insert the age of the dog: "))

        # Your code goes here
        """
        Create a new Dog object, and add it to the Animals' list. 
        """
        new_dog = Dog(owner_name, age_dog)
        animals_list.append(new_dog)

    elif command == "bird":
        pass
        """
          Receive color from the user
        """
        color = input(" Please insert the color of the bird: ")
        """
        Receive bird type from the user
        """
        bird_type = input("  Please insert the type of the bird: ")

        """
        Create a new Bird object, and add it to the Animals' list. 
        """
        new_bird = Bird(color, bird_type)
        animals_list.append(new_bird)

    elif command == "print":
        pass
        """
        Prints all the animals in the list, using the "print_details" method.
        """
        for animal in animals_list:
            animal.print_details()

    elif command == "move":
        pass
        """
               Receives distance from the user
        """
        distance = float(input("Please insert the distance to move: "))
        """
        Call `move` method for all the animals in the list.
        """
        for animal in animals_list:
            animal.move(distance)

    elif command == "avg_legs":
        pass
        """
        Prints the AVERAGE number of the legs of all the animals in the list.
        """
        sum_legs = sum(animal.get_number_of_legs() for animal in animals_list)
        sum_animals = len(animals_list)

        if sum_animals > 0:
            avg_legs = sum_legs / sum_animals
        else:
            avg_legs = 0
        print(f"The average number of legs is {avg_legs}.")

    elif command == "remove":
        pass
        """
           Receive the id of the animal to remove from the user
        """
        animal_id = int(input("Please insert the id of the animal you want to remove:"))
        removed_animal = None
        for animal in animals_list:
            if animal.get_id() == animal_id:
                animals_list.remove(animal)
                removed_animal = animal
                print(f"Animal #{animal_id} was removed from the list.")
                break

            if removed_animal is None:
                print(f"Animal #{animal_id} was not found in the list.")

    elif command == "exit":
        break
    else:
        print(f"Sorry! The command {command} is unknown. Please try again.")

print("Thank you for using ANIMALS and FUN!")