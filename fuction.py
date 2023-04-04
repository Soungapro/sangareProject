def Table_Multiplication(multiplicateur, valeur_initiale, valeur_finale):

    for i in range(valeur_initiale, valeur_finale + 1):
        print(valeur_initiale, " x " , multiplicateur ,"=", valeur_initiale*multiplicateur)
        valeur_initiale += 1
Table_Multiplication( multiplicateur = int(input("saisir le nombre multiplicateur : ")),
                      valeur_initiale = int(input("saisir la valeur initiale : ")),
                      valeur_finale = int(input("entrer la valeur superieure : ")))

