
print(type('james')) #<class 'str'>
name = 'james'
print(name) #james
print(type(['james', 'jodie', 'jackson'])) #<class 'list'>
names = ['james', 'jodie', 'jackson']
print(names)
print(names[2]) #jodie
james = ['programmer', 'seoul', 25, False]
james[1] = 'pusan'
print(james) #['programmer', 'pusan', 25, False]

del(james[0])
print(james)
james.append('james')
print(james)