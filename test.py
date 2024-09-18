age = input("t'as quelle age?")

while not age.isdigit():
    print("T'es con ou quoi, faut l'ecrire en nombre")
    age = input("t'as quelle age ducoup?")

age = int(age)
print(type(age))

if 15 < age < 90:
    if age > 18:
        print("Mais c'est quoi ce papi de con!")
    elif age == 18:
        print("T'as 18 ans c'est clean.")
    else:
        print("AYYIIIIII T'ES MINEUR??")
else:
    print("Tu dis de la merde")