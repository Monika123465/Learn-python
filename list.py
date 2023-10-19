thislist=list(("apple","banana","cherry"))
print(thislist)

mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
mylist[2]="papaya"
print(mylist)
print(type(mylist))
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[-4:-1])
mylist[1:3]=["blackcurrant","watermelon"]

print(mylist)
if "papaya" in thislist:
    print("yes,'apple' is  in the fruit list")
elif "banana" in thislist:
    print("yes it is in the list")
else:
    print("not present in the list")

list=["monika","satyam","prakriti","nishi","jyoti","swati","shilpa"]
list[2:5]=["beauty","puja","priti","suhani"]
list.insert(2,"shreya")

list.append("manvi")
print(list)

newlist=["apple","banana","cherry"]
tropical=["mango","pineapple","papaya"]
newlist.remove("banana")
newlist.pop(1)
newlist.append("banana")
# del newlist
thistuple=("kiwi","orange")
# newlist.clear()
# newlist.extend(thistuple)
print(newlist)
for x in newlist:
    print(x)

    thisnewlist=['hello ' for x in newlist]
    print(thisnewlist)

mylist.sort()
mylist.sort(reverse=True)
print(mylist)