thisdict={
    "brand":"ford",
    "model1":"Mustang",
    "year":1964,
    "year":2020
}
print(thisdict)

newdict=dict(name="john",age=36,country="norway")
print(newdict)

x=thisdict.keys()
print(x)

thisdict["brand"]="audi"
print(thisdict)
x=thisdict.values()
print(x)
thisdict["year"]=2000
print(thisdict)

y=thisdict.items()
print(y)


for x in thisdict:
    print(x)

# lambda arguments:expression
x=lambda a,b:a*b
print(x(5,10))

y=lambda a,b,c:a*b*c
print(y(5,6,2))


def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(3)
print(mydoubler(11))


def tripler(n):
    return lambda a:a*n

mytripler=tripler(3)
print(mytripler(11))

class MyClass:
    x=5

p1=MyClass()
print(p1.x)
   



# thisdict["brand"]="maruti"
# print(thisdict)
# thisdict.pop("model1")
# print(thisdict)
# del thisdict["brand"]
# print(thisdict)
# thisdict.clear()
# print(thisdict)