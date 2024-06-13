


# Carlys Clippers on CCademy
# Changing too
# Smoothie Shop, still following task list

smoothies = ["Fruity", "Tropicaly", "Refreshingly", "Berryly", "Yummly", "Orangy"]
prices = [10, 12, 14, 16, 18, 20]
purchased = [20, 25, 30, 15, 17, 32]


total_price = 0 
for i in prices:
    total_price += i
print(total_price)

average_price = total_price / 6
print(f"Our average Smoothie price is: ${average_price}")

new_prices = [i - 2 for i in prices]
print(new_prices)

total_price = 0 
for i in new_prices:
    total_price += i
print(total_price)

average_price = total_price / 6
print(f"Our new average Smoothie price is: ${average_price}")


total_revenue = 0 
for i in range(len(smoothies)): #finds the lengt of smoothies without hvaing to know it is 6
    total_revenue += prices[i] * purchased[i]
print(f"Our total income on the old model is: {total_revenue}")

average_daily_revenue = total_revenue / 7
print("Average Daily: ", average_daily_revenue) #cause why not throw in a non fstr once in a while

smoothies_under_14 = [smoothies[i] for i in range(len(new_prices)) if new_prices[i] < 14]
print(smoothies_under_14)


