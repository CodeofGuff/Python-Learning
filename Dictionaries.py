


# Dictinaries
# A dictionary is an unordered set of {key: value, key: value, key:value} pairs, seperated by commas.

# It provides us with a way to map pieces of data to 
# each other so that we can quickly find values that 
# are associated with one another.


sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)



# keys can be numbers, and values cann be any type: strings, numbers, lists, other dictionaries etc. 
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

# Can be empty, to be filled later
my_empty_dictionary = {}


# To add a single key: value pair to a dictionary, we can use the syntax:
# dictionary[key] = value


# Dictionaries 


# REMIDNER Lists are muteable and cannot be keys 



# Adding multiple keys using the .update() method
# .append() does not work in dict
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({
    
  "theLooper": 138475, "stringQueen": 85739
  
})
print(user_ids)


# add keys without chanbging the definition by using:
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)


# combine to lists into a dictionary using Dict Comprehensions
# zip() combines two lists into an iterator of tuples with the list elements paired together.
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# would i make a    zipped_drinks = zip(drinks, caffeine)  var first? Dont need to? 
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}         
print(drinks_to_caffeine)



# REVIEW CREATE DICT FORM LISTS POROJECT

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {k:v for k, v in zip(songs, playcounts)}\

print(plays)

plays.update({"Purple Haze": 1})
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}} 

print(library)

# **make a dict for Sunday Feelings**



# Access keys in a dict
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["air"])

# Updating a key then checking if it exists and pulling it
zodiac_elements.update({"energy": "Not a Zodiac element"})

i = "energy" # var not needed but I like them
if i in zodiac_elements:
    print(zodiac_elements["energy"])

print(zodiac_elements)


# We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. 
# If the key you are trying to .get() does not exist, it will return None by default:

building_heights = {
    "Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3
    }
#this line will return 632:
building_heights.get("Shanghai Tower")
#this line will return None:
building_heights.get("My House")

#can specify a value to return if the key doesn't exist
print(building_heights.get('Shanghai Tower', 0)) # Prints 632
print(building_heights.get('Mt Olympus', 0)) # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'

# Another IE
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("SuperStackSmash", 100000)
print(stack_id)



# Removing a key with .pop()
# .pop() removes AND returns the value being removed
# We can provide a default calue to return if it doesn't exist
available_items = {
    "health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30
    }
health_points = 20
hp = health_points # cause i like vars
print(hp, available_items)

hp = hp + available_items.pop("stamina grains", 0)
print(hp, available_items) # 35, [LIST WITHOUT STAMINA GRAINS] as it added stamina grains to HP then removed it from the list


hp = hp + available_items.pop("cake of the cure", 0)
print(hp, available_items)


# Get all keys  
#  (and some values)

test_scores = {
    "Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]
    }
print(list(test_scores))
print(list(test_scores.values()))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"] using the list() func
# .keys() method returns a dicts keys as a VIEW object, meaning we can see the keys with out being able to mod them
# .values() method does the same with the Values

for student in test_scores.keys():
 print(student)
#prints Grace Jeffrey Sylvia Pedro Martin Dina

students = test_scores.keys()
print(students)
scores = test_scores.values()
print(scores)

for scores in test_scores.values():
    print(scores)


# Get all Values
num_exercises = {
    "functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18
    }
total_exercises = 0

for i in num_exercises.values():
    total_exercises += i
    print(total_exercises)
    
    
# Get ALL items with .items() method
# each ele returned by .items() is a tuple with (key, value)
pct_women_in_occupation = {
    "CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9
    }
for title, percent in pct_women_in_occupation.items():
    print(f"Women make up", percent, "percent of", title + "s")

#another way to access data using .items() method using indices
for i in  pct_women_in_occupation.items():
    print(i[0])
    print(i[1])


# REVIEW
import random

tarot = {
    1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"
    }

rand_num_past = random.choice(list(tarot.keys()))
rand_num_present = random.choice(list(tarot.keys()))
rand_num_future = random.choice(list(tarot.keys()))
spread = {}

spread["past"] = tarot.pop(rand_num_past)
spread["present"] = tarot.pop(rand_num_present)
spread["future"] = tarot.pop(rand_num_future)
print(spread)

for  d, g in spread.items():
    print(f"Your", d, "is the", g, "card.")
