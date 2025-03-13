# dictionary = a collection of {key:value} pairs   
# ordered and changable. No duplicates

capitals = {"USA" : "Washington D.C.",
            "Nepal" : "Kathmandu",
            "India" : "Delhi",
            "China" : "Beijing"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))

#if capitals.get("Japan"):
 #   print("That capital exists")
#else: 
 #   print("That capital doesn't exist")

#capitals.update({"Germany" : "Berlin"})
#capitals.pop("China")
#capitals.popitem()#latest lai remove/pop gardincha
#capitals.clear()

#keys = capitals.keys() #to get all the keys not the value in the dictionary
#for key in capitals.keys():
#    print(key)


#values = capitals.values()
#for value in capitals.values():
#   print(value)


#TRICKY

#items= capitals.items()

#print(items) #returns dictionary items which resembles 2d list of tuples

for key, value in capitals.items(): #items le chai duitai dincha
    print(f"{key}: {value}")
