#Defined with {}
#Have unique values
#Order doesn't matter

#Set with unique items
my_set = {1,2,3,4,5}
print('Set {1,2,3,4,5}')
print(my_set)
print(f'Length of this set is {len(my_set)}')
print(type(my_set))
print('\n')

#Set with repeatable items
my_set1 = {1,1,2,2}
print('Set {{1,1,2,2}')
print(my_set1)
print(f'Length of this set is {len(my_set1)}')
print('\n')

#Will return true, as it order doesn't matter
print({1,2,3} == {3,1,2})

#Will return true, as it order doesn't matter and unique items are equal
print({1,2,3} == {3,3,1,2,1,2})

#Will return false, as they are not equal
print({1,2,3} == {3,1,2,4})