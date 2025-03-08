import random

# EJERCICIO NUMERO 4

lista = [random.randint(1, 10) for _ in range (10)]
print("Esta es la lista que se genero: " + str(lista))

resultado = [(num, num**2, num**3) for num in lista]
resultado

print("El resultado de los numeros y sus potencias es:" + str (resultado));





# EJERCICIO NUMERO 1

def abecedario(n):
    let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    res = [let[i] for i in range(len(let)) if (i+1) % n != 0]
    print res

n = int(input("Ingrese un digito: "))
print (abecedario(n))








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

