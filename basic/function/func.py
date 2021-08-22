
def a3():
    print('aaa')
a3()

def a4():
    return 'aaaa'
print(a4())


def a(num):
    return 'a' * num
print(a(3))


def make_string(str, num):
    return str*num
print(make_string('b', 10))

input_id = input('input your id \n')
def login(_id):
    members = ['james', 'jackson', 'jodie']
    for member in members:
        if member == _id:
            return True
    return False

if login(input_id):
    print('Hello, ' + input_id)
else:
    print('who are you?')


