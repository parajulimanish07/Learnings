# return = statement used to end the function and return a value 


def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    return first_name + " " + last_name

full_name = create_name("manish" , "parajuli")

print(full_name)