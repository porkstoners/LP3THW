# Create a a definition that takes two values and prints out the totals
def cheesse_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man thats enough for a party")
    print("Get a blanket.\n")

# prints a string 
print("Can we just give the function some numbers?")

# run the def and two 
cheesse_and_crackers(24, 32)

print("Or can we use variables from our script?")

amount_of_cheese = 40
amount_of_crackers = 50

cheesse_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")

cheesse_and_crackers(10 + 24, 5 + 10)

print("And we can even combine the two.")
cheesse_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

