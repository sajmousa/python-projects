print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0


answer = input("What does NBA stand for? ")
if answer.lower() == "national basketball association":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("Who leads the all time scoring for the Lakers? ")
if answer.lower() == "kareem abdul-jabbar":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What is the name of Thor's new weapon? ")
if answer.lower() == "stormbreaker":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
answer = input("Who is the Avenger that can pick up Mjolnir? ")
if answer.lower() == "captin america":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
answer = input("What is the best tool to get help when stuck programming? ")
if answer.lower() == "google":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
    
