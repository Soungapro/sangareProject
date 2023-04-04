import random

guest_number = input("Type a guest number : ")
if guest_number.isdigit():

    guest_number = int(guest_number)
    if guest_number <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, guest_number)
guesses = 0
while True:
    guesses = + 1
    user_guest = input("Make a guest ")
    if user_guest.isdigit():
        user_guest = int(user_guest)
    else:
        print("Please enter a number next time.")
        continue
    if user_guest == guest_number:
        print("You Win!")
        break
    else:
        if user_guest > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")
print("You Win in", guesses, "guesses")
