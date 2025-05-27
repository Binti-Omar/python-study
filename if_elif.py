#Take three inputs from a user, separately. Print the largest of the numbers.
#Hint: Determine what type of data is taken in as input.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if  num1 > num2 and num1 > num3:
    print("The largest number is:", num1)
elif num2 >num1 and num2 > num3:
    print("The largest number is:",num2)   
else:
    print("The largest number is:",num3)

no1=int(input("Enter first number: "))
no2=int(input("Enter second number: "))
no3=int(input("Enter third number: "))
no4=int(input("Enter fourth number: "))
if no1 > no2 and no1 > no3 and no1 > no4:
    print("The largest number is:", no1)
elif no2 > no1 and no2 > no3 and no2 > no4:
    print("The largest number is:", no2)
elif no3 > no1 and no3 > no2 and no3 > no4:
    print("The largest number is:", no3)
else :
    print("The largest number is:", no4)
#  Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature” 
temp=float(input('enter temperature:'))
if temp>30:
    print("The temperature is too high")
elif temp>15:
    print("Normal temperature")
else:
    print("Cold temperature")   
#Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=19
y=95
if x>=10 and x<=20 and y>100:
    print("conditions met ")
else:
    print("conditions not met")   
# Write a Python program that checks if a variable password is equal to the string "secret123".
#  If it is, print "Access   granted", otherwise print "Access denied"
password="secret123" 
if password== "secret123":
    print("Access granted")
else:
    print("Access denied")