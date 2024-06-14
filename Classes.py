


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
# They are both considered attributes of an object.



class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"


hasattr(attributeless, "fake_attribute") # will return True if an object has a given attribute and False otherwise
# returns False

getattr(attributeless, "other_fake_attribute", 800) #  will return the value of a given object and attribute.
# returns 800, the default value

# .count() examples of which elemnts have it
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# dictionaries and integers both do not have a .count attribute, while strings and lists do. 



# Self
# This is the strength of writing object-oriented programs. 
# We can write our classes to structure the data that we need and write methods 
# that will interact with that data in a meaningful way.

# use self to refer to class and instance variables in a method.

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


# We can use the dir() function to investigate an object’s attributes at runtime. 
# dir() is short for directory and offers an organized presentation of object attributes.

class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']


# Everything is an object
# Their classes are int, float, str, list, and dict. 
# Have special syntax for instantiation, 1, 1.0, "hello", [], and {} 

fun_list = [10, "string", {'abc': True}]
type(fun_list)
# Prints <class 'list'>
print(dir(fun_list))
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



# __repr__() This is a method we can use to tell 
# Python what we want the string representation of the class to be. 
# __repr__() can only have one parameter, self, and must return a string.
class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self): #implemented repr and it returned the actual str value
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"


class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
 
  def __repr__(self):   #Added repr and now prints the proper string
    return f"Circle with radius {self.radius}" 

  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)


print(medium_pizza)
print(teaching_table)
print(round_room)



class User:
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return f"Hiya {self.name}!"
  
devorah = User("Devorah")
print(devorah)