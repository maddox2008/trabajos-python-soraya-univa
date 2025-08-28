lista5 = []

lista = ["maddox", 5, -9, False, "buenrostro", 1011]
lista2 = [5, 8, 1, 0, 6]

print(lista)
print(lista[0:3])
print(lista[0:2])
print(lista[1:])

lista.append("maddox")
lista.insert(2, "buenrostro")
lista.extend(["hola", 8])
lista2.sort()
lista.reverse()
lista.remove("buenrostro")

print(lista2)

for l in lista:
    print(l)
