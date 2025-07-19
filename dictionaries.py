student={'name':'alex',
         'age':30,
         'email':'alex@gmail.com'}
print(type(student))
student={'name':'alex',
         'age':30,
         'email':'alex@gmail.com',}
print(student)
# assessing
student['age']=40
student['name']='zari'
print(student)
student['occupation']='doctor'
print(student)
student['phone']='0717824020'
print(student)
student['location']={'town':'nakuru','address':1000,'street':'kimathi'}
print(student['location']['street'])
