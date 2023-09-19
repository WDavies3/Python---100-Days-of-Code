def hello():
    print("hello there")

def hello2(name):
    print(f'hello {name}')

def hello3(name, age):
    print(f'hello {name}.  How does it feel to be {age} years old')

def sum(*nums):
    sum = 0
    for x in nums:
        sum += x
    return sum

hello()
hello2("bob")
hello3('andy', 35)
hello3(age=45, name="vanessa")
print(sum(3,4,5))
