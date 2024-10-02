"""
Home Assignment #1 - Advance Python
"""

###################################
# General Guidelines
###################################
"""
In this Homework assignment we will use Python (and OOP in Python) to maintain a list of animals,
and perform various operations on the list.

Guidelines:
    - After completing each part, you should be able to run the program and test your results (so far).
    - Your program MUST run (if it will not, you will lose points).
    - You can use the code from the lectures and recitations as a base line.
    - Make sure to add home_assignment_1.pydocumentation - as we saw in class.
    - Keep a clean code.
"""

###################################
# The Assignment
###################################
"""
The assignment contains 3 files:
- home_assigment_1.py - 
    This file - contains guidelines and the task description.
- hw1_main.py - 
    - Contains the main file that you will run.
    - Make sure to run it after you complete each part.
    - Change ONLY the parts you are asked to change or add code to.

"""

###################################
# Part 0 - Personal Details
###################################
"""
In hw1_main.py print the id, name and email of the submitters.
Replace the details in the "Part 0 - Personal Details" section.
"""

###################################
# Part 1 - The Animal class
###################################
"""
---
Task 1.0 (nothing to do - only read!)
---
The animal class represents a general animal.

In the file animal.py - create an Abstract Class - and call it Animal (already done for you).

Note: 
The constructor for the class was already built for you (you will change its body later in this assigment).
Make sure you do not change its signature.

---
Task 1.1
---
Add documentation for the class.

---
TASK 1.2
---
Add 3 ABSTRACT methods to the class:
- move - receives a single float parameter `distance`, returns nothing.
- get_number_of_legs - receives no parameters, returns the number of legs of the animal as integer.
- print_details - receives no parameters, prints data for the animal.

Make sure you add type hints and documentation to all the methods!
"I DO"
"""

###################################
# Part 2 - The Dog
###################################
"""
---
Task 2.0 (nothing to do - only read!)
---
In the file dog.py - create a class - and call it Dog (already done for you).

---
Task 2.1
---
Add documentation for the Dog class.

---
Task 2.2
---
Make Dog inherit from Animal.
"I DO"
---
Task 2.3
---
Add a constructor to Dog class:
- Call the super class constructor.
- The constructor should receive 2 parameters: 
    * owner_name is string.
    * age is an integer.
- The constructor should declare 2 PROTECTED attributes: owner_name and age.
  *###*Those attributes are initialized using the received parameters.
- Make sure you add type hints and documentation to the constructor.
" I DO"
---
Task 2.4
---
Implement the move abstract method:
- move - receives a single float parameter `distance`, 
         prints the following message:
            <owner_name> walks with the dog for <distance> meters
         Where:
            * <owner_name> - should be the Dog's owner name
            * <distance> - should be the distance received parameter.

---
Task 2.5
---
Implement the get_number_of_legs abstract method:
- get_number_of_legs - receives no parameters and returns the number of legs of the dog (4) as an integer.

---
Task 2.6
---
- print_details - receives no parameters, prints data for the dog:
    * The method prints the following text:
        Dog #<id> is <age> years old and is owned by <owner_name>.
    * Where:
        * <id> - should be the dog's id (use get_id method)
        * <age> - should be the dog's age
        * <owner_name> - should be the Dog's owner name
        "I DO"
"""

###################################
# Part 3 - The Bird
###################################
"""
In this part you will create the Bird class.

In the file - bird.py - you should create the Bird class (you can and should change the existing code).

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
"I DO"
###################################
# Part 4 - Animal ID
###################################
"""
In this task you will add the animal's ID part.

The task is to make sure each animal is created with a unique (int) ID,
and this id is generated automatically by the Animal's class constructor.

---
Task 4.1
---
Change the constructor of Animal so each animal is created with a unique integer ID.
    IMPORTANT NOTES:
    - You are NOT allowed to add parameters to the constructor!!
    - You must have an attribute "self._animal_id" in class Animal.
    - You can (and SHOULD) add static member to the Animal class.
    - You can (and should) add code in the BODY of __init__ method (constructor) of Animal.
"""

###################################
# Part 5 - HW1 main
###################################
"""
In this part you will create a small program that receives input from the user.
Based on the input the program will maintain a list of animals and will be able to print data on the list.

In every iteration - the program will ask the user for a command.

you will code this part in "hw1_main.py".

Note that the main loop and the program's skeleton were already written for you.
You have to fill the code based on the commands list below.

You will see the:
    # Your code goes here
comment in every place you need to add code.

Possible commands and what the program should do:
1. "dog" - 
    * The program will ask the user for the dog's owner name, with the following message:
        Please insert the owner name of the dog
    * The program will ask the user for the dog's age, with the following message:
        Please insert the age of the dog.
    * The program will create a new dog with the received owner name and age, and will add it to the list.
2. "bird" - 
    * The program will ask the user for the bird's color, with the following message:
        Please insert the color of the bird.
    * The program will ask the user for the bird's type, with the following message:
        Please insert the type of the bird
    * The program will create a new bird with the received color and type, and will add it to the list.
***3. "print" -
    * The program will print all the animals in the list, using the "print_details" method.
4. "move" - 
    * The program will ask the user for the distance to move, with the following message:
        Please insert the distance to move
    * The program will move all the animals in the list, using the "move" method and the received distance.
***5. "avg_legs" - 
    * The program will print the AVERAGE number of the legs of all the animals in the list:
        The average number of legs is <avg_legs>.
        
        * Where:
            - <avg_legs> - is the average number of the legs of all the animals in the list
***6. "remove" -
    * The program will ask the user for the id of the animal to remove:
        Please insert the id of the animal you want to remove.
    **** If an animal with such id exists in the list, the program will remove it from the list,
      and will print:
        Animal #<id> was removed from the list.
        
        * Where:
            - <id> - is the id of the removed animal.
    * If an animal with such id doesn't exist in the list, the program print:
        Animal #<id> was not found in the list.
        
        * Where:
            - <id> - is the id that was not found.
7. "exit" - 
    ALREADY DONE FOR YOU!
    * The program will break the loop.
8. Any other command - 
    ALREADY DONE FOR YOU!
    * The program will print an error message - and ask the user for a valid command.
"""

###################################
# GOOD LUCK
###################################
"""
GOOD LUCK!!!
"""
