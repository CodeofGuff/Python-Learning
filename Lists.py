

# Lists
# Built in Data Structure that allows us to work with a collection of data in sequential order
# Lists always have = [] brackets, each item seperated by a comma (but not needed)
# Can contain mor ethen just numbers
# Lists can contain any data type in Python, ie. string, integer, boolean, and float.
 
# https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-lists/cheatsheet

# Create/Access 11 - 147 - codecademy_Python\Lists_Create_Access.py
# METHODS 145 - 

    
normal_list = [1, 2, 3, 4]
no_space_list = [1,2,3,4]
name_list = ["David", "John", "Sam", "Ava"]
mixed_list = ["David", 2, 13, "Sam"]
anything_list = ["David", 27, True, 0.7]
empty_list = [] # used for user input

print(mixed_list)


# Can combine 2 lists with + []
my_list = [1, 2, 3]
print(my_list)

my_new_list = my_list + [4, 5]
print(my_new_list)


orders = ["flowers", "shampoo", 4]
updated_orders = ["tortillas"]
orders_combined = orders + updated_orders

print(orders)
print(updated_orders)
print(orders_combined)


# Location of elements in a list is an INDEX (0 1 2 3 4)
# if list = ['john', 'bob', 'susan'] then their INDEX is john = 0, bob = 1, susan = 2

bartenders = ["Bryson", "April", "David", "Seth"]

print(bartenders[3])
bartender_4 = "Seth"

print(bartenders[0])
bartender_1 = "Bryson"

# NEGATIVE INDEX allows us to access the last item on alist without knowing 
# its full range with [-1]

bartenders = ["Bryson", "April", "David", "Seth"]

last_element = bartenders[-1]
index3_element = bartenders[3]
print(last_element , index3_element)


# MODIFY LIST ELEMENTs

bottles = ["Tequila", "Vodka", "Gin", "Kraken", "Bourbon"]
print(bottles)

# REPLACED BOURBON WITH WHISKEY

bottles[4] = "Whiskey"
print(bottles)

# REPLACE KRAKEN WITH RUM
bottles[-2] = "Rum"
print(bottles)


# Lists can contain other lists 
# 2d Lists

jim = ["Jim", 20]
anne = ["Anne", 25]
john = ["John", 30]
name_tags = [jim, anne, john]
print(name_tags)


name_tags2 = [["Jim", 20], ["Anne", 25], ["John", 30]]
print(name_tags2)

# Accessing a 2d List 
# Instead of providing a single pair of brackets [ ] 
# we will use an additional set for each dimension past the first.

jims_age = name_tags2[0][1]
print(jims_age)

annes_age = name_tags2[-2][-1]
print(annes_age)


# Modify 2d Lists, Negatgive indices work too. 

fave_booze = [["David", "Gin"], ["Bryson", "Whiskey"], ["Marissa", "Tequila"], ["Seth", "Vodka"]]
print(fave_booze)

fave_booze[0][1] = "Rum"
print(fave_booze)

fave_booze[-4][-1] = "Schnapps"
print(fave_booze)


# Applying learning in order 

first_names = ["David", "Marissa", "Maple", "Ruth"]
print(first_names)

food = ["Pizza", "Ramen", "Leaves"]
print(food)

food.append("Treaties")
print(food)

food_eaten = [["David", "Pizza", True], ["Marissa", "Ramen", False], ["Maple", "Leaves", True], ["Ruth", "Treaties"]]
print(food_eaten)

food_eaten[1][2] = True
print(food_eaten)

food_eaten[1].remove(True)
print(food_eaten)

paula_visit = [["Paula", "Budlight", True]]

food_eaten_final = food_eaten + paula_visit
print(food_eaten_final)


# CREATE/ACCESS ENDS


# WORKING WITH LISTS STARTS

# Methods
# append + remove
# .insert() is a list method to insert an element into a specific index of a list.
# .pop() is a list method to remove and element from a specific index or from the end of a list. 
# .range() is a built-in Python function to create sequence of integers. 
# len() is a built-in Python function to get the length of a list.
# .count() is a list method to count the number of occurrences of an element in a list.
# .sort() or sorted() is a method and a built-in function to sort a list.
# .remove () + .append() as well

#APPEND, REMOVE
method_list = [1, 2, 3, 4]
print(method_list)

method_list.append(5)
print(method_list)

# IE Append
def append_sum(my_list):
  i = my_list[-1] + my_list[-2]
  my_list.append(i)
  i = my_list[-1] + my_list[-2]
  my_list.append(i)
  i = my_list[-1] + my_list[-2]
  my_list.append(i)
  return my_list
# CAN ALSO BE WRITTEN
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))


method_list.remove(4)
print(method_list)


# .insert() method expects two inputs, 
# the first being a numerical index, followed by any value as the second input.

wares_list = ["coin", "trinket", "book", "ring"]
print(wares_list)

wares_list.insert(0, "watch")
print(wares_list)



# .pop() method will remove elements at a specific index.
# Using .pop() without an index will remove whatever the last element of the list is.

pack_list = ["cloth", "saddle", "rope"]
print(pack_list)

removed_element = pack_list.pop()
pack_list.pop(1)
print(pack_list)
print(removed_element)



# range() takes a single input, and generates numbers starting at 0 and 
# ending at the number before the input.
# if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9
# if we call range() with two inputs, we can create a list that starts at a different number.
# If we use a third input, we can create a list that “skips” numbers.

coins = range(7)
print(list(coins), "coins")

trinkets = range(4, 14, 2)
print(list(trinkets))

def every_three_nums(start):
  return list(range(start, 101, 5))
print(every_three_nums(5))


# len() function helps us find the number of items in a list, usually called its length.

bag_list = [1, 2, 3, 4, 5, 6, 7, 8, True, "hello"]
print(len(bag_list))

bag_list_len = len(bag_list) + len(trinkets)
print(len(bag_list))
print(bag_list_len)

#USE OF len() 
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  if len(my_list2) >= len(my_list1):
    return my_list2[-1]
  else:
    return my_list1[-1]
#CAN ALSO BE WRITTEN
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))



# Slicing is extracting only a portion of a list
# syntax: feathers[start:end] 
# start is the index of the first element that we want to include in our selection. 
# end is the index of one more than the last index that we want to include. +1 TO INDEX

feathers = ["1", "2", "3", "4", "5", "6"]
sliced_feathers = feathers[1:4]
print(sliced_feathers)


straws = ["red", "blue", "orange", "green", "yellow", "cyan"]
#used_straws = straws[:2]
used_straws = straws[:-2]
#used_straws = straws[-2:]
#used_straws = straws[2:]
print(used_straws)


def remove_middle(my_list, start, end):
 return my_list[:start] + my_list[end+1:]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#END SLICING



# .count allows us to count occurrences of an itme on a list
# .count() returns a value, we can assign it to a variable to use it.
#  can use .count() to count element appearances in a two-dimensional list.

letters = ["m", "i", "s", "s", "i", "p", "p", "i"]
num_s = letters.count("s")
print(num_s)

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34], [100, 200]]
num_pairs = number_collection.count([100, 200])
print(num_pairs)

#COUNT IE
def more_than_n(my_list, item, n):
  if n < my_list.count(item):
    return True
  else:
    return False
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# PRINT MORE FREQ ITEM
#THE WAY I WROTE IT ( CAN ADD 3RD CONDITION IF THEY ARE ==)
def more_frequent_item(my_list, item1, item2):
  i = my_list.count(item1)
  n = my_list.count(item2)
  if i > n:
    return item1 
  elif i == n:
    return item1 # return item3
  else:
    return item2
# BETTER WAY TO WRITE IT 
# (BUT HAS AN ERROR BECAUSE IT WOULD STILL PLACE ITEM1 AS MORE EVEN IF THEY ARE ==)
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# .sort() allows us to sort the original list numerically, or alphabetically
# cannot be assigned to a var, doesn't return any value

new_item_list1 = ["xylaphone", "button", "eagle beak", "carrot leaf", "fishing lure"]
new_item_list1.sort()
print(new_item_list1)


new_item_list2 = ["xylaphone", "button", "eagle beak", "carrot leaf", "fishing lure"]
new_item_list2.sort(reverse=True)
print(new_item_list2)



# sorted() is different from the .sort() method in two ways:
# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists.

things = ["tables", "lamp", "apple", "acorn", "zebra"]
sorted_things = sorted(things)
print(things)
print(sorted_things)

# sorted() IE
def combine_sort(my_list1, my_list2):
  n = my_list1 + my_list2
  return sorted(n)
#CAN ALSO LOOK LIKE
def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))



# TUPLES
# Like lists, but immutable, meaning it cant be changed. 

my_info = ("David", 33, "Programer")  # Tuple
print(my_info)

name, age, occupation = my_info # Unpacking a Tuple
print(age)

one_element_tuple = (10, ) 
# Must have a comma and space, because () and sound expressions ie. (3 + 1) * 1 = 4
print(one_element_tuple)



# .zip() function allows us to quickly combine associated data-sets 
# without needing to rely on multi-dimensional lists.

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)




#DOUBLE A CERTIAN # IN A LIST
def double_index(my_list, index):
  if index >= len(my_list): 
    return my_list   # Checks to see if index is too big
  else:
    my_new_list = my_list[0:index]     # Gets the original list up to index
    my_new_list.append(my_list[index]*2)  # Adds double the value at index to the new list 
    my_new_list = my_new_list + my_list[index+1:]   #  Adds the rest of the original list
    return my_new_list

print(double_index([3, 8, -10, 12], 2))


# Middle Item
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    s = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return s / 2
  else: 
    return my_list[int(len(my_list)/2)] 

print(middle_element([5, 2, -10, -4, 4, 5]))
