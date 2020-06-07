# Try It Yourself: Conditional Test
# Q1
def conditional_test():
    pen_type = 'black ink'
    print("Is pen_type ==  'black ink'? I predict True.")
    print(pen_type == "black ink")
    print("\nIs pen_type == 'blue ink'? I predict False")
    print(pen_type == "blue ink")

#conditional_test()

# Q2: Alien Color
alien_color = ["green", "yellow", "red"]

def alien_v1(arg):
    if "green" in alien_color:
        points = 5
        print(f"You just earned {str(points)} points.")
    elif "green" not in alien_color:
        print(f"No points earned")

#alien_v1(alien_color)

# Version that doesn't pass the test
def alien_v2(alien_color):
    if "green" not in alien_color:
        points = 5
    elif "green" in alien_color:
        points = 5
#alien_v2(alien_color)

# Q3 Alien Color
alien_color2 = "red"
def alien_v3(arg):
    if "green" in alien_color2:
        points = 5
        print(f"You just earned {str(points)} points.")
    if "green" not in alien_color2:
        points = 10
        print(f"You just earned {str(points)} points.")

#alien_v3(alien_color2)

# With an else statement
alien_color3 = "green"
def alien_v4(arg):
    if "green" in alien_color3:
        points = 5
        print(f"You just earned {str(points)} points.")
    else:
        points = 10
        print(f"You just earned {str(points)} points.")

#alien_v4(alien_color3)

alien_color5 = "red"
def alien5(arg):
    if "green" in alien_color5:
        points = 5
        print(f"You just earned {str(points)} points.")
    elif "yellow" in alien_color5:
        points = 10
        print(f"You just earned {str(points)} points.")
    elif "red" in alien_color5:
        points = 15
        print(f"You just earned {str(points)} points.")

#alien5(alien_color5)

def alien5_v2():
    alien_color5 = "yellow"
    if alien_color5 == "red":
        points = 15
        print(f"You just earned {str(points)} points.")
    if alien_color5 == "green":
        points = 5
        print(f"You just earned {str(pints)} points.")
    if alien_color5 == "yellow":
        points = 10
        print(f"You jus earned {str(points)} {alien_color5.upper()} points")

#alien5_v2()

def alien5_v3():
    alien_color5 = "green"
    if alien_color5 == "red":
        points = 15
        print(f"You just earned {alien_color5.upper()} {str(points)} points.")
    elif alien_color5 == "yellow":
        points = 10
        print(f"You just earned {alien_color5.upper()} {str(points)} points.")
    else:
        points = 5
        print(f"You just earned {alien_color5.upper()} {str(points)} points.")

#alien5_v3()


# Q6
def life_stages():
    age = 30
    if age < 2:
        print("You are a baby")
    elif age < 4:
        print("You are a toodler")
    elif age < 13:
        print("You are a kid")
    elif age < 20:
        print("You are a teenager")
    elif age < 65:
        print("You are an adult")
    elif age >= 65:
        print("You are an elder")
    else:
        print("You are an alien")

#life_stages()

"""
Q7
  Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements
  that check for certain fruits in your list. Make a list of your three favorite fruits and call it favorite_fruits .
   Write five if statements . Each should check whether a certain kind of fruit is in your list .
 If the fruit is in your list, the if block should print a statement, such as You really like bananas!
"""

def tasty_fruits():
    fruits = ["guava", "orange", "apple", "mango", "tangerin", "banana"]
    if "guava" in fruits:
        print("Guava is available")
    if "orange" in fruits:
        print("Orange is available")
    if "apple" in fruits:
        print("Apple is available")
    if "mango" in fruits:
        print("Mango is available")
    if "tangerin" in fruits:
        print("Tangerin is available")
    if "banana" in fruits:
        print("Banana is available")

#tasty_fruits()

def favorite_fruits():
    fruits = ["guava", "banana", "mango"]
    if "guava" in fruits:
        print("You really like guavas!")
    if "banana" in fruits:
        print("You really like bananas!")
    if "mango" in fruits:
        print("You really like mangos!")

#favorite_fruits()


#Q1: Hello Admin
usernames = ["adam", "eve", "abraham", "isaac", "jacob", "sampson", "elijah", "admin"]
def website_login(names):
    for username in usernames:
        if "admin" in username:
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again")

#website_login(usernames)

# Q2: No Users
del usernames[:]
def no_users(names):
    if usernames:
        print("We have users")
    else:
        print("We need to find some users")

#no_users(usernames)

# Q3: Checking usernames
current_users = ["cbiringa", "bug", "sourcebox", "virus", "malignant", "attack"]
new_users = ["trapezoid", "circle", "Cbiringa", "Triangle", "sourcebox", "rectangle"]
def check_usernames(arg1, arg2):
    for new_user in new_users:
        new_user = new_user.lower()
        if new_user in current_users:
            print(f"{new_user} is already in use. Please pick another username")
        else:
            print(f"{new_user} is available")

#check_usernames(current_users, new_users)

"""
 Q4: Ordinal Numbers
 Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .
 Store the numbers 1 through 9 in a list .
 Loop through the list .
 Use an if-elif-else chain inside the loop to print the proper ordinal end- ing for each number . Your output should read "1st 2nd 3rd
 4th 5th 6th 7th 8th 9th", and each result should be on a separate line .
"""

numbers = [number for number in range(1, 10)]
def ordinal_numbers(arg):
    for number in numbers:
        if number == 1:
            print(f"This is the {number}st number")
        elif number == 2:
            print(f"This is the {number}nd number")
        elif number == 3:
            print(f"This is the {number}rd number")
        elif number == 3:
            print(f"This is the {number}rd number")
        elif number == 4:
            print(f"This is the {number}th number")
        elif number == 5:
            print(f"This is the {number}th number")
        elif number == 6:
            print(f"This is the {number}th number")
        elif number == 7:
            print(f"This is the {number}th number")
        elif number == 8:
            print(f"This is the {number}th number")
        elif number == 9:
            print(f"This is the {number}th number")
        elif number == 10:
            print(f"This is the {number}th number")
        else:
            print(f"{number} is not available")

#ordinal_numbers(numbers)

