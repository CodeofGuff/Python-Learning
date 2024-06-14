


# Classes


# Types
# Check a type of variable using type()

a_string = "Cool String"
an_int = 12
print(type(a_string))
# prints "<class 'str'>"
print(type(an_int))
# prints "<class 'int'>"

class Facade:
  pass
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
# __main__.Facade meaning where it was pulled from


# Class
#  A template for a data type
#  It describes the kinds of information that class will
#  hold and how a programmer will interact with that data. 

# class ThisIsAClass:
#   pass

# A class must be instantiated. We must create an instance of the class. 
# Looks similar to calling a func. 

# class_instance = ThisIsAClass()

# Above, we created an object by adding parentheses 
# to the name of the class. We then assigned that 
# new instance to the variable class_instance for safe-keeping 
# so we can access our instance of ThisIsAClass at a later time.

# Instantation takes a class and turns it into an object, 
# In Python __main__ means “this current file that we’re running” 
# You can access all of an object’s class variables with object.variable syntax.
# The first argument in a method is always the object that is calling the method.


class Circle:
  pi = 3.14 # class var
  def area(self, radius): #.area() method that takes two parameters: self and radius.
    # Return the area as given by this formula:
    area = Circle.pi * radius ** 2 
    return area 

# Create an instance of Circle. Save it into the variable circle.
circle = Circle() 

#saving the areas of each unit in a var
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(pizza_area, teaching_table_area, round_room_area)


# Dunder methoeds

# __init__() used to initialize a newly created object, 
#   it is called everytime the class is instantiated

# Methods that are used to prepare an object being 
# instantiated are called constructors.

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"


class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout") # since it is called like a func, params can be added
# prints "SHOUT"
shout2 = Shouter("shout")
# prints "SHOUT"
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"





class Circle:
  pi = 3.14
  def __init__(self, diameter): #constructor with two arugments
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle("36")





# Instance variables and class variables are both accessed similarly in Python.
#  they are both considered attributes of an object.