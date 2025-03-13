
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# Using keyword arguments
greet(name="Alice", greeting="Hi", punctuation=".")
greet(greeting="Good morning", name="Bob")
greet(name="Charlie")
