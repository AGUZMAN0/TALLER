


def ejercicio2():
    frase = "Esta es mi frase"
    vowels = ['a', 'e', 'i', 'o', 'u']
    vocales = []

    for i in frase:
        if i.lower() in vowels:
            vocales.append(i)
    
    print(len(vocales))
    print(vocales)




def ejercicio3():
    frase = "El mejor regalo? El perdón..."
    list_frase = list(frase)
    print(frase)
    print(list_frase) #deben jugar con esta lista

    #Aquí va la solución...
    contador=0
    lista = []
    for i in list_frase:
        if contador==0 or contador == 1 or contador == 4 and i!=".":
            lista.append(i)
        if i==" ":
            contador+=1
        

    list_frase = lista


    nueva_frase = ''.join(list_frase)
    print(list_frase)
    print(nueva_frase)


ejercicio2()
ejercicio3()