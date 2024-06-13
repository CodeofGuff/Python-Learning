

# Sals Shipping Project

# build a program that will take the weight of a package and determine 
# the cheapest way to ship that package.

# This program asks the user for the weight of their package and then tells them which method of
# shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.


# Variables
weight = 10
cost_ground = ""
cost_drone = ""
prem_ground = 125


# Ground SHipping
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <= 6:
    cost_ground = weight * 3 + 20
elif weight <= 10:
    cost_ground = weight * 4 + 20
else:
    cost_ground = weight * 4.75 +20

print("Cost with Standard Ground: $", cost_ground)

# Premium Shipping
print("Cost with Premium Ground: $",prem_ground)

# Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.5
elif weight <= 6:
    cost_drone = weight * 9
elif weight <= 10:
    cost_drone = weight * 12
else:
    cost_drone = weight * 14.25
print("Cost with Drone: $", cost_drone)