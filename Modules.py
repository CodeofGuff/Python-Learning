

# Modules / Libraries


# how to use tools other people have built in Python 
# that are not included automatically for you when 
# you install Python. Python allows us to package 
# code into files or sets of files called modules.

# A module is used as a tool. Modules are also often referred to as “libraries” 
# or “packages” — a package is really a directory that holds a collection of modules.

# ie: top of the file would be the syntax:
# from module_name import object_name

from datetime import datetime

current_time = datetime.now()
print(current_time)

# import random
# generate numbers, or select items at random
# random.choice() 
# which takes a list as an argument and returns a number from the list
# random.randint() 
# which takes two numbers as arguments and generates a random number between the two numbers you passed in

import random

random_list = [random.randint(1, 100) for i in range(101)]
random_number = random.choice(random_list)
print(random_number)

# Notice that when we want to invoke the randint() function
# we call random.randint(). This is default behavior 
# where Python offers a namespace for the module. 
# A namespace isolates the functions, classes, and variables 
# defined in the module from the code in the file 
# doing the importing. Your local namespace, meanwhile, 
# is where your code is run.

# Python defaults to naming the namespace after the module
# being imported, but sometimes this name could be ambiguous
# or lengthy. Sometimes, the module’s name could also
# conflict with an object you have defined within your local namespace.

# This name can be altered by aliasing using the as keyword:
# import module_name as name_you_pick_for_the_module


#random.sample takes a list and randomly selects k items from it
# new_list = random.sample(list, k)
#for example:
nums = [1, 2, 3, 4, 5]
sample_nums = random.sample(nums, 3)
print(sample_nums)


# Using PyPlot from MatPlotLib ranaming ad PLT to use to create a plot graph. 
# Does not work in VSCode? Library is wrong? Hello? 

#from matplotlib import pyplot as plt

#numbers_a = range(1, 13)
#numbers_b = random.sample(range(1000), 12)
#print(numbers_b)

#plt.plot(numbers_a, numbers_b)
#plt.show()



# Usually, modules will provide functions or data types
# that we can then use to solve a general problem,
# allowing us more time to focus on the software that
# we are building to solve a more specific problem.


# using decimal to add each decimal together without is ending in .889999999 etc. 
from decimal import Decimal

two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.5") * Decimal("0.65")
print(four_decimal_points)



