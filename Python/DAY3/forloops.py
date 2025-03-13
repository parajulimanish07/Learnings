#for loops = execute a block of code a (fixed ko lagi use garne) number of times
# you can iterate over a range, string, sequence, or collection, etc



for x in range(1,11,2):  #range(start, stop, step)
    print(x)

print("Happy New Year!")

for x in range(1,21):
    if x == 13:
        continue  #skip the current iteration
        break  #exit the loop
    else:
        print(x)



    #while is better if you don't know how many times you want to loop
    #for is better if you know how many times you want to loop