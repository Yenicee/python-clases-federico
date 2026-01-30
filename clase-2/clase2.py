listaNumeros = [1,2,3,4,5]
listaString = ["Hola","Adios","Libro"]

listaNumeros.append(6)
print(listaNumeros)

listaString.append("Comida")
print(listaString)

listaString.insert(1,"pizza")
print(listaString)

masEjemplos = ["C#","JS","TS"]
listaString.extend(masEjemplos)
print(listaString)

listaString.remove("Comida")
print(listaString)

# ultimo = listaString.pop()

primero = listaString.pop(0)
print(primero)

# listaString.clear()
# print(listaString)

listaNumerosDesordenador = [7,9,8,5,6]
listaNumerosDesordenador.sort()
print(listaNumerosDesordenador)

listaNumerosDesordenador.sort(reverse=True)
print(listaNumerosDesordenador)
# Lista Original
listaString.sort()
print(listaString)

# Copia Lista
copiaLista = sorted(listaString)
print(listaString)
print(copiaLista)

listaString.reverse()
print(listaString)

posicion = listaString.index("JS")
print(posicion)

listaNumerosRepetidos = [1,2,1,2,3,2,5]
cantidad = listaNumerosRepetidos.count(2)
print(cantidad)

# es como un constructor
# listaString.list()

listaTabla = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(listaTabla[1][1])

listaTabla[2][1] = 4
print(listaTabla[2])