#Lab 6/balanceAndInterest
#Bryce Rinderknecht
#10/19/20
#Write a Python function named balanceAndInterest that is given the principle balance and number of year a bank account has been opened. The function should calculate and return the ending balance and interest earned.

print("Hello! Welcome to balanceAndInterest! This program will calculate your ending balance and interest earned based on your principle balance and how long your bank account has been opened for.")
bank = 1
principle = int(input("What is your principle balance for bank #"+str(bank)+"?"))
years = int(input("How many years has the bank account been open for bank #"+str(bank)+"?"))
interest_rate = .04
total = principle * (1 + interest_rate)**years
interest = (1+interest_rate)**years
print("Your ending balance is: $"+str(total))
print("Your accumulated interest is: $"+str(interest))
choice = input("Enter \''Done'\' if you are do not have any more bank accounts that need to be calculated or enter any letter to keep going ")
while choice != "Done":
    bank +=1
    principle: int = int(input("What is your principle balance for bank #"+str(bank)+"?"))
    years = int(input("How many years has the bank account been open for bank #"+str(bank)+"?"))
    interest_rate = .04
    total = principle * (1 + interest_rate) ** years
    interest = (1 + interest_rate) ** years
    print("Your ending balance is: $" + str(total))
    print("Your accumulated interest is: $" + str(interest))
    choice = input("Enter \'Done\' if you are do not have any more bank accounts that need to be calculated or enter any letter to keep going ")
if choice == "Done":
    print("Goodbye.")
