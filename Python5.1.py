               ####TUPLE####

##diff ways of creating tuple##
#create a empty tuple#
# tuplex=tuple()
# print(tuplex)

#create a tuple with numbers#
# tuplex=25,5,4,69,74,51
# print(tuplex)

#create a tuple of one item#
# tuplex=5
# print(tuplex)
# tuplex=("tuple","false",1,2,3)
# print(tuplex)

##slice a tuple##
#create a tuple#
# tuple=32,45,87,94,56,78,65,43,22,12
# print(tuple)
#slicing a tuple#
# print(tuple[1:]) #remove first element
# print(tuple[::-1]) #the elements disprete in reverse order
# print(tuple[1:2]) #from last 2nd no it printed
# print(tuple[2::3]) #it print from last 2 gap then 3 gap

# tuple=("hello pinkiy")
# slice = 2:3:4 
# print(slice)


##find the index of an item of a tuple##
# tuplex=tuple("index.tuple")
# print(tuplex)
# index=tuplex.index("p")
# print(index)
# index=tuplex.index("p",5)
# print(tuplex)
# index=tuplex.index("e",3,6)
# print(tuplex)
# index=tuplex.index("y")
# print(tuplex)

##add an item in a tuple##
tuplex=34,56,78,98,12,43,54
tuplex=tuplex +(9,)
print(tuplex)
tuplex=tuplex[:5] + (15,20,25)
print(tuplex)
listx=list(tuplex)
tuplex=tuple(listx)
print(tuplex)