#Extra Credit Program
#Bryce Rinderknecht
#12/10/20
#Validate a password using cetain restraints
password = input("Enter a password: ")

space = [" "]
lst = ["Invalid."]


if len(password)< 8 or len(password) > 16:
    lst.append("Must be 8-16 characters long.")
if not any(str.isupper()for str in password):
    lst.append("Must be at least one upper case character.")
if not any(str.islower()for str in password):
    lst.append("Must be at least one lower case character.")
if not any(str.isdigit() for str in password):
    lst.append("Must contain one number.")
if any(str in space for str in password):
    lst.append(" Cannot have any spaces")
if len(lst) > 1:
    print(*lst)
else:
    print("Valid!")
