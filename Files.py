

# Files
# Named locations on disk to store related information that can be used in Python.
# we use 'with' as a context manager takes care of opening the file
# when we call open() and then closing the file after we leave the indented block.

# This opens a file object called cool_doc and creates a new indented block 
# where you can read the contents of the opened file. 
# We then read the contents of the file cool_doc using cool_doc.read() 
# and save the resulting string into the variable cool_contents. 
# Then we print cool_contents, which outputs the info in the .txt doc

# Open up file objects using open() and with.
# Read a file’s full contents using Python’s .read() method.
# Read a file line-by-line using .readline() and .readlines()
# Create new files by opening them in write-mode.
# Append to a file non-destructively by opening a file in append-mode.
# Apply all of the above to different types of data-carrying files including CSV and JSON!

with open('text.txt') as text_file:
  text_data = text_file.read()
print(text_data)


# Iterating through lines in a file
# .read() will grab the whole doc
# .readlines() will read a txt file line by line
# .readline() will iterate a single line at a time


with open("text.txt") as multi_lines:
    for l in multi_lines.readlines():
        print(l)
        
with open("text.txt") as line_test:
    first_line = line_test.readline()
    second_line = line_test.readline()
print(first_line, second_line)
        
        
# Writing a file
# we pass the second argument to open() ,w to inditicate we are 'Writing'.
# ,r is the default value meaning 'Read'

# With each time run, will overwrite previous file
with open("new_text.txt", "w") as test_text:
    test_text.write("Hello world!")


# Appending a file
# use ,a argument to append
# The newline character '\n' moves the new line to the next line 
# before adding the rest of the sting. 

#normally this would keep adding the string multiple times, 
# but this file re-writes 'new_text.txt on each call
with open("new_text.txt", "a") as test_text2:
    test_text2.write("\nAnd hello to you too!")




# CSV Files
# Comma Seperated Value, an example of afile that imiposes structure to the data
# Think of them as plain text files, using commas to sepearete the values. 
# we call all files with a list of different values a CSV file and then 
# use different delimiters,  delimiter="@" , (like a comma or tab) to indicate where the 
# different values start and stop.



with open("logger.csv") as log_csv_file:
  log = log_csv_file.read()
  print(log)
  
  
# The possibility of a new line escaped by a \n character in our data is why we 
# pass the newline='' keyword argument to the open() function.
# ,newline='' argument to open() function so that we don’t accidentally
# mistake a line break in one of our data fields as a new row in our CSV 

# import CSV to be able to parse the CSV file
import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file) # creates a dictioinary we can now reference
  for f in cool_csv_dict:
    print(f["Cool Fact"]) # 'Cool Fact' is a key used in the first line of the CSV file

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@") #delimiter is used as the indicication where values are seperated
  isbn_list = []
  for i in books_reader:
    isbn_list.append(i["ISBN"])
print(isbn_list)


# Writing a CSV file
# Created the logger.csv file

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]

fields = ['time', 'address', 'limit']


with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields) #dictates creating the file, and what the fieldnames(headers) will be
  log_writer.writeheader() #This writes all the fields passed to fieldnames as the first row in our file.
  for i in access_log:
    log_writer.writerow(i) #writes each line to CSV
    



# Reading / Writing a JSON file
# JavasScript Object Notation
# JSON’s format is endearingly similar to Python dictionary syntax, making it easy to read

#json.load() creates a dictionary out the json file
#json.dump() to write a file, takes two arguments: data object, then the file object to save.


import json

with open("message.json") as message:
    message_is = json.load(message)
    print(message_is["text"])


data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open("json_file.json", "w") as json_maker:
    json.dump(data_payload, json_maker) # data object(where the data is from), temp var we made