#List comprehension = a concise way to create lists
# It is faster, compact and more readable than using a for loop
# Syntax: [expression for item in iterable if condition]

#fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#fruit_chars = [fruit[0] for fruit in fruits] #return the first character of each fruit
 

#print(fruit_chars)


#numbers = [ 1, -2, 3, -4, 5, -6, 7, -8, 9, -10 ]
#positive_nums=[num for num in numbers if num >=0]
#negative_nums=[num for num in numbers if num <0]
#even_nums = [ num for num in numbers if num%2==0]
#odd_nums = [ num for num in numbers if num%2==1]

#print(positive_nums)
#print(negative_nums)
#print(even_nums) 
                   
#print(odd_nums)


grades = [85, 92,55,54, 78, 88, 95, 75, 90]

passing_grades = [grade for grade in grades if grade>=60]


print(passing_grades)
