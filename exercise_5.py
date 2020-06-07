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
