# tuplex=(1,2,3,4,5)
# print(tuplex)
# print(type(tuplex))

# tuplex={1,2,3,4,5}
# print(tuplex)
# print(type(tuplex))

# tuplex=[1,2,3,4,5]
# print(tuplex)
# print(type(tuplex))

# for x in range (6):
#     if (x==3 or x==6):
#         continue
#     print(x,end='')


# def insert_end(self,data):
#     new_node=Node(data)
#     if self.head is None:
#         self.head=new_node
#         return
#     last=last.head
#     while(last.next):
#         last=last.next
#     last.next=new_node

# def searching(slef,value):
#     position=-0
#     found=0
#     if self.head is None:
#         print("the ll is not exists")
#     else:
#         temp=self.head
#         if temp is not None:
#             position+=1
#             if temp.value == value:
#                 print("element found at",position)
#                 found=1
#                 temp=temp.next
#             if found == 0:
#                 print("npot found")

# tower of hanoi:---
# def tower_of_hanoi(disk,source,auxiliary,target):
#     if(disk==1):
#         print ("move disk 1 from rod {} to rod{}.".format(source,target))
#         return
#     tower_of_hanoi(disk-1,source,target,auxiliary)
#     print ("move disk {} from rod{} to rod{}.".format(disk,source,target))
#     tower_of_hanoi(disk-1,auxiliary,source,target)
# disk=int(input("enter disk"))
# tower_of_hanoi(disk,'A','B','C')

# factorial:---
# import sys
# sys.setrecursionlimit(10**6)

# def factorial(n):
#     if n<0:
#         print ("not defined")
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# f=int(input("enter the no"))
# print("factorial no is:", factorial(f))

# dfs:--
# graph={2:[4,5,6],6:[8,9],2:[9,8]}
# print("graph is")
# print(graph)

# def dfs(input_graph,source):
#     stack = list()
#     visted_list = list()
#     stack.append(source)
#     visted_list.append(source)
#     while stack:
#         d=stack.pop()
#         print(d,end= " ")
#         if d in input_graph:
#             for u in input_graph[d]:
#                 if u not in visted_list:
#                     stack.append(u)
#                     visted_list.append(u)
# print("dfs is")
# dfs(graph,2)

# bfs:-----
# from queue import Queue
# graph={2:[4,5,6],7:[8,9,1],6:[8,7]}
# print("graph is")
# print(graph,3)

# def bfs(input_graph,source):
#     Q=Queue()
#     visited_list=list()
#     Q.put(source)
#     visited_list.append(source)
#     while not Q.empty():
#         vertex = Q.get()
#         print(vertex,end= " ")
#         if vertex in input_graph:
#             for u in input_graph[vertex]:
#                 if u not in visited_list:
#                     Q.put(u)
#                     visited_list.append(u)
# print("dfs is")
# bfs(graph,7)

# bracket:--
# open_list = [ "["  "{" "(" ]
# close_list= [ "]" "}"  ")" ]

# def checkp(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if stack and open_list [pos] == stack[-1]:
#                 stack.pop()
#             else:
#                 return"unbalanced"
#     if len(stack) == 0:
#         return "balanced"
#     else:
#         return "unbalanced"
# string =" [{()}"
# print ( "string" , " -" , checkp(string))
            
----------------------------

def tower_of_hanoi(disks,source,auxillary,target):
    if(disks==1)
    print('Move disk 1 from rod{}to rod{}'.format(source,target))
    tower_of_hanoi(disks-1,source,target,auxillary)
    print('move disk{}from rod{}to rod{}'.format(disks,source,target))
    tower_of_hanoi(disks-1,auxillary,source,target)
    disks=int(input('Enter the number of disks':))
    tower_of_hanoi(disks("a","b","c"))
