num_pad =((1,2,3),
          (4,5,6),
          (7,8,9)
          ,("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print() #new line

    #grid or matrix of data ko lagi 2d list use garda milcha