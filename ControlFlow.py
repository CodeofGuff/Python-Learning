

#Control Flow
# A program will run (wake up) and start moving through its checklists, 
# is this condition met, 
# is that condition met, 
# okay let’s execute this code and return that value.

# boolean is an expression that is True or False
# ie. "Saturday is the best day" = "No" "Saturday starts with 'S'" = "Yes"

# Relational operators compare two items and return either True or False. 
# For this reason, you will sometimes hear them called comparators.
# == Equals
# != Not equals 

# 1 == 1 / True
# 2 != 4 / True
# 3 == 5 / False

# True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable.
# ie. set_to_true = True, set_to_false = False
# ie. bool_one = 5 != 7, bool_two = 1 + 1 != 2, bool_three = 3 * 3 == 9

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two)) #print(type()) shows the type of variable

bool_test = 5 == 5
print(bool_test)
print(type(bool_test))


# Relational Operators II
# > Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

age = 12
if age <= 13:
    print("Sorry, parental control required")

credits = 120
if credits >= 120:
  print("You have enough credits to graduate!")



#IF Statements

if 2 == 4 - 2: 
  print("apple")
  
is_raining = True
if is_raining:
    print("bring an umbrella")
  
# notice that instead of “then” we have a colon, :
# That tells the computer that what’s coming next is what should be executed if the condition is met.

# Stop David from getting on the Comp
user_name = "angela_catlady_87"
if user_name == "David":
  print("Get off my computer David!")
if user_name == "angela_catlady_87":
  print("I know it is you, David! Go away!")


#Boolean / Logical Operators 
# the conditions you want to check in your conditional statement 
# will require more than one boolean expression to cover. 
# In these cases, you can build larger boolean expressions using boolean/logical operators. 
# and - combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.
# or - combines two expressions into a larger expression that is True if EITHER component is True.
# not - when applied to any boolean expression it reverses the boolean value. True statement + a not operator = a False statement.

#AND
(1 + 1 == 2) and (2 + 2 == 4)   # True
(1 > 9) and (5 != 6)            # False

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0) #false
statement_two = (4 * 2 <= 8) and (7 - 1 == 6) #true
print(statement_one)
print(statement_two)

credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
  

# OR 
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

statement_one = (2 - 1 > 3) or (-5 * 2 == -10) #true
statement_two = (9 + 5 <= 15) or (7 != 4 + 3) #true
print(statement_one)
print((9 + 5 <= 15) or (7 != 4 + 3))


credits = 118
gpa = 2.0
if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
  
  
#NOT - If we have a True statement and apply a not operator we get a False statement.
not 1 + 1 == 2  # False
not 7 < 0       # True

statement_one = not (4 + 5 <= 9) #false
statement_two = not (8 * 2) != 20 - 4 #true
print(statement_one)
print(statement_two)


credits = 120 #can change these values and different PRINT statemnts appear
gpa = 1.8
if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")



# ELSE statements
# Allow us to elegantly describe what we want our code to do when certain conditions are not met.
# Always appear in conjunction with if statements.

weekday = False

if weekday:
  print("wake up at 6:30") #true
else:
  print("sleep in") #false

age = 12
if age >= 13:
  print("Access granted.") 
else:
  print("Sorry, you must be 13 or older to watch this movie.")

credits = 120
gpa = 1.9
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")
  
  
# ELIF / Else If Statements
# checks another condition after the previous IF statements conditions aren’t met.
#control the order we want our program to check each of our conditional statements. 
# First, the if statement is checked, 
# then each elif statement is checked from top to bottom, 
# then finally the else code is executed if none of the previous conditions have been met.


donation = 550
print("Thank you for the donation!")

if donation >= 1000:
    print("LEGENDARY")
elif donation >= 500:
    print("EXPECTIONAL")
elif donation >= 100:
    print("NICE")
else:
    print("THANK YOU")
    
grade = 86
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
  
  
# REVIEW 
# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.
# We can create boolean expressions using relational operators:
# ==: Equals
# !=: Not equals
# >: Greater than
# >=: Greater than or equal to
# <: Less than
# <=: Less than or equal to
# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements

print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# my solution
if planet == 3:
    print("Jupiter")
else:
    print("not Jupiter")
weight = 185 * 2.34
print(weight)

#proper
weight = 185
planet = 3
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

print("Your weight:", weight)


print((9 - 4) * 2 == 77 / 7 - 1)