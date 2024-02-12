# creating an epmty set
b = set()
print(type(b))
# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # adding a value repeatedly does not changes a set
b.add((4,5,6))
# We cannot add list or dictionary to sets
# b.add([4,5,6])
# b.add({4;5})
print(b)
print(len(b))# prints the length of this set
b.remove(5)
print(b)
# b.remove(15) throws an error while trying to emove 15 
b.pop() #it remove random values from the sets
print(b)
