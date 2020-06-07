"""
Working with files
Q.10-1. Learning Python: Open a blank file in your text editor and write
a few lines summarizing what you’ve learned about Python so far.
Start each line with the phrase In Python you can. Save the file as learning_python.txt
in the same directory as your exercises from this chapter. Write a program that reads the file and prints
what you wrote three times . Print the contents once by read- ing in the entire file, once by looping over the file object,
and once by storing the lines in a list and then working with them outside the with block.

# Q.10-2. Learning C: You can use the replace() method to replace any word in a string with a different word.
# Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
"""

class Files():
    """ Working with files """

    def __init__(self, file_name, file_format):
        self.file_name = file_name
        self.file_format = file_format


    def __repr__(self):
        return f"file name: {self.file_name} \nfile format: {self.file_format}"

    def files(self, filename):
        with open(filename, "r") as file_objects:
            file_details = file_objects.readlines()
        for _ in range(3):
            print()
            for file_detail in file_details:
                file_detail = file_detail.strip()
                return(file_detail)

    def learning_c(self):
        value = self.files(filename)
        if value is not None:
            result = value.replace("python", "C")
            print(result)



filename = "data_files/learning_python.txt"
file = Files("learning python", "txt")


import json

"""
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file. Write a separate program that reads
in this value and prints the message, “I know your favorite number! It’s _____ .”
"""

class FavoriteNumber():
    """ a program that prompts for the user’s favorite number """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Object: {self.name}"

    def get_new_favorite_number(self):
        """gets favorite number"""
        favorite_number = input('What is your favorite number? ')
        filename = "data_files/favorite_number.json"
        with open(filename, "w") as file_objects:
            json.dump(favorite_number, file_objects)
        return favorite_number

    def get_stored_favorite_number(self):
        """gets stored user's favorite_number if it doesn't exist"""
        filename = "data_files/favorite_number.json"
        try:
            with open(filename) as file_objects:
                favorite_number = json.load(file_objects)
        except FileNotFoundError:
            return None
        else:
            return favorite_number

    def acknowledge_favorite_number(self):
        """authenticates favorite number"""
        favorite_number = self.get_stored_favorite_number()
        if favorite_number:
            verification = input(f"Is {favorite_number} your favorite number? \n(please enter 'yes/no'): ")
            if verification == "yes":
                print(f"Welcome back, your favorite_number is {favorite_number}")
            elif verification == "no":
                print("Sorry, please provide further details below")
                favorite_number = self.get_new_favorite_number()
                print(f"Your favorite number {favorite_number} will be remembered next time")
            elif verification not in "yes" or "no":
                verification_denied = verification
                print(f"Please provide a 'yes/no' response, not '{verification_denied}'")
        else:
            favorite_number = self.get_new_favorite_number()
            print(f"Your favorite number {favorite_number} has been stored!")

# favorite_check = FavoriteNumber("favorite number")
# favorite_check.acknowledge_favorite_number()
