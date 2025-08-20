from sys import argv

script, filename = argv


print(f"We are going to open a the file called {filename}")
print("If you do not want to open the file press CTRL-C")
print("If you do want to open the file press ENTER")

target = open(filename, 'w')

#target.truncate()

print("I want some user input for this file please provide three lines for me ")

line1 = input("Enter Line one:")
line2 = input("Enter Line two:")
line3 = input("Enter Line three:")


target.write(line1, "\n", line2, "\n", line3)


print(f"We are now going to close the {filename}")

target.close



