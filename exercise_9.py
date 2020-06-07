
class Dog():
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog sitting in response to a command
        return self.name.title() + " is now sitting."

    def roll_over(self):
        # Simulate rolling over in response to a command
        return self.name.title() + " rolled over!"

    def math(self, x, y):
        # my dog is smart and can perform simple addition
        result = x + y
        return result


# my_dog = Dog('willie', 6)
# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {str(my_dog.age)} years old.")

# print(my_dog.sit())
# print(my_dog.roll_over())

# my_dog_1 = Dog("shark", 5)
# print(f"{my_dog_1.name.title()}, age {str(my_dog_1.age)} is math literate")
# print("...Proof...")
# result = my_dog_1.math(5, 5)
# print(f"5 + 5 = {result}")

"""
# Try it yourself: classes and objects
# 9-1. Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method
called describe_restaurant() that prints these two pieces of information, and a method called
open_restaurant() that prints a message indicating that the restaurant is open. Make an instance
called restaurant from your class . Print the two attributes individually, and then call both methods.
"""

"""
Q.9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class
you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work;
just pick the one you like better . Add an attribute called flavors that stores a
list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def __repr__(self):
        return f" Object details: {self.restaurant_name}, {self.cuisine_type}, {self.number_served}"

    def describe_restaurant(self):
        return f"{self.restaurant_name.title()} star cuisine is {self.cuisine_type.title()}"

    def open_restaurant(self):
        return f"{self.restaurant_name.title()} is officially open for business"

    def set_number_served(self, update_served):
        if update_served <= self.number_served:
            return f"The current number of customers served is {str(self.number_served)}. It can't be rolled back"
        else:
            self.number_served = update_served
            return f"Total number of customers served = {str(self.number_served)}"
            return

    def increment_number_served(self, increment_served):
        if self.number_served < 0:
            return "You can't input a negative number"
        else:
            self.number_served += increment_served
            return f"Number of serves have been increamented to: {str(self.number_served)}"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self, flavor):
        if self.flavors == []:
            self.flavors = flavor
            print("Flavors:")
            for enu, flavor in enumerate(self.flavors):
                print(f"{enu}. {flavor.title()}")

ice_cream_stand = IceCreamStand("cold stone", "ice cream")
# print(ice_cream_stand)
flavor = ["chocolate", "vanila", "strawberry"]
#ice_cream_stand.display_flavors(flavor)



# instantiating an object
my_restaurant = Restaurant("calabar kitchen", "afang soup with fufu")

# print(f"Restaurant: {my_restaurant.restaurant_name.title()} \nMenu: {my_restaurant.cuisine_type.title()}")

# print(my_restaurant.describe_restaurant())
# print(f"{my_restaurant.open_restaurant()}, please come and enjoy!")
# print(my_restaurant_1.describe_restaurant())

# print(my_restaurant.number_served)
# print(my_restaurant.set_number_served(update_served=5))
# print(my_restaurant.increment_number_served(30))

"""
Q.9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information. Make another
method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

"""
Q.9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) .
Write a method called increment_login_attempts() that increments the value of login_attempts by 1 .
Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 .
Make an instance of the User class and call increment_login_attempts() several times .
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts() .
Print login_attempts again to make sure it was reset to 0.
"""

class User():
    # make sure to change the "programmer" attribute to
    def __init__(self, first_name, last_name, age, occupation, salary, employer):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.email = f"{last_name}{first_name}"
        self.occupation = occupation
        self.age = age
        self.salary = salary
        self.employer = employer
        self.login_attempts = 0

    def describe_user(self):
        description = f"""{self.full_name.title()}, age {self.age} works for {self.employer.title()}
        as an associate {self.occupation.title()} making an annual salary of ${self.salary}. {self.first_name.title()}
        is currently on the data science team at {self.employer.title()}. He can be contacted via email at: {self.email}"""
        return description

    # represent object's information
    def __repr__(self):
         return f"Object: {self.full_name}, {self.email}, {self.occupation}, {self.age}, {self.salary}"

    def greet_user(self):
        return f"Hello {self.full_name.title()}, welcome to {self.employer.title()}!"

    def increment_login_attempts(self, attempt):
        if attempt < 1:
            return "Please check your value"
        else:
            self.login_attempts += attempt
            return self.login_attempts

    def reset_login_attempts(self, attempt):
        if self.login_attempts ==  0:
            return f"Current login attempts = {self.login_attempts}. No reset required"
        else:
            self.login_attempts = attempt
            return f"login attempts reset to {self.login_attempts}."

"""
Q.9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class . Make a Privileges instance as
an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""

class Privilege():
    def __init__(self, priveleges = []):
        self.priveleges = priveleges

    def show_privileges(self, privilege):
        if self.priveleges == []:
            self.privileges = privilege
        print("Privileges:")
        for enu, privilege in enumerate(self.privileges):
            print(f"{enu}. {privilege.title()}")

"""
Q.9-7 An administrator is a special kind of user. Write a class called Admin
that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges()
that lists the administrator’s set of privileges . Create an instance of Admin, and call your method.
"""

class Admin(User):
    def __init__(self, first_name, last_name, age, occupation, salary, employer):
        super().__init__(first_name, last_name, age, occupation, salary, employer)
        self.privilege_access = Privilege()

privilege = ["can add post", "can delete post", "can ban user", "can reprimand user"]

admin = Admin("chidera", "biringa", 23, "data scientist", 105_000, "google")
# admin.show_privileges(privilege)

admin_1 = Admin("chidera", "biringa", 23, "data scientist", 105_000, "google")

#admin_1.privilege_access.show_privileges(privilege)


# print(admin.__repr__())
# user = User("chidera", "biringa", 24, "data scientist", 105_000, "google")
# print(user.__repr__())

# print(user.describe_user())
# print(user.login_attempts)
# print(user.increment_login_attempts(10))
# print(user.reset_login_attempts(0))



# Q.9-13: Ordered dictionaries
from collections import OrderedDict

def ordered_dict():
    rivers_countries = OrderedDict()
    rivers_countries["nile"] = "egypt"
    rivers_countries["amazon"] = "south america"
    rivers_countries["ganges"] = "india"
    rivers_countries["mississippi"] = "united states of america"
    rivers_countries["danube"] = "europe"
    for river, country in rivers_countries.items():
        if river in "mississippi":
            print(f"The {river.title()} river is in the {country.title()}")
        else:
            print(f"The {river.title()} river is in {country.title()}")

# ordered_dict()

# Help available to the variable
# print(dir(rivers_countries))
# help availabe to string
# print(help(str))
# help availabe to specific method to string
# print(help(str.lower))
# print(help(OrderedDict))

"""
# Q.9-14. Dice: The module random contains functions that generate random numbers in a variety of ways.
The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:
"from random import randint" x = randint(1, 6) Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has .
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die . Roll each die 10 times.
"""

from random import randint

class Die():
    """ simulating a roll of a die """
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, 6)
        return f"Random number {x} of a {self.sides} sided die"

    def six_sided_die(self, six_sides):
        if self.sides == six_sides:
            print("A 6-sided die rolled ten times")
            for rolls in range(10):
                six_sides = randint(1, 6)
                print(f"Roll {rolls} = {six_sides}")

    def ten_side_die(self, ten_sides):
        if self.sides != ten_sides:
            print("A 10-sided die rolled ten times")
            for rolls in range(10):
                ten_rand = randint(1, 10)
                print(f"Roll {rolls} = {ten_rand}")

    def twenty_side_die(self, twenty_sides = 20):
        if self.sides != twenty_sides:
            print("A 20-sided die rolled ten times")
            for enu,  _ in enumerate(range(10)):
                twenty_rand = randint(1, 20)
                print(f"Roll {enu} = {twenty_rand}")

# die = Die()
# die.ten_side_die(ten_sides = 10)
# die.twenty_side_die(twenty_sides = 20)
