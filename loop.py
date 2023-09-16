# print('hello world')
# ## python is not block scpoed as like js, it is only function scoped

# def greet():
#     name1 = input("enter your anme ")
#     age = input("Enter you age: ")
#     course=input("enter your prospective course:")
#     return [name1, age,course]

# while True:
#     val = greet()
#     val.append(val[1])
#     print(val)


# superhero=input("who is your superhero?:")
# print(superhero)

# old_age=input("enter your old age:")
# new_age=int(old_age)+2        #add type function or define int/float/complex 
# print(new_age)

# a=33
# b=34
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")

# a=400
# b=240
# c=500
# if b>a:
#     print("b is greater tha a")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("a is greater than b")
# if a<b and c>a:
#     print("both condition are true")
# elif a<b or c<a:
#     print ("only one condition are true")
# else:
#     print('true for anyother condition')


# if not a <b:
#     print("a is NOT greater than b")

# x=41
# if x>10:
#     print("above ten")
# if(x>20):
#     print("and also above 20!")
# else:
#     print("but not above 20")
 
 #break
# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1

#continue

# i=1
# while i<10:
#     i+=1
#     if i==3:
#         continue
    # print(i)

    #for loops
# fruits=['apple','banana','cherry']
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break

# for x in fruits:
#     if x=="banana":
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,6):
#     print(x)

# for x in range(2,30,3):
#     print(x)

# for x in range(6):
#    print(x)
# else:
#    print("finally finished")

# for x in range(8):
#    if x==3 : break
#    print(x)
# else:
#    print("finally finished")

# # nested loop
# adj=["red","big","tasty"]
# fruits=["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in [0,1,2]:
#     pass


#function 

# def  my_function():
#     print("hello from a function")
 
# my_function()

# def my_function(fname):
#     print(fname+" "+"singh")


# my_function("Monika")
# my_function("Satyam")
# my_function("priti")

#  *  before the parameter name in the function definition.

# def my_function(*child):
#     print("The youngest child is "+child[3])

# my_function("manu","vedu","navi","sudhanshu","shantanu")


#keyword arguments

# def my_function(child3,child2,child1):
#     print("the youngest child is "+child1)


# my_function(child1="Manu",child2="vedu",child3="navi")

#**  arbitrary keyword arguments

# def my_function(**child):
#     print("his  name  is"+" " +child["fname"]+" "+child["lname"])

# my_function(fname="monika" ,lname="singh")

#default parameter value

# def my_function(country="norway"):
#     print("I am from "+country)


# my_function("India")
# my_function("bangaladesh")
# my_function("Brazil")
# my_function()

# a list of arguments
# def my_function(food):
#     for x in food:
#         print(x)

# fruits=["apple","banana","cherry"]
# my_function(fruits)

# def tri_recursion(k):
#     if(k>0):
#         result=k+tri_recursion(k-1)
#         print(result)
#     else:
#         result=0
#         return result
    
# print("\n\nRecursion Example Results")
# tri_recursion(6)

#lambda 

# x=lambda a:a+10
# print(x(5))

# y=lambda a,b:a*b
# print(y(7,8))

# z=lambda a,b,c :a+b+c
# print(z(5,6,7))


# def myfunc(n):
#     return lambda a:a**n

# mydoubler=myfunc(3)
# print(mydoubler(4))


