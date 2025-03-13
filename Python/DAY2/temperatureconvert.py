unit = input("Enter the unit of temperature (C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32,2)
    print(f"The temperature is {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5/9,2)
    print(f"The temperature is {temp}C")
else:
    print(f"{unit} is not a valid unit of measurement")

