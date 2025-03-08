
frase = "Esta es mi frase"


def ejercicio2(frase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vocales = []

    for i in frase:
        if i.lower() in vowels:
            vocales.append(i)
    
    print(len(vocales))
    print(vocales)






ejercicio2(frase)