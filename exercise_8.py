"""
# Try it yourself: Functons
Q.8-1. Message: Write a function called display_message()
that prints one sentence telling everyone what you are learning about in this chapter.
Call the function, and make sure the message displays correctly.
"""

def display_message():
    """Simply disply of character contents being digested"""
    print("I am learning how to write clear, concise and bug-free functions in python")

# display_message()

"""
Q.8-2 Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call.
"""

def favorite_book(title):
    print(f"One of my favorite books is {title}")

"""
favorite_book("Alice in Wonderland")
Q.8-3. T-Shirt: Write a function called make_shirt()
that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt.
Call the function a second time using keyword arguments .
"""

def make_shirt(size):
    print(f"The round-neck T-shirt is of {size} size")

# make_shirt("medium")
# make_shirt(size = "medium")

"""
Q.8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python .Make a large shirt and a medium shirt
with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size_0, size_1, size_2="extra-large"):
    print("I love python")
    print(f"My collecation are only in sizes {size_0}, {size_1} and {size_2}")

# make_shirt("small", size_1 = "medium")

"""
Q.8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland . Give the parameter for the country
a default value. Call your function for three different cities, at least one of which is not in the default country.
"""

def described_city(nigerian_cities, country = "nigeria"):
    city = input(f"Please enter a name of a city in {country.title()}: ")
    if city in nigerian_cities:
        print(f"{city.title()} is in {country.title()}")
    elif city not in nigerian_cities:
        print(f"{city.title()} is not a {country.title()}")

nigerian_cities = ["lagos", "port harcourt", "abuja", "benin", "owerri"]

#described_city(nigerian_cities)

"""
Q.8-6. City Names: Write a function called city_country() that takes in the name of a city and its country .
The function should return a string formatted like this:
"""

def city_country(city, country = "united states of america"):
    print("-"*100)
    print(f"{city.title()}, {country.title()}")
    print("-"*100)

#city_country(city = "massachusetts")

"""
# Q.8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album . The function should take in an artist name and an album title,
and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album information correctly.
Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
If the calling line includes a value for the num- ber of tracks, add that value to the album’s dictionary.
Make at least one new function call that includes the number of tracks on an album.
"""

def make_album(artist_name, album_title, number_of_tracks=""):
    music_album = {"artist": artist_name.title(), "album": album_title.title()}
    if number_of_tracks:
        music_album["tracks"] = number_of_tracks
    return music_album


# print(make_album(artist_name = "wizkid", album_title = "superstar", number_of_tracks = 17))
# print(make_album(artist_name = "davido", album_title = "omo baba olowo"))
# print(make_album(artist_name = "dbanj", album_title = "no long thing"))

"""
# Q.8-9. Magicians: Make a list of magician’s names. Pass the list to a
function called show_magicians(), which prints the name of each magician in the list .
"""
def show_magicians(magicians):
    print("Names of famous nollywood magicians: ")
    for magician in magicians:
        yield(magician.title())


magicians = ["abrakadaba", "odeshi", "vanish", "kianor kianor"]
generator = show_magicians(magicians)

def generate(generator):
    for magician in generator:
        print(magician)

# generate(generator)

"""
# Q.8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 .Write a function
called make_great() that modifies the list of magicians by  adding the phrase the Great to
each magician’s name.Call show_magicians() to see that the list has actually been modified.
"""

def make_great(magicians):
    for magician in magicians:
        print(magician)

# make_great(magicians)

"""
Q.8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich .
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that is being ordered .
Call the function three times, using a different num- ber of arguments each time .
"""

def sandwiches(*items):
    print("Sandwich requested items: ")
    for item in items:
        print(f"- {item}")

# sandwiches("beef", "hot dog", "chicken", "ham", "ketchup")

"""
Q.8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
"""

def build_profile(first, last, **profile_info):
    profile = {}
    profile["first"] = first
    profile["last"] = last
    for key, value in profile_info.items():
        profile[key] = value
    return profile


build_finish = build_profile("Chidera", "Biringa",
    location = "new bedford",
    major = "computer science",
    languages = ["python", "java", "R"]
    )
# print(build_finish)
