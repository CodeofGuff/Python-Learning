


# Scrabble Project
 
# Use your Python dictionary skills to keep point totals for 
# 4 people playing a game of scrabble! 
# Say goodbye to the pencil-and-notebook scoring method of the past


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letter_to_points = {k:v for k, v, in zip(letters, points)} #combines the lists into a dict

print(letter_to_points)


letter_to_points[" "] = 0 #takes blank tiles into account and makes them worh 0

def score_word(word): #function takes a word and returns points worth
    point_total = 0
    for i in word:
      point_total += letter_to_points.get(i, 0) # goes through each letter in the word and adds the correct key:value to point_total
    return point_total

brownie_points = score_word("BROWNIE") # = 15 points
print(brownie_points)




player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["EREASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items(): # Goes through each list and player and adds their totals together
  player_points = 0
  for i in words:
    player_points += score_word(i)
    player_to_points[player] = player_points


print(player_to_points)





# FURTHER PRACTICE!!


#play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# make your letter_to_points dictionary able to handle lowercase inputs as well