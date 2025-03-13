#Iterables =  An obj/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop.  
# lists, tuples, strings, dictionaries, sets, and range objects are all iterable.

my_dictionary = {"name": "John", "age": 30, "city": "New York"}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
