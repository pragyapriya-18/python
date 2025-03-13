               ####ARRAY####
##5 int and display in array items
# from array import*
# pp=array('i',[5,3,7,8])
# for i in pp:
#     print(i)
# print('access first three times')
# print(pp[0])
# print(pp[1])
# print(pp[2])

##append a new item
# from array import*
# pp=array('i',[5,3,7,8])
# print("original array is" + str (pp))
# print("append 11 at the end of the array ")
# pp.append(12)
# print(pp)

##get the no of occurrences of specified element in an array
from array import*
pp=array('i',[5,3,7,8])
print("original array is" + str (pp))
print("no of occurences of the no 3 is " + str(pp.count(3)))
