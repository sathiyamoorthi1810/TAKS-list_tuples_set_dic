'''
1)Create a dictionary with information about a person (name, age, and city) and print it.
'''
person = {'name':'sakthi','age':25,'city':'kallakurichi'}
print(person)
'''
2)Add a new key-value pair for the person's job and print the updated dictionary.
'''
person["job"] = "developer"
print(person)
'''
3)Update the person's age and print the updated dictionary.
'''
person["age"] = 26
print(person)
"""
4)Remove the person's city from the dictionary and print the updated dictionary.
"""
person.pop("city")
print(person)
'''
5)Loop through the dictionary and print each key and value.
'''
for key, value in person.items():
    print(f"key:{key},value:{value}")



















