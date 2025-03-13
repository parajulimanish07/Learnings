#Python reading files (.txt, .json, .csv)


import csv

file_path = "output.csv"


try:
    with open(file_path, "r") as file:  #this is done because we want to read the file before writing
        content = csv.reader(file) #this is done because we want to read the file before writing
        for line in content: #what this does is to read each line in the file
            print(line[0]) 

except FileNotFoundError: #this is to handle the error if the file does not exist
    print(f"The file {file_path} does not exist.") 

except PermissionError: #this is to handle the error if the file is not accessible
    print(f"You donot have permission to read that file.")
