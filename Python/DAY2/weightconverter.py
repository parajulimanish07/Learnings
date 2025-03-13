#Python Weight Converter Program

weight = float(input("Enter your weight:"))
unit = input("kilograms or pounds (K or L):")

if unit == "K":
    weight = weight * 2.20462
    unit = "lbs"
    print(f"Your weight is {round(weight,1)} {unit}")

elif unit == "L":
    weight = weight / 2.20462
    unit = "kgs"
    print(f"Your weight is {round(weight,1)} {unit}")

else:
    print(f"{unit} is not a valid unit")
    

