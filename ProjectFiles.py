





# Hacking the Fender
# Files learning project


import csv
import json


compromised_users = []

#Creating the com[promised user list
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for l in password_csv:
    password_row = l
    compromised_users.append(l["Username"] + ", ")
  
#Adding a txt file with the compromised usernames
with open("compromised_user.txt", "w") as compromised_user_file:
  for l in compromised_users:
      compromised_user_file.write(l)
      
      
#Create a JSON message to the bos
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)
