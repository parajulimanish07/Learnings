#2dlist = [[list1], [list2], [list3]]
#2d list vitra tuples, list, dict, set, etc. haru jun ni rakhna milcha 

fruits = ["apple", "banana", "cherry"] #1d list
vegetables = ["carrot", "lettuce", "onion"]
meats = ["chicken", "buff", "pork"]

grocery = [fruits, vegetables, meats]

#print(grocery[0][2]) #[0] = fruits, [2] = cherry

for collection in grocery:
    for food in collection:
        print(food, end = " ")
    print() #new line