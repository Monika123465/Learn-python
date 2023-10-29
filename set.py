thisset={"apple","banana","cherry",True,1,2}
print(len(thisset))
print(thisset)
set2={1,5,78,9,3}
set3={True,False,False}
print(set2)
print(set3)
print(type(set2))
thatset=set(("apple","banana","cherry"))
print(thatset)

for x in thisset:
    print(x)

print("banana" in thisset)
thisset.add("orange")
print(thisset)
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
mylist=["kiwi","orange"]
thisset.update(mylist)
print(thisset)