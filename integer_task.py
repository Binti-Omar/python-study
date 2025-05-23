# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp=56.8926
temp=round(temp)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp=56.8926
temp=round(temp,2) 
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp=56.8926
temp=round(temp,3)
print(temp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 
temp=56.8926
temp=str(temp)
temp=temp[0]+'.'+temp[1: ]
temp=float
print(temp)
# convert 111.0789 to 78.9
x=111.0789
x=str(x)
print(x)
x=x[5:7]+'.'+x[7]
x=float(x)
print(x)
