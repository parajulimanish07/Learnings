import time

my_time = int(input("Enter the time in seconds: ")) # user le time input garna sakcha

for x in range(my_time, 0, -1): # range function le 0 bata my_time samma ko range banako
    seconds = x % 60 # seconds nikalna ko lagi % operator use gareko ho
    minutes = int(x / 60) % 60 # minutes nikalna ko lagi / operator use gareko ho
    hours = int(x / 3600) # ek hour ma 3600 seconds huncha so hours nikalna ko lagi / operator use gareko ho
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # time format ko lagi f string use gareko ho ani seconds ko format 2 digit ma print gareko ho
    time.sleep(1) # sleep for 1 second ani loop continue huncha

print("3 seconds have passed")