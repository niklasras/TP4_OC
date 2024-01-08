nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
while nombreEtudiants < 0 :
    print("Donnez un nombre d'etudiants superieur a 0")
    nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
print("")


moyenne = 0.0
notes = []
somme = 0


for i in range(0, nombreEtudiants):

    etudiant = int(input(f"Note etudiant {i}: "))
    while etudiant < 0 or etudiant > 20:
        print(f"Entrez une note entre 0 et 20")
        etudiant = int(input(f"Note etudiant {i}: "))

    notes.append(etudiant)
    somme += etudiant
print("")


moyenne = somme/nombreEtudiants
print("La moyenne de la classe est de: ", moyenne)
print("")


print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(0, nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i]- moyenne}")
