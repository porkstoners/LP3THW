from sys import argv 
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()




print(f"The input file is {len(indata)}' bytes long")
print(f"File is {len(indata)} bytes long\n, Does the ouput file exist? {exists(to_file)} ")
# print("Does the output file exist? %d") % exists(to_file)

input("Press Enter to continue press CTRL-C to abort ")



out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")



out_file.close()
in_file.close()



