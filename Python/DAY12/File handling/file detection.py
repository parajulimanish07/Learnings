# Python file detection


import os  # Importing the operation system module

file_path = "C:/Users/lenovo/Desktop/MQ"  # Replace with the path to your file

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")

    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The location '{file_path}' does not exist") 