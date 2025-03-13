           ####LIST####
##access the index of list##
# num=[5,15,35,8,98]
# for num_index,num_val in enumerate(num):
#     print(num_index,num_val)

##sum all the items in a list##
# s=0
# list=[2,3,4,5]
# for x in list:
#     s=s+x
# print(s)

##or
##error
# list=[]
# num=int(input("how many numbers:"))
# for n in range(num):
#     numbers=int(input("enter numbers:"))
#     list.append(numbers)
# print("sum of elements in given list is:",sum list)


##get the largest and smallest no from a list##
##largest
# list1=[10,29,4,67,65]
# list1.sort()
# print(list1)
# a=list1[-1]
# print("the largest item in the list:",a)
# #smallest
# list1=[10,29,4,67,65]
# list1.sort()
# print(list1)
# a=list1[0]
# print("the smallest item in the list:",a)

##remove duplicates from a list##
# a=[10,20,30,40,20,50,20,60,30]
# dup_items=set()
# unique_item=[]
# for x in a:
#     if x not in dup_items:
#         unique_item.append(x)
#         dup_items.add(x)
# print(dup_items)

# a=[46,39,56,38,46,39]
# unq_item=[]
# for x in a:
#     if x not in unq_item:
#         unq_item.append(x)
# print(unq_item)