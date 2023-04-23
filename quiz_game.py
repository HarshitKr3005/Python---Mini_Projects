print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!") 

answer1 = input("What does GPU stand for? ")
if answer1.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!") 

answer2 = input("What does RAM stand for? ")
if answer2.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!") 

answer3 = input("What does PSU stand for? ")
if answer3.lower() == "power supply unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!") 

print(f"You got {score} questions correct! ")
print(f"You got {(score/4)*100}%.")