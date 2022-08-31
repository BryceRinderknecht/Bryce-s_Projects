#Lab 4
#Bryce Rinderknecht
#10/5/20
#Write a program to calculate the amount you would receive for the next ten years ­under each option to determine the best choice.
count = 0
total = 0
salary = 20000
count1 =.5
salary1 = 10000
total1_half_year = 0
print("Option      Current Salary  Total")
while count < 10:
    count +=1
    count1 += .5
    total1_half_year += salary1
    salary1 += 250
    print("Half year")
    print("Option 1:  "+str(salary)+"           "+str(total))
    print("Option 2:  "+str(salary1)+"           "+str(total1_half_year))
    total += salary
    salary += 1000
    total1_half_year += salary1
    salary1 += 250
    print("Year "+str(count))
    print("Option 1:  "+str(salary)+ "           " + str(total))
    print("Option 2:  " +str(salary1)+ "           " + str(total1_half_year))
print("Option 1 earns $"+str(total))
print("Option 2 earns $"+str(total1_half_year))
