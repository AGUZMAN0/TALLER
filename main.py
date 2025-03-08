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




