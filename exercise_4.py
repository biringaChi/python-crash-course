# Try it yourself  - loops and list comprehension
# Q1: Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

def count_twenty():
    result = [count for count in range(21)]
    return result

count_twenty()

"""
 Q2: One Million: Make a list of the numbers from one to one million, and then use a for loop
     to print the numbers . (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window
"""

def one_million():
    result = [count for count in range(1, 1_000_0001)]
    return result

# one_million()

"""
Q3: Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
    to make sure your list actually starts at one and ends at one million . Also, use the sum() function
    to see how quickly Python can add a million numbers .
"""

def summing_a_million():
    result = [count for count in range(1, 1_000_001)]
    stat_combine = [
        (f"min = {min(result)}, max = {max(result)}, sum = {sum(result)}")]
    return stat_combine

# summing_a_million()

"""
 Q4: Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers
     from 1 to 20 . Use a for loop to print each number.
"""

def odd_numbers():
    result = [count for count in range(1, 20, 2)]
    return result

# odd_numbers()

# Q5: Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list
def threes():
    result = [count for count in range(3, 33, 3)]
    return result

# threes()

"""
Q6: Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3
     in Python . Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and
     use a for loop to print out the value of each cube.
"""

def cubes():
    result = list(map(lambda x: x**3, range(1, 11)))
    return result

# cubes()

# Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
def cubes_comprehenstion():
    result = list(map(lambda x: x, range(3, 33, 3)))
    return result

# cubes_comprehenstion()

# Q10
def slice():
    favorite_food = ['Afang soup with fufu', 'Jollof rice, plantain and chicken', 'Roasted plantain, potato',
                     'fish and red oil sauce', 'Native soup and pounded yam', 'Fried rice and beef']
    print("My favorite foods are: ")
    for food in favorite_food[-3:]:
        print(food.title())

# slice()

# Q11
def pizza():
    pizzas = ["Beef", "Chicken", "Hotdog"]
    friend_pizzas = pizzas[:]
    total_pizza = zip(pizzas, friend_pizzas)
    print("My favorite and friend's pizzas are:")
    for pizza, friend_pizza in total_pizza:
        print(f"{pizza}-------\t {friend_pizza}")

#pizza()

# Q12: Use a for loop to print each food the restaurant offers.
def restaurant():
    menu = ("rice", "beef", "sauce", "cake", "vegetables")
    new_menu = ("chinese rice", "beef", "sauce", "cake", "sharwama")
    for food in new_menu:
        print(food.title())

#restaurant()
