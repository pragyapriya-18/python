def tower_of_hanoi(disk,source,auxiliary,target):
    if (disk==1):
        print("move disk 1 from rod {} to rod {}.".format(source,target))
        return
        # Function call itself
    tower_of_hanoi(disk-1,source,target,auxiliary)
    print("move disk {} from rod {} to rod {}.".format(disk,source,target))
    tower_of_hanoi(disk-1,auxiliary,source,target)
disk=int(input("enter the number of disks:"))
# we're referencing source as 'A',auxiliary as 'B', target as 'C'
tower_of_hanoi(disk,'A','B','C')