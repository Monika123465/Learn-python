#Swapping program

# x=10
# y=50

# temp=x
# x=y
# y=temp
# print("value of x:",x)
# print("value of y:",y)


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

num=10
n1,n2=0,1
print("fibonacci Series:",n1,n2, end="")

for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print( n3,end="")



print()




