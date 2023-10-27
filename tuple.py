mytuple=("apple","banana","cherry","orange","kiwi","melon")
print(mytuple)
print(len(mytuple))

thistuple=("apple",)
print(type(thistuple))

tuple1=("abc",34,True,40,'male')
print(tuple1)
print(mytuple[-1])
print(mytuple[2:5])
print(mytuple[:4])
print(thistuple[2:])
print(thistuple[-4:1])

if "apple" in mytuple:
    print("yes","apple is in the fruits tuple")

x=("apple","banana","cherry")
if "papaya" in thistuple:
    print("yes","apple is in the fruits tuple") 