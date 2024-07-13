'''
1) ceate a list ypur favourite movies and print tge list
'''

lst1 = ["Mankatha","Billa","Master","Leo","Doctor"]
print(lst1)

'''
2)Add a new movie to the list and print the updated list.

'''
lst2 = ["Iron Man","Civil war","Avengers","Emd Game"]
lst1.extend(lst2)
print(lst1)
'''
3)Remove the first movie from the list and print the updated list.

'''
lst1.remove("Mankatha")
print(lst1)

lst1.pop(0)
print(lst1)

"""
4)Sort the list of movies in alphabetical order and print it.

"""
lst1.sort()
print(lst1)

'''
5)Count the number of movies in the list.
'''
print(len(lst1))









