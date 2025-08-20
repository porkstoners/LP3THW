# Import the argv module from sys
from sys import argv

# specify the arguments require when running the scrip
script, filename = argv

# create a variable txt that opens the file provided in your argument
# set the encoding to latin-1 to accomodate the string charactersin the file
txt = open(filename, encoding='latin-1')
txt1 = open(filename, encoding='latin-1')

# createa variable string we can use to search the file 
search = "tailscaled[1786]"

count = 0 

# create a for loop to iterate over the file with 
for match in txt:
    count += 1
    if search in match:
        print(match)
print(count)


for lines in txt1:
    count += 1
print(count)
# print(f"Heres your file {filename}:")
# print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")


# txt_again = open(file_again, encoding='latin-1')



# print(txt_again.read())
