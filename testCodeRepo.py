



# TESTED CODE REPOSITORY

import random

var1 = "50 "
var2 = 45 + 5
var3 = "Add"
var4 = "Teeth"
var5 = "Together"


print("Total = ")
print(var1 + var4)



print("Hello World")


name = "David"
question = "am I alone?"
answer = ""
random_number = random.randint(1, 4)

if random_number == 1:
    answer = " depends on who you ask."
elif random_number == 2:
    answer = " . . . Yes"
elif random_number == 3:
    answer = " No! Behind you!"
elif random_number == 4:
    answer = ", you are never alone with yourself"
    
print(name + ",", question, "Hmmm" + answer)



coin_bag = "So many coins in your bag! Look at them: "

def coins(n):
    for coins1 in range(10):
        if coins1 >= 10:
            print(f" {coin_bag} {coins1 + 1}")
    else:
        print("You're poor")
        

coins(11)


list = ['marbles', 'rollers', 'galactics', 'speedys']
def list_function():
    list[2] = 'gals'
    print(list)

list_function()


print("What is your name?")

name = "Marissa Jones"

print(f"Hello {name}, It is nice to meet you!")






var1 = 1 > 99

if var1 == True:
    print("Yay!")
else:
    print("boo!")
    
    
print(1 > -1)



def greet():
    var = "This is a sentence"
    total = 0
    for i in var:
        if i == "s":
            total += 1
    if total == 3:
        print("hello world")

greet()

a = True
if a == True:
    print("Hello world")
else:
    print("Fuck You")

b = 2
if b != 2:
    print("Yes")
else:
    print("False")
    

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
