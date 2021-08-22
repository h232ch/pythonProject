
while False:
    print("hello world")
print('After word')

i = 0
while i < 3:
    print('Hello world')
    i = i + 1

i = 0
while i < 10:
    print('print("hello world '+str(i*9)+'")')
    i = i + 1

i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i = i + 1
print('after while')