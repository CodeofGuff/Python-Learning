



# STRINGS
# Like a 'List' of charatcers

#selecting the index of a string
fruit = "strawberry"
first_letter = fruit[0]


# string slicing with:
# string[first_index:last_index]
# creates a substring - that starts at (and includes) the first_index
# and ends at (but excludes) the last_index.

fruit2 = "blueberry"
new_list = fruit2[0:4] #'blue'
# or 
new_list2 = fruit2[:4] # 'blue' slice starts at the begining
# or
new_list3 = fruit2[4:] # 'berry' slice conitinues from index, till the end of string.
print(new_list3)

#PASSWORD/LOGIN GEN
first_name = "David"
last_name = "Guffre"

new_account1 = first_name[0] + last_name[:4] # first 4 letters of lastname
temp_password1 = last_name[2:6] + "13579" # 3rd - 6th letter of last name

print(f"\nHey there {first_name}! \nWelcome to the thing. \nYour new account log in is: {new_account1}. \nYour temporary password is {temp_password1}. \nPlease change your temporary password ASAP in user settings.")

#PASSWORD/LOGIN GEN FUNC
def account_generator(first_name, last_name):
    return first_name[:2] + last_name[:4]
    
new_account = account_generator(first_name, last_name)

def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)
print(f"Here is your new user name: {new_account}, and PW: {temp_password}")


# using len() and others? 

town_name = "hambergurtonthithles"
length = len(town_name)
last_chars = town_name[length-10:]
print(length)
print(last_chars)


# Strings are immutable 
first_name = "Bavid"
last_name = "Guffre"
fixed_first_name = "D" + first_name[-4:]

print(fixed_first_name)

# Getting a length without len()

def get_length(i):
    counter = 0 
    for l in i:
        counter += 1
    return counter
    
len = get_length('hahahahaa')
print(len)


# Returns true if the word contaisn the letter
def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
    return False

print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "o"))


# 

def contains(big_string, little_string):
  return little_string in big_string
#returns True if IE. melon is in watermelon

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
# returns a list of letters each string has in common




# Learned what?
# A string is a list of characters.
# A character can be selected from a string using its index string_name[index]. 
# These indices start at 0.
# A ‘slice’ can be selected from a string. 
# These can be between two indices or can be open-ended, 
# selecting all of the string from a point.
# Strings can be concatenated to make larger strings.
# len() can be used to determine the number of characters in a string.
# Strings can be iterated through using for loops.
# Iterating through strings opens up a huge potential for applications, 
# especially when combined with conditional statements.





# String Methods 
# All have the same syntax:
# string_name.string_method(arguments)
# These string methods allow you to change the case of a string, 
# split a string into many smaller strings, join many small strings 
# together into a larger string, and allow you to 
# neatly combine changing variables with string outputs.


# .lower() returns the string with all lowercase characters.
# .upper() returns the string all uppercase characters.
# .title() returns the string in title case, the first letter of each word is capitalized.
poem_title = "wastleland diaries"
poem_author = "Mad Max"

poem_title_fixed = poem_title.title()
print(poem_title, "/", poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author, "/", poem_author_fixed)

# .split() returns a new object
# takes one argument, returns a list of 
# substrings found betwen the given argument
# (which in the case of .split() is known as the delimiter).
# string_name.split(delimiter)
# will default to  split spaces if no argument is given

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

# You can use any string as the argument for .split(), 
# making it a versatile and powerful tool.
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# Create another list that contains the last names 
# of the poets in the provided string.
author_last_names = [] 
for i in author_names:
  author_last_names.append(i.split()[-1])
print(author_last_names)

#escape sequences 
# \n Newline
# \t Horizontal Tab
# \n will allow us to split a multi-line 
# string by line breaks
# \t will allow us to split a string by tabs. \
# \t is particularly useful when dealing with 
# certain datasets because it is not uncommon for 
# data points to be separated by tabs.
spring_storm_text = \
"""The sky has given over 
...
...
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)


# Joining Strings 
# 'delimiter'.join(list_you_want_to_join)
# The string .join() acts on is the delimiter you want to join with,
# therefore the list you want to join has to be the argument.
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)


# We could join this list together with ANY string. 
# One often used string is a comma , because then we can 
# create a string of comma-separated values, or CSV.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
# creates each list item on a new line
print(winter_trees_full)


# .strip()
# helps clean up strings with extra whitespace, linesbreaks, and tabs 
# that come from harvesting real data. 
featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas     


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
print(love_maybe_lines)

love_maybe_lines_stripped = []
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())

love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)



# .replace()
# string_name.replace(substring_being_replaced, new_substring)
with_spaces = "You got the kind of loving that can be so smooooth"
with_underscores = with_spaces.replace('smooooth', 'smooth')
print(with_underscores)


# .find()
# .find() takes a string as an argument and searching the 
# string it was run on for that string. It then returns 
# the first index value where that string is located.
print('smooth'.find('t'))
# => '4'
print("smooth".find('oo'))
# => '2'

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)


# .format()
# takes variables as an argument and includes them 
# in the string that it is run on. 

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song_statement("Homesick", "ADTR"))
# => "My favorite song is Smooth by Santana."

def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)
print(poem_title_card("I Hear America Singing", "Walt Whitman"))




# Review 
# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() allows you to interpolate a string with variables.


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",") # split each list at the ','
print(highlighted_poems_list)

highlighted_poems_stripped = [] # strips the whitespace 
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
print(highlighted_poems_stripped)

highlighted_poems_details = [] # removes the ':' and creates new lists from them
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))
print(highlighted_poems_details)

titles = [] 
poets = []
dates = [] 
for i in highlighted_poems_details: # seperates each aspect of each list in their own lists
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])

for title, poets, dates in highlighted_poems_details: 
  print("The poem {} was published by {} in {}".format(title, poets, dates))



# Review Project
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
# Start coding below!

daily_sales_replaced = daily_sales.replace(";,;", "/")
print(daily_sales_replaced)

print("...........................")

daily_transactions = daily_sales_replaced.split(",")
print(daily_transactions)

print("...........................")

daily_transactions_split = []
for i in daily_transactions:
  daily_transactions_split.append(i.split("/"))
print(daily_transactions_split)

print("...........................")

transactions_clean = []
for i in daily_transactions_split:
  new_list = []
  for n in i:
    new_list.append(n.replace("\n", "").strip(" "))
  transactions_clean.append(new_list)
print(transactions_clean)


print("...........................")

customers = []
sales = []
thread_sold = []
for i in transactions_clean:
  customers.append(i[0])
  sales.append(i[1])
  thread_sold.append(i[2])
print(customers, sales, thread_sold)

print("...........................")

total_sales = 0
for i in sales:
  total_sales += float(i.strip("$"))
print(total_sales)

print("...........................")

print(thread_sold)
print("...........................")

thread_sold_split = []
for i in thread_sold:
  for n in i.split("&"):
    thread_sold_split.append(n)
print(thread_sold_split)
  
print("...........................")

def color_count(color):
  color_total = 0
  for i in thread_sold_split:
    if color == i:
      color_total += 1
  return color_total

print(color_count("white"))

print("...........................")
colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for i in colors:
  print("Today we sold {0} of {1}".format(color_count(i), i))