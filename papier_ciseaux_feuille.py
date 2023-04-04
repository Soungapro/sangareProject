import random
les_gains = 0
computer_gain = 0
options = ["papier", "ciseaux", "pierre"]

while True:
    user_input = input("Type papier/ciseaux/pierre : ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer pick", computer_pick + ".")
    if user_input == "pierre" and computer_pick == "ciseaux":
        print("You win!")
        les_gains += 1
    elif user_input == "papier" and computer_pick == "pierre":
        print("You win!")
        les_gains += 1
    elif user_input == "ciseaux" and computer_pick == "papier":
        print("You win!")
        les_gains += 1
    else:
        print("You lost!")
        computer_gain += 1

print("You have ", les_gains , "wins.")
print("computer have ", computer_gain, "wins.")
print("Goodbye!")

