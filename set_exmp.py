s1 = {
    "name", "name", "age","addreess", "address",
}

print(s1)


# s2 = {
#     {
#         "name": "John",
#         "age": 30,
#         "address": "123 Main St"
#     },
#     {
#         "name": "Jane",
#         "age": 25,
#         "address": "456 Elm St"
#     }
# }

''' 
No, dictionaries (dict) are not allowed as elements in a set. This is
 because set elements must be immutable and hashable, but dictionaries
   are mutable and unhashable. That’s why trying to add a dictionary to 
   a set will raise a TypeError.
'''

# print(s2)

s3 = {
    "name": "John"
}


# s3.__hash__() # TypeError: unhashable type: 'dict'


name = "John"

print(name.__hash__() ) # This will return a hash value since strings are immutable and hashable.