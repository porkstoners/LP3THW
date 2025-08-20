from sys import argv

script, filename = argv

txt = open(filename, encoding='latin-1')

search = "2025-03-17T23:12:4"

for line in txt:
    if search in line:
        print(line)
        count = 0
        for i in line:
            count += 1
print(count)


# print(f"Heres your file {filename}:")
# print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")


# txt_again = open(file_again, encoding='latin-1')



# print(txt_again.read())
