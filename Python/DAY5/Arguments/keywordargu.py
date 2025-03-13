#keyword arguments = an argument that allows you to pass a value to a function by name, rather than by position
# helps with readability and code organization
# 1.positional 2.default 3. keyword 4.arbitary

#def hello(greeting, title, first, last):
 #   print(f"{greeting}, {title} {first} {last}!")

#hello("Hello", last="Doe", first="John", title="Mr") #keyword arguments is followed by positional arguments

#print("1","2","3","4","5", sep="*") #sep is used to separate the elements in the output string

def get_phone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}{last}"

phone_num = get_phone(country_code=61, area_code=123,first=456,last="1234")

print(phone_num)


#preceded by an identifier that matches the parameter name in the function definition