# Try it Yourself: Dictionary
# Q.6-1
divine = {
            "first_name" : "divine",
            "last_name" : "biringa",
            "age" : 21,
            "city" : "Ontario",
               }

def divine_dict(arg):
    for key in last_child:
        print(f"Value: {key.title()}")

# divine_dict(last_child)

"""
Q.6-2: Favorite numbers
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number. For even more fun, poll a few friends
and get some actual data for your program
"""
names_numbers = {}
names_numbers["mike"] =  10
names_numbers["james"] = 6
names_numbers["john"] = 1
names_numbers["veronica"] = 8
names_numbers["gabriel"] = 11

def favorite_numbers(arg):
    for name, number in names_numbers.items():
        print(f"Names: {name.title()}, Favorite Number: {number}")

#favorite_numbers(names_numbers)

# Q.6-4: Major rivers and countries.
rivers_countries = {
    "nile" : "egypt",
    "amazon" : "south america",
    "ganges" : "india",
    "mississippi" : "united states of america",
    "danube" : "europe"
}

def river_location(arg):
    for river in sorted(rivers_countries.keys()):
        if "nile" in river:
            print(f"The {river.title()} river is the longest river in the world.")
        elif "amazon" in river:
            print(f"The {river.title()} river is the second largest river in the world.")
        elif "ganges" in river:
            print(f"The {river.title()} river flows through India and Bangladesh.")
        elif "mississippi" in river:
            print(f"The {river.title()} river is the second-longest river and chief river of the second-largest \
              drainage system on the North American continent.")
        elif "danube" in river:
            print(f"The {river.title()} river is Europe's second longest river, after the Volga.")

#river_location(rivers_countries)

# River Names
def river_names(arg):
    for river_name in sorted(rivers_countries.keys()):
        print(f"Name of River: {river_name.title()}")

#river_names(rivers_countries)

# Country Names
def country_names(arg):
    for country_name in set(rivers_countries.values()):
        print(f"Name of Country: {country_name.title()}")

#country_names(rivers_countries)

"""
Loop through the list of people who should take the poll .
If they have already taken the poll, print a message thanking them for responding .
If they have not yet taken the poll, print a message inviting them to take the poll .
"""

friends = ["phil", "sarah", "chi", "russell"]

favorite_languages = {"jen" : "python",
                      "sarah": "c",
                      "edward": "ruby",
                      "phil": "python",
                      }
def polling(arg1, arg2):
    for friend in friends:
        if friend in favorite_languages.keys():
            print(f"Thank you {friend.title()}, you have taken the poll!")
        elif friend not in favorite_languages.keys():
            print(f"You haven't taken the pool {friend.title()}")

#polling(friends, favorite_languages)

"""
Try it yourself: Nesting
Q.6-7. People
Start with the program you wrote for Exercise 6-1 (page 102) .
Make two new dictionaries representing different people, and store all three dictionaries in a list called people .
Loop through your list of people . As you loop through the list, print everything you know about each person .
"""

onyema = {"first_name" : "Onyema", "last_name" : "Biringa", "age" : 59, "city": "Port Harcourt"}
chinwe = {"first_name" : "Chinwe", "last_name" : "Biringa", "age" : 51, "city" : "Port Harcourt"}
divine = {"first_name" : "Divine", "last_name" : "Biringa", "age" : 21, "city" : "Ontario"}
family = [onyema, chinwe, divine]

def people(arg):
    for family_member in family:
        for member_key, member_value in family_member.items():
            print(f"{member_key.title()} : {member_value}")
#people(family)


# Q.6-8 Pets
noise = {"name" : "parrotty", "kind" : "bird", "owner_name" : "doug valentino"}
doggie = {"name" : "sharky", "kind" : "dog", "owner_name" : "biringa chidera"}
fishy = {"name" : "gill", "kind" : "fish", "owner_name" : "sandy clay"}
relative = {"name" : "kingdom", "kind" : "monkey", "owner_name" : "rodney williams"}

pets = [noise, doggie, fishy, relative]

def animal(arg):
    for pet in pets:
        if pet == noise:
            print("The Noisy one:")
            for noise_key, noise_value in noise.items():
                print(f"\t{noise_key.title()} : {noise_value.title()}")
        elif pet == doggie:
            print("The friendly one:")
            for doggie_key, doggie_value in doggie.items():
                print(f"\t{doggie_key.title()} : {doggie_value.title()}")
        elif pet == fishy:
            print("The sushy one:")
            for fishy_key, fishy_value in doggie.items():
                print(f"\t{fishy_key.title()} : {fishy_value.title()}")
        elif pet == relative:
            print("The closest relative:")
            for relative_key, relative_value in relative.items():
                print(f"\t{relative_key.title()} : {relative_value.title()}")
#animal(pets)

"""
Q.6-9
Favorite Places: Make a dictionary called favorite_places . Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places . Loop through the dictionary, and print each person’s name and their favorite places.
"""

favorite_places = {"chi" : ["nigeria", "london", "usa"],
                   "liza" : ["barcelona", "milan", "massachusetts"],
                   "russell" : ["boston", "new bedford", "china"],
                   }

def places(arg):
    for name, places in favorite_places.items():
        print(f"{name.title()}'s favorite places are: ")
        for place in places:
            print(f"\t {place.title()}")

# places(favorite_places)

"""
Q.6-10: Favorite Numbers
Modify your program from Exercise 6-2 (page 102) so each person can have more than one
favorite number . Then print each person’s name along with their favorite numbers .
"""

# Modifying.....
names_numbers = {}
names_numbers["mike"] =  [2, 10, 2]
names_numbers["james"] = [3, 15, 3]
names_numbers["john"] = [4]
names_numbers["veronica"] = [5, 25, 5]
names_numbers["gabriel"] = [6, 30, 6]

def numbers_modify(arg):
    for names, numbers in names_numbers.items():
        if names == "john":
            print(f"{names.title()}'s favorite number is:")
        else:
            print(f"{names.title()}'s favorite numbers are:")
        for number in numbers:
            if number == 4:
                print(f"\t{number}")
            else:
                print(f"\t{number}")

# numbers_modify(names_numbers)

"""
 Q.6-11. Cities: Make a dictionary called cities . Use the names of three cities as keys in your dictionary .
 Create a dictionary of information about each city and include the country that the city is in, its approximate population,
 and one fact about that city . The keys for each city’s dictionary should be something like country, population, and fact .
 Print the name of each city and all of the information you have stored about it.
"""

cities = {
        "lagos" : {
          "country" : "nigeria",
          "population" : 21_000_000,
          "fact" : "It is the sixth-largest city in the world by population"
          },
        "new york" : {
          "country" : "united states of america",
          "population" : 8_623_000,
          "fact" : "Times Square is named after the New York Times"
          },

          "london" : {
            "country" : "england",
            "population" : 8_900_000,
            "fact" : "It is the smallest city in England"
          },

          "dubai" : {
          "country" : "united arab emirates",
          "population" : 3_137_000,
          "fact" : "Burj Khalifa is the world’s tallest building in the world"
          }
        }

def city(arg):
    for city, information in cities.items():
        print(f"\nCity: {city.title()}")
        for information_key, information_value in information.items():
            if information_key == "population" or information_key == "fact":
                print(f"\t{information_key.title()} : {information_value}")
            else:
                print(f"\t{information_key.title()} : {information_value.title()}")

# city(cities)
