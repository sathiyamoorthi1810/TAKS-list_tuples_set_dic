'''
1)Create a set of your favorite fruits and print it.
'''
set1 = {"apple","orange","grape","mango","pomegranate"}
print(set1)

'''
2)Add a new fruit to the set and print the updated set.
'''
set1.add("banana")
print(set1)
'''
3)Remove a fruit from the set and print the updated set.
'''
set1.remove("grape")
print(set1)
'''
4)Check if a specific fruit is in the set.
'''
print("banana" in set1)

'''
5)Create another set of fruits and find the union and intersection of both sets.
'''
set2 = {"apple","grape","pineapple","banana","watermelon"}

#union
print(set1.union(set2))
#intersection
print(set1.intersection(set2))
#difference
print(set1.difference(set2))











