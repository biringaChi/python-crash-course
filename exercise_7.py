"""
Accepting inputs
Q.7-1. Rental Car: Write a program that asks the user what kind of rental car they would like .
Print a message about that car, such as “Let me see if I can find you a Subaru .”
"""

def rental_car():
    car = input("What kind of rental car would you like?\nResponse: ")
    print(f"Let me see if I can find you that {car}")

#rental_car()

"""
Q.7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group .
If the answer is more than eight, print a message saying they’ll have to wait for a table . Otherwise, report that their table is ready .
"""

def restaurant():
    dinner = input("How many people are in your dinner group?\nResponse: ")
    dinner = int(dinner)
    if dinner > 8:
        print("Sorry, but you would have to wait for a table")
    else:
        print("Your table is ready")

#restaurant()

# Q.7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .

def multiple_10():
    ten = input("Please input a number: ")
    ten = int(ten)
    if ten % 10 == 0:
        print(f"The number {ten} is a multiple of ten")
    else:
        print(f"The number {ten} is not a multiple of ten")

# multiple_10()

"""
Q.7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value .
As they enter each topping, print a message saying you’ll add that topping to their pizza .
"""

prompt = "(Enter 'quit' when you are finished to exit)"
prompt += "\nPlease enter a pizza topping: "

def pizza_toppings(arg):
    active = True
    while active:
        toppings = input(prompt)
        if toppings == "quit":
            active = False
            print("You just exited")
        else:
            print(f"{toppings.title()} will be added to your pizza")

# pizza_toppings(prompt)

"""
Q.7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age .
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15 . Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
"""

prompt = "Please enter your age: "

def movie_tickets(arg):
    active = True
    while active:
        age = int(input(prompt))
        if age < 3:
            print("Your ticket is free!")
            active = False
        elif age < 12:
            price = 10
            print(f"Your ticket is {str(price)}$")
            active = False
        elif age >= 12:
            price = 15
            print(f"Your ticket is {str(price)}$")
            active = False

#movie_tickets(prompt)

"""
Q.7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
Use a conditional test in the while statement to stop the loop .
Use an active variable to control how long the loop runs .
Use a break statement to exit the loop when the user enters a 'quit' value
"""

def movie_tickets1():
    while True:
        age = int(input(prompt))
        if age < 3:
            print("Your ticket is free!")
            break
        elif age < 12:
            price = 10
            print(f"Your ticket is {str(price)}$")
            break
        elif age >= 12:
            price = 15
            print(f"Your ticket is {str(price)}$")
            break

#movie_tickets1()

# Infinity loop
def infinity():
    number = 1
    while number < 10:
        print("One is less than Ten")

# infinity()

# Try it yourself: While loops in list and dictionaries

"""
Q.7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches . Then make an empty list called finished_sandwiches .
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
move it to the list of finished sandwiches . After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

"""
Q.7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ["french dip", "pastrami",  "sloppy joe", "pastrami", "cheesesteak", "tuna", "pastrami", "chicken"]
finished_sandwiches = []

def deli(arg_0, arg_1):
    print(f"The deli has run out of {sandwich_orders[1].title()}'s")
    while sandwich_orders:
        while "pastrami" in sandwich_orders:
            sandwich_orders.remove("pastrami")
        current_sandwich = sandwich_orders.pop()
        print(f"I made you a {current_sandwich.title()} sandwich")
        finished_sandwiches.append(current_sandwich.title())
    print("\nFinished sandwiches: ")
    for enu, sandwich, in enumerate(finished_sandwiches):
        print(f"{enu}. {sandwich} sandwich")

#deli(sandwich_orders, finished_sandwiches)

"""
Q.7-10. Dream Vacation: Write a program that polls users about their dream vacation . Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll .
"""

def dream_vacation(users_poll):
    active = True
    while active:
        users_name = input("What is your name? ")
        users_visits = input("If you could visit one place in the world, where would you go? ")
        users_poll[users_name] = users_visits
        repeat_action = input("Would you like to make another reponse? \n Please enter (y/n) ")
        if "n" in repeat_action:
            active = False
    print("\nPolling results...")
    for names, visits in users_poll.items():
        print(f"{names.title()} would love to visit {visits.title()}")

#dream_vacation(users_poll = {})
