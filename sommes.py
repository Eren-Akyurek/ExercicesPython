# Créer un algorithme qui calcule la somme des éléments d'une liste.
# Exemple :
# Entrée : [1, 2, 3, 4]
# Sortie : 10
def somme_liste(liste):
    somme = 0
    for element in liste :
        somme += element
    return somme

print(somme_liste([1,2,3,4]))


# Écrire un script qui trouve le plus grand nombre dans une liste.
# Exemple :
# Entrée : [3, 58, 11, 21]
# Sortie : 58
def plus_grand_nombre(liste) :
    max_nombre = liste[0]
    for nombre in liste :
        if nombre > max_nombre:
            max_nombre = nombre
    return max_nombre

print(plus_grand_nombre([3,58,11,21]))


# Développer une fonction qui calcule la factorielle d'un nombre.
# Exemple :
# Entrée : 5
# Sortie : 120 (car 5! = 5 x 4 x 3 x 2 x 1)
def calcule_factirielle(nombre) :
    factoriel = 1
    for i in range (1, nombre + 1):
        factoriel *= i
    return factoriel

print(calcule_factirielle(5))


# Créer un programme qui vérifie si un mot est un palindrome (se lit de la même manière dans les deux sens).
# Exemple :
# Entrée : "radar"
# Sortie : True
def palindrome(mot):
    debut = 0
    fin = len(mot) - 1
    while debut < fin:
        if mot[debut] != mot[fin]:
            return False 
        debut += 1
        fin -= 1
    return True

print(palindrome("radar")) # A reessayer a la maison + chercher des exos sur ytb ou chat gpt


# Écrire un script qui compte le nombre de mots dans une phrase.
# Exemple :
# Entrée : "Le test logiciel est essentiel"
# Sortie : 5
def compter_mots(phrase):
    mots = phrase.split(' ')  #split -> ajoute +1 a "mots" a chaques espaces
    return len(mots)

print(compter_mots("Le test logiciel est essentiel"))


# Challenge a checker sur yt-fonction recursive = fonction qui s'appelle elle même

def somme_recursive(liste):
    total = 0
    for element in liste :
        if isinstance(element, list): #fonction isinstance verifie que l'on rentre dans une liste
            total += somme_recursive(element)
        else:
            total += element
    return total

print(somme_recursive ([5, 2, 8, [5, [99, 5], 6, 10], 5, 9, [9, [5,[]]]]))