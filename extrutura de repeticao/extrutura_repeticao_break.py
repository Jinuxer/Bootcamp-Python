#while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break
#    print(numero)


# Outro exemplo com for usando break ----------------------------

#for numero in range(100):
    
#    if numero == 15:
#        break

#    print(numero, end=" ")


# Outro exemplo com for usando continue ----------------------------

#for numero in range(100):
    
#    if numero == 12:
#        continue

#    print(numero, end=" ")


# Outro exemplo com for usando continue para numeros impares----------------------------
#for numero in range(100):
    
#    if numero % 2 == 0:
#        continue

#    print(numero, end=" ")


# Outro exemplo com break e continue----------------------------
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
