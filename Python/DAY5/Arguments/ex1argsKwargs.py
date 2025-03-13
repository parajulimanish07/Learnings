#*args and **kwargs together

def shipping_label(*args, **kwargs): #(**kwargs,*args) wont work here because args should come before kwargs in function definition
    for arg in args:
        print(arg,end=" ")
    print()


    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')},{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}")


shipping_label("Dr.","SpongeBob", "SquarePants", "III",
               street="Pineapple St",
                city="Springfield",
               # apt="123",
                pobox="PO box #1001",
                zipcode="01234",
                state="Massachusetts")