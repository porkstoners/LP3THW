# Create a function (def)named print_two - include *args this allows us to specify arguments 
def print_two(*args):
    arg1, arg2 = args
    print (f"arg1: {arg1} arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")

def print_one(arg1):
    print (f"arg1: {arg1}")

def print_none():
    print("I have nothing!")


def switch_types(*switches):
    sw_model_1, sw_model_2, sw_model_3 = switches
    print("## Switch Types ##")
    print(f"Model1: {sw_model_1}\nModel2: {sw_model_2}\nModel3: {sw_model_3}")

print_two("Doug", "Barker")
print_two_again("Doug", "Barker")
print_one("First")
print_none()
switch_types("7150", "7050", "7060")