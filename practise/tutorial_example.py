"""first programm"""

# print("hello world")

"""variable example"""
name="ritu"
age= 38.0
# print("my name is :", name)
# print("my age is :",age)

"""finding datatype(int,float,string,boolean,none) of each"""
# print(type(name))
# print(type(age))


"""Operators"""
# a=3
# b=4
# c=5
# print(a+b)
# print(a-b)
# print(a/b)
# print(a**b)
# print(a%b)
"""here modulo is used to find reminder"""

"""Practice questions-1"""
# a=int(input("enter first no:"))
# b=int(input("enter second no:"))
# print("sum=",a+b)

"""practice question 2"""
# side=int(input("enter side of square:"))
# print("area=",side*side)

"""practice 3"""
# first=float(input("enter first number:"))
# second=float(input("enter second number:"))
# print("average is:",(first+second/2))

"""string operation"""

# name =input("enter first name:")
# print(len(name))

# str="my name is ritu dubbani"
# print(str.count("i"))

"""conditional statement"""

# age=52
#
# if(age >= 18):
#     print("can apply for vote")
# elif(age <=18):
#     print("cant apply for vote")



# marks=50
# marks=int(input("enter student marks"))
# if(marks>=90):
#     print("here grade is A")
# elif(marks>=80 and marks<90):
#     print("here grade is B")
# elif(marks>=70 and marks<80):
#     print("here grade is C")
# else:
#     print("here grade is D")


"""Nesting"""
# age=94
#
# if(age>=18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

"""Tutorial 2"""
# Example 1
# num=int(input("enter number:"))
# if(num%2 == 0):
#     print("number is even")
# else:
#     print("number is odd")


# Example 2
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# num3=int(input("enter third number:"))

# if(num1>num2 and num1>num3):
#     print("num1 is greatest")
# elif(num2>num1 and num2>num3):
#     print("num2 is greatest")
# else:
#     print("num3 is greatest")

# Example 3
# num=int(input("enter number:"))
# if(num%7==0):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")

"""List operation"""
info =[55,45.5,24,88,79,"Ritu","swati"]
# print(type(marks))
# print(len(info))
# print(info[5])
# info[0]="shekhar"
# print(info[-4:-1])

"""List methods example"""
list2=[5,4,6,7,90]
# print(list)
# print(list.append(1))
"""here method not return any value"""
# print(list.sort())
# print(list.sort(reverse=True))
# print(list.reverse())
# print(list.remove(5))
# print(list.pop(1))
# list.insert(0,1)
# print(list)

"""tuples and its methods"""
# tup=(1,2,3,4,1)
# tup=(1,)
# print(type(tup))
"""Here in tuple method return value"""
# print(tup.count(1))
# print(tup.index(1))

"""test examples"""
"""first"""
# movie1=input("enter first name of movie")
# movie2=input("enter second name of movie")
# movie3=input("enter third name of movie")
# list=[movie1,movie2,movie3]
# print(list)

"""second"""
# list1=[1,3,1]
# list2=[1,2,3]

# copy_list1=list1.copy()
# copy_list1.reverse()
#
# if(copy_list1==list1):
#     print("is palindrome")
# else:
#     print("is not palindrome")
#
# copy_list2=list2.copy()
# copy_list2.reverse()
#
# if(copy_list2==list2):
#     print("is palindrome")
# else:
#     print("is not palindrome")

"""third"""

# tup=["C","D","A","A","B","B","A"]
# print(tup.count("A"))

"""fourth"""
# list=["C","D","A","A","B","B","A"]
# list.sort()
# print(list)


"""Dictionary"""

# dict={
#     "name":"ritu",
#     "count":2.9,
#     "marks":[88,67,56],
# }
# print(type(dict))
# print(dict["name"])


"""Nested Dictionary"""
# student={
#     "name":"Ritu",
#     "Score":{
#         "maths":56,
#         "eng":23,
#         "phy":45
#     }
# }
# print(student["Score"]["maths"])

"""Dictionary methods """

student={
    "name":"Ritu",
    "Score":{
        "maths":56,
        "eng":23,
        "phy":45
    }
}
# print(student.keys())
# print(student.values())
# print(len(student))
print(list(student.keys()))
### added a code











