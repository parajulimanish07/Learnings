#Python quiz game

questions= ("How many elements are there in periodic table?:",
            "What is your name?:",
            "How many bones are there in human body?:")

options = (("A.116", "B.117" , "C.118", "D.119"),
           ("A.a","B.b","C.c","D.d"),
           ("A.a","B.b","C.c","D.d"))

answers = ("C" , "D" , "A")
guesses = []
score = 0
question_num= 0


for question in questions:
    print("------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1  
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1


print("------------")
print("         RESULT        ")
print("------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print ("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score/ len(questions) *100)
print(f"Your score is {score}%")