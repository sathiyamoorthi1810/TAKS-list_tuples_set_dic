'''
1)Create a tuple with your favorite colors and print it.
'''

tup = ("Red","Blue","Black","White")
print(tup)

'''
2)Access and print the first and last elements of the tuple.
'''
#first elemen acces
print(tup[0])
#last element access
print(tup[3])

"""
3)Try changing one of the elements in the tuple and observe what happens.
"""
'''
1) tuples are immutable.
2)Their contains can't be modified after creation
3) if try to change an element in a tuple , it will be get a "VALUE ERROR
'''

'''
4)Convert the tuple to a list, add a new color, and convert it back to a tuple.

'''

lst = list(tup)
print(type(lst))
lst.append("pink")
print(lst)
tup1 = tuple(lst)
print(tup1)
print(type(tup1))





















