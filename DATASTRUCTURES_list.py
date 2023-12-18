### Lists ###
my_list = [1,2,3,4]
print(my_list)
print(f"{len(my_list)}\n")

my_list2 = ['list', 'of', 'strings']
print(my_list2)
print(f"{len(my_list2)}\n")

my_list3 = [1, 'list', False, []]
print(my_list3)
print(f"{len(my_list3)}\n")

my_list4 = [[1,2,3], [False, True], [], my_list]
print(my_list4)
print(f"{len(my_list4)}")
print(my_list4[0][1])

# Will return false as position matters
print([1,2,3]==[3,2,1])

# Will return true
print([1,2,3]==[1,2,3])

