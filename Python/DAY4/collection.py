#collection = single "variable" that is used to store multiple values
# list = [] - collection of multiple values that are ordered and changeable. Duplicates are allowed
# tuple = () - collection of multiple values that are ordered and unchangeable. Duplicates are allowed
# set = {} - collection of multiple values that are unordered and unindexed. No duplicate values. FASTER than list


fruits = ("apple", "banana", "kiwi", "cherry", "banana")

#Example of list
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits) #Boolean - True or False
#fruits[1] = "pineapple"
#fruits.append("orange") #add an item to the end of the list append le add garna milcha
#fruits.remove("apple") #remove an item from the list remove le remove garna milcha
#fruits.insert(0,"pineapple") #insert an item at a specific index
#fruits.sort() #sort the list in ascending order
#fruits.reverse() #reverse the list
#fruits.clear() #remove all items from the list
#print(fruits.index('pineapple')) #return the index of the first item with the specified value
#print(fruits.count('apple')) #return the number of times the value appears in the list
#fruits.pop() #remove the last item from the list
#for fruit in fruits:
    #print(fruit)


#Example of set
#print("pineapple" in fruits) #Boolean - True or False
#fruits.add("orange") #add an item to the set
#print(fruits[0]) #error because set is unordered and unindexed
#fruits.remove("apple") #remove an item from the set
#fruits.pop() #remove the last item from the set
#fruits.clear() #remove all items from the set


#Example of tuple
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits) #Boolean - True or False

#print(fruits.count('banana')) #return the number of times the value appears in the tuple

#for fruit in fruits:
#   print(fruits)