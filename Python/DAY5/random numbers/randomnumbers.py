import random

low = 1
high = 20  #inclusive range end point
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# number = random.randint(low, high) #random integer between 1 and 20 (inclusive) 
# number = random.random()
#option = random.choice(options)
random.shuffle(cards)

print(cards)