         ####CONTROL FLOW BLOCKS####

##fibonacci series between 0 to 50##
# x=0
# y=1
# while y<50:
#     print(y)
#     x,y=y,x+y

##calculate the sum and average of a integer no(input form the user)input 0 to finish##
# print("input some integer to calculate their sum and average input 0 to exit")
# count=0
# sum=0.0
# number=1
# while number!=0:
#     number=int(input(""))
#     sum=sum+number
#     count+=1
# if count==0:
#     print("input some numbers")
# else:
#     print("average and sum of the above numbers are",sum/(count-1),sum)

##Demonstrate the use of for loop and nested for loop##
# #for loop=>
# n=int(input("input a number:"))
# for i in range (n):
#     print(i)
# #nested loop=>
# n=int(input("input a number:"))
# for i in range (1,n+1,1):
#     for j in range (1,i+1):
#          print(j,end='')
#     print("")

##prints all the no form 0 to 6 except 3 and 6##
# for x in range (6):
#     if(x==3 or x==6):
#         continue
#     print(x,end='')
