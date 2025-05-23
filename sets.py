numbers={10,10,20,20,30,40,50}
print(type(numbers))
print(numbers)
days={'monday','tuesday','wednesday','thursday','friday','saturday','sunday','sunday','sunday','sunday'}
print(days)
days.remove('friday')
print(days)
days.remove('sunday')
print(days)
days.add('friday')
print(days)
days.add('sunday')
print(days)

# differnce
x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
z=x.difference(y)         
print(z)  
# union
z=x.union(y)    
print(z)
# symmetric_difference
z=x.symmetric_difference(y)
print(z)
#intersection
z=x.intersection(y)
print(z)


