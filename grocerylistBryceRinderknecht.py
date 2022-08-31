#Program 3 Grocery List
#Bryce Rinderknecht
#11/15/20
#The program prompts the user to enter items for a grocery list and store those in a list, prints the list and helps you make a checklist as you are shopping
print("Welcome to the grocery list program!")
lst = []
x = input("Please enter in your grocery list: type done when finished ")
count = 0
while x != "done":
    lst.append(x)
    x = input("Please enter in your grocery list: type done when finished ")
print("Your list is: ")
print(*lst, sep = "\n")
while count < len(lst):
    print("go get: " +lst[count])
    input("type done when you have your item: ")
    count += 1
