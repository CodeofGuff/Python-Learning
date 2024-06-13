




# Functions

# allow tasks to be performed multiple times within a program without having to be rewritten.
# 
# Some tasks need to be performed multiple times within a program. 
# Rather than rewrite the same code in multiple places, 
# a function may be defined using the 'def' keyword. 
# the amount of whitespace tells the computer what is part of a function and what is not part of that function.

# def function_name(): 
  # functions tasks go here


var = ["Things", "Stuff", "AC", "Items"]
what_i_want = "AC"

def this_is_a_function():
    for i in var:
        if i == what_i_want:
            print(i)



print("Hi")


this_is_a_function()


# Parameters & Arguments
# Function definitions may include parameters, providing data input to the function.
# Parameter - Supplies data to a defined function when it is called in a program.
# Argument - is the data that is passed in when we call the function, which is then assigned to the parameter name.
#                 Parameter
def trip_welcome(destination): 
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

#              Arugment
trip_welcome("the Bahamas")




# Multpiple Parameters
def fill_coin_bag(cashier, bag):
    new_bag_total = cashier + bag 
    print(f"The cashier hands you ", cashier, " coins!")
    print(f"You take the ", cashier,  " coins and place them in your bag with ", bag, " coins")
    print(f"You have ", new_bag_total, " coins!")

fill_coin_bag(20, 60)



# Arguments 
# Positional arguments: arguments that can be called by their position in the function definition.
# Keyword arguments: arguments that can be called by their name.
# Default arguments: arguments that are given default values.


# Built in Functions
# Codecademy IE 
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)


# Returns 
# Functions can also return a value to
# the program so that this value can be modified
# or used later. We use the Python keyword return to do this.

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


# Multiple Returns 


def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()


print(most_popular1)
print(most_popular2)
print(most_popular3)

# More Codecademy IE
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)


# Functions Review
# using Codecademys Tasks list and names cause im too tired to make up different ones


def trip_planner_welcome(name):
  print("Welcome to tripplannerv1.0 " + name)  


trip_planner_welcome("David")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5) # I do not understand how this makes 10 = 2 
  
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimate) + " hours")

destination_setup("Cali", "Fiji", 10, "Plane")



# This was a fun challenge one from the review
# Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. 
# If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"