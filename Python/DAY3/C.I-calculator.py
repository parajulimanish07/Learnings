#Python Compound Interest Calculator
#This program calculates the compound interest on a given principal amount, rate of interest and time period.

#Formula to calculate compound interest annually is given by: A = P(1 + R/100) t

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("Principle amount must be greater than 0")

while rate <=0:
    rate = float(input("Enter the rate of interest: "))
    if rate <=0:
        print("Rate of interest must be greater than 0")

while time <=0:
    time = float(input("Enter the time in years: "))
    if time <=0:
        print("Time must be greater than 0")

total = principle * (1 + rate/100)**time # ** time le chai power of time vanxa 

print(f"Blanace after {time} year/s is:  ${total:.2f}") #.2f le chai 2 decimal point samma matra display garxa