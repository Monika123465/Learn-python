# Swapping program

x=10
y=50

temp=x
x=y
y=temp
print("value of x:",x)
print("value of y:",y)


# program to check if a no is prime or not 
#input:23
 
# num=int(input("enter a number:"))
# flag=False

# if num >1:
#     for i in range(2,num):
#         if(num%i)==0:
#             flag=True
#             break

# fibonacci series

# num=10
# n1,n2=0,1
# print("fibonacci Series:",n1,n2, end="")

# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print( n3,end="")



# print()

# find factorial of a given number

# num=int(input("enter a number:"))
# factorial=1

# if num<0:
#     print("factorial doesn't exist")
# elif num==0:
#     print("factorial is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i


#     print("factorial of given no is:",factorial)

#armsstrong
# num=int(input("enter a number:"))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=temp**3
#     temp //=10

# if num==sum:
#     print(num,"is an armsstrong number")
# else:
#     print(num,"is not a armsstrong number")


# list=["a","b","c"]
# print(list)

# list1=["a","b","c","d"]
# list1 [2]="z"
# print(list1)

# list2=["a","b","c","d","e","f"]
# list2[1:4]=["x","y","z","t"]
# print(list2)


# list3=["a","b","c","d","e","f"]
# list[1:4]=['x']
# print(list)

# list=["a","b","c","d"]
# list.append("e")
# print(list)


name=str(input("enter your name:"))
print("Hello",name,"!")
