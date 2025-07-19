fruits=["apples","banana","orange","melon"]
for u in fruits:
    print(u)
    

for i in range(100):
    print(list(i))
x= list(range(2,10))
for i in x:
  if i % 2 == 0:
     print(i)

# display odd numbers from 100 to 200
no=list(range(100,201))
for u in no:
   if u %2!=0:
      print(u) 

# store odd numbers from 100 to 200 in a list
odd_numbers=[]
numbs=list(range(100,200))

for a in numbs:
    if a %2!=0:
      odd_numbers.append(a)
print(odd_numbers)
# store even numbers from 100 to 200 in a list
even_numbers=[]
no=list(range(100,200))

for b in no:
   if b%2==0:
      even_numbers.append(b)
print(even_numbers)