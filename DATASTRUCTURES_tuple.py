#Once tuples are declared, you can't add to it, or change any of its values.
#they are very memory efficient
#Good for sorting lots of little things, like x,y coordinates


my_tuple = (1,2,3)
print(len(my_tuple))
print("\n")

#returns false. Order matters
print((1,2) == (2,1))