#/usr/bin/python3

# import argv from the sys modeul
from sys import argv

# define the arguments passed into the script
script, input_file = argv

# create a function to open and print a file 
def print_all(f):
    print(f.read())

# rewind the file to the start
def rewind(f):
    f.seek(0)

# print a line 
def print_a_line(line_count, f):
    print(line_count, f.readline())

# current file <F4>
current_file = open(input_file)

# print the string  
print("First lets print the whole file\n")

# call the function with the file variable current_file
print_all(current_file)

# print the string 
print("Now lets rewind, kind of likea tape")

# call the funtion rewind with the variable currenlt file
rewind(current_file)

# print the string 
print("Lets print three lines ")

# create the variable current line 
for line in current_file:
    current_line = 0
    print(f"I am printing these lines: {line}")

    
# call the function print_a_line with the variable current_line / current_file
print_a_line(current_line, current_file)

# create variable current file from existing variable pluf one 
current_line +=1
# call the function print_a_line with the variable current_line / current_file
print_a_line(current_line, current_file)

current_line +=1
# call the function print_a_line with the variable current_line / current_file
print_a_line(current_line, current_file)
