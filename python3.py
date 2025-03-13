      ####CONTROL FLOW CONDITIONS BLOCK####

##if statement##
# num=5
# if(num<10):
    # print("num is smaller than 10")
    # print("this statement will always be executued")

##even and odd##
# number=(1,2,3,4,5,6,7,8,9)
# count_odd=0
# count_even=0
# for x in number:
#     if not x % 2:
#         count_even+=1
#     else:
#         count_odd+=1
# print("number of even number:",count_even)
# print("number of odd number:",count_odd)

##count the no of digits and letters##
# s=input("input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("letters",l)
# print("digits",d)

##find the median of three values##
# a=float(input("input first number:"))
# b=float(input("input second number:"))
# c=float(input("input third number:"))
# if a>b:
#     if a<c:
#         median=a
#     elif b>c:
#         median=b
#     else:
#         median=c
# else:
#      if a>c:
#             median=a
#      elif b<c:
#             median=b
#      else:
#             median=c
# print("the median is",median)

##demonstrate a elif-else ladder##
# score=int(input("enter the score:"))
# if score>=90:
#     print("you got  a A%")
# elif score>=80:
#     print("you got a B%")
# elif score>=70:
#     print("you got a C%")
# elif score>=60:
#     print("you got a D%")
# else:
#     print("you got a F%")