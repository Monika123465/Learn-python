print('hello world')
## python is not block scpoed as like js, it is only function scoped

def greet():
    name1 = input("enter your anme ")
    age = input("Enter you age: ")
    course=input("enter your prospective course:")
    return [name1, age,course]

while True:
    val = greet()
    val.append(val[1])
    print(val)





# print(greet())
# val = greet()
# print(val)


