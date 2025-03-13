# logical operators = evaluate multiple expressions (and, or, not)
# and = returns True if both statements are true
# or = returns True if one of the statements is true
# not = reverse the result, returns False if the result is true

# Example 1

temp = 35 
is_raining = False

if temp >= 35 and is_raining:
    print("The weather is hot and raining")
    print("It is not suitable for outdoor event")

elif temp <= 0 and is_raining:
    print("The weather is cold and raining")

elif 28 > temp > 0 and is_raining:
    print("The weather is warm and raining")

elif temp >= 35 and not is_raining:
    print("The weather is hot and cloudy")
    print("It is not suitable for outdoor event")

elif temp <= 0 and not is_raining:
    print("The weather is cold and cloudy")
    
elif 28 > temp > 0 and not is_raining:
    print("The weather is warm and cloudy")