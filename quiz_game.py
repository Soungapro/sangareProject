print("Welcome to my computer quiz !")

playing = input("Do you want to play ?").lower()

if playing != "yes":
    quit()
print("Okay! let's play :)")

score = 0

answer = input("what does CPU stand for ?").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("what does GPU stand for ?").lower()
if answer2 == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("what does RAM stand for ?").lower()
if answer3 == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("what does PSU stand for ?").lower()
if answer4 == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("you got " + str(score) + " questions correct !")

print("you got " + str((score / 4) * 100) + "%.")