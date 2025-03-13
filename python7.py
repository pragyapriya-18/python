              ####DICTIONARY####

##denstrate create,update,get the element from dictionary##
# d={0:10,1:20}
# print(d)

# d.update({2:30})
# print(d)

# mydict={'one':20,'two':30}
# mydict['one']=56
# print(mydict)
# mydict['three']='23'
# print(mydict)

# mydict={'abs':'12','def':'34'}
# print(mydict.get('abs'))

# mydict={'x':45,'y':76}
# for dict_key,dict_value in mydict.items():
#     print(dict_key,dict_value)


##program to loop through python dictionary##
# mydict={'x':45,'y':76}
# for dict_key,dict_value in mydict.items():
#     print(dict_key,'=',dict_value)

# mydict={'x':45,'y':76}
# for key in mydict:
#     print(key)

# mydict={'x':45,'y':76}
# for value in mydict.values():
#     print(value)

##program to delete items of dictionary using diffterent methods##
# mydict={'x':45,'y':76}
# del mydict['x']
# print(mydict)

# popitem=mydict.pop('y')
# print(popitem)
# print(mydict)

# print("mydict before clear()",mydict)
# mydict.clear()
# print("mydict after clear()",mydict)

##program to check if key is present in python dictionary ornot##
mydict={'x':45,'y':76}
present='key.value' in mydict
print(present)
