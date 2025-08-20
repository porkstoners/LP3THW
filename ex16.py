# imports the arg variable from the sys module
from sys import argv

# uses the argv module to request the variables required when the script is run. 
# example python3 file1.py file.txt 
# script = file1.py filename = file.txt
script, filename = argv

# Warns the user that the contents of the file will be erased 
# prints the text and uses an fstring to call the filename recived from the argv module
print(f"We are going to erase {filename}")
# prints a string - with the default break command
print("If you don't want that hit CTRL-C (^C).")
# prints a string
print("If you do want that hit Enter.")

# requests  an input from the user and prints a question mark as a prompt  
input("?")

#prints a string to tell the user we are about to open the file
print("Opening the file...")
# creates a variable to open the file - users the filename variable provided from theargv module - opens the file in write mode using 'w'
target = open(filename, 'w')

# Prints a string stating the file will be truncated. (I don't know what that means at the time of writing this my best guess is that...
# The existing content will be erased 
print("Truncatingt the file. Goodbye")
## LOOKUP WHAT THIS DOES ##
target.truncate()

# Prints a string
print("Now I am going to ask for three lines ")

# Creates a variable called line1 - uses the input function to request data from the user. Appends a string as a prompt for the user
line1 = input("line 1:")
# Creates a variable called line1 - uses the input function to request data from the user. Appends a string as a prompt for the user
line2 = input("line 2:")
# Creates a variable called line1 - uses the input function to request data from the user. Appends a string as a prompt for the user
line3 = input("line 3:")

# Prints a string explainingthat the users imputs will be writted to the file we have opened.
print("I am going to write these to the file ")

# Writes the variable created by the user input to a line 
target.write(line1)
# adds a new line with the formatter \n
target.write("\n")
# Writes the variable created by the user input to a line 
target.write(line2)
# adds a new line with the formatter \n
target.write("\n")
# Writes the variable created by the user input to a line 
target.write(line3)
# adds a new line with the formatter \n
target.write("\n")

# prints a string telling the user the file is going to be closed 
print("And finally we are going to close it.")
# closes the file
target.close()


