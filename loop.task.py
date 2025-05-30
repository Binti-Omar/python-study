# Write a program that displays a numbers 1 to 50 inside a list.
numbs=list(range(1,50))
print(numbs)
# From 1 above display the ones divisible by 7 or 5 inside a list.
no=[]
for u in numbs:
       if u%5==0 or u%7==0 :
              no.append(u)
print(no)
# Find sum and average of values in the range between 10 to 40.
g=list(range(10,41))
print(g)
sum=0
for u in g:
       sum=sum+u
print(sum)
average=sum/len(g)
print(average)
# Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers=[]
numb=list(range(10,51))
for u in numb:
       if u % 2!=0:
              odd_numbers.append(u)
              if len(odd_numbers)==10:
                     break
print(odd_numbers)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# get input,convert to int,create a list of numbers upto 11
numbers=int(input("enter number :"))
n=list(range(0,11))
# loop thru the list,print()
for i in n:
       print(i)
       mult=10*i
print(f"{i}*{numbers}={mult}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count=0
no=list(range(1,51))
for i in no:
       if i%2==0:
              count=count+1
print(count)
       
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
ls1 = [ ('Jay', 20), ("Mo", 30), ("Mya", 32) ]
# Display the total quantity of the 3 above.
sum=0
for i in ls1:
       print(i[1])
       sum=sum+i[1]
print(sum)











