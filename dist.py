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


