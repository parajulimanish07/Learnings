#Python writing files (.txt, .json, .csv)

#.json is made of key value pairs, separated by commas and enclosed in curly braces.


import json
import csv

employee = [["Name", "Age", "Department"],
            ["Manish", 30, "HR"],
            ["Spongebob", 22, "Finance"],
            ["Sandy","18","Scientist"]]
file_path = "output.csv" #location ja ko rakhda ni huncha 


#mode "w" is used to write data to a file


try:
    with open(file=file_path, mode= "w", newline="") as file: #with will close the file and return the file object automatically
        writer = csv.writer(file) #this will write data to the file
        for row in employee: #this will iterate over each row in the employee list
            writer.writerow(row) #this will write a row of data to the file
        print(f"csv file {file_path} was created successfully")
except FileExistsError:
    print("That file already exists.")
