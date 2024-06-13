


# LOOPS




# for Loops 
# - In a for loop, we will know in advance how many times the loop will 
# need to iterate because we will be working on a collection with a predefined length. 
# With for loops, on each iteration, we will be able to perform an action on each 
# element of the collection.

# for <temporary variable> in <collection>:
# <action>

# A for keyword indicates the start of a for loop.
# A <temporary variable> that is used to represent the value of the element in the 
# collection the loop is currently on.
# An in keyword separates the temporary variable from the collection used for iteration.
# A <collection> to loop over. In our examples, we will be using a list.
# An <action> to do anything on each iteration of the loop.


ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredients:
    print(ingredient)
# A temporary variable’s name is arbitrary and does not need to be defined beforehand. 
# Both of the following code snippets do the exact same thing as our above example:
for i in ingredients:
    print(i)
for item in ingredients:
    print(item)

# for Loop + range 
promise = "I will finish the python loops module!"

for i in range(5):
  print(promise + str(i + 1))

cache_note = "This cache contains: "
for i in range(3):
    print(cache_note,  str(i + 1), str("coins!"))
    # or (i like f strings)
    print(cache_note, f"{i + 1}", "coins!")
    
    
# while Loops
# A while loop performs a set of instructions as long as a given condition is true.

#while <conditional statement>:
#  <action>

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
# count is initially defined with the value of 0. 
# The conditional statement in the while loop is count <= 3, 
# which is true at the initial iteration of the loop, so the loop body executes.
# Inside the loop body, count is printed and then incremented by 1.
# When the first iteration of the loop has finished, 
# Python returns to the top of the loop and checks the conditional again. 
# After the first iteration, count would be equal to 1 so the conditional still evaluates to True 
# and so the loop continues. 
# This continues until the count variable becomes 4. At that point, when the conditional is tested 
# it will no longer be True and the loop will stop.

coins = 0
while coins <= 4:
    print(f"You have {coins} coins!")
    # or print("You have",  str(coins),  "coins!")
    coins += 1
    print("-----") 

    # WHY THE FUCK IS IT PRINTING I HAVE 5 COINS?!?!?!
print(f"So your total is {coins}! Wow so many coins!")
    


# while Loops + Lists 
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while length > index:
  print("I am learning about " + python_topics[index])
  index += 1

#Infinite loops, 
# your fucked just refresh or control(command) + C
# This is a cool append loop demo
dirt_samples = ["Quartz", "Obsidian", "Balls"]
water_samples = ["Dirty", "Fresh", "Cup"]

for i in dirt_samples:
    water_samples.append(i)
    print(water_samples)
    
    
    
# Loop Control: break
# Stop a list from continuing when a condition is met

ship_style = ["Origin", "Drake", "RSI", "Banu"]
style_1 = "RSI"
print(f"Ship styles for selection: {ship_style}")
print("Make selection now: ")
for n in ship_style:
    print(n)
    if n == style_1:
        print("^ I want this")
        break



# Loop Control: continue
# Similar to when we were using the break control statement,
# our continue control statement is usually paired with some form of a conditional 
# (if/elif/else).
# When a loop then encounters a continue statement it 
# immediately skips the current iteration and moves onto the next element

id_check = [21, 34, 32, 22, 19, 45]

for i in id_check:
    if i > 21:
        print(i)
        continue
    

# nested loops
# with this I can print each list item induvidually

bag_items = [["coin", "cloth"], ["id", "card"], ["nail", "spoon"]]
for i in bag_items:
    print(i)
    for n in i:
        print(n)

#codeCademny IE to add them together:
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0 

for l in sales_data:
  for i in l:
    scoops_sold += i
    continue

print(scoops_sold)



# List Comprehensions
# another way of writing elegant(one line) code
# not a fan of the other elegant loops but this one seems alright
#IE new_list = [<expression> for <element> in <collection>]
dabloons = [100, 2, 4, 56, 76, 39]
d_dabloons = [i * 2 for i in dabloons]
print(d_dabloons)
print("DABLOOOONNSSSSSS!!!!!")

grades = [96, 74, 50, 86, 90]
scaled = [i + 4 for i in grades] # add 4 to make the highest grade = 100
print(scaled)

#####################
#THIS IS TRANFORMED INTO
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
print(only_negative_doubled) 
# INTO THIS
numbers = [2, -1, 79, 33, -45]
new_numbers = [num * 2 for num in numbers if num < 0] 
print(new_numbers)
# ADD ONE OF THESE TO new_numbers TO SEE HOW EACH LOOP CHANGES
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]
# ^ CCADEMY IE
#######################

patrons = [100, 121, 120, 150, 143, 119]
has_enough = [i for i in patrons if i >= 120]
print(f"This patron has: {has_enough}") 
# how do I get each line ot rpint induvidually?
# add a for loop
for p in has_enough:
    print(f"This patron has: {p}") 



## CCademy REVIEW code (self written)
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for i in single_digits:
  print (i)
  squares.append(i*i)
print(squares)

cubes = [i**3 for i in single_digits]
print(cubes)




#Checks how many #'s are divisblew by 10
def divisible_by_ten(nums):
  count = 0
  for n in nums:
    if n % 10 == 0:
      count += 1
  return count
print(divisible_by_ten([20, 25, 30, 35, 40]))


#Creates a new list with automatic greetings
def add_greetings(names):
  g_list = []
  for n in names:
    g_list.append("Hello, " + n)
  return g_list
print(add_greetings(["Owen", "Max", "Sophie"]))

