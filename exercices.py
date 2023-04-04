
liste = []
tuple1 = ()
user_input = input("Entrer une suite de chiffres separees par des virgules : ")
print(user_input)
print(type(user_input))
liste = list(user_input.split(","))
tuple1 = tuple(liste)
print(liste)
print(tuple1)
for element in liste:
    print(element)
for element1 in tuple1:
    print(element1)
print("End!")

