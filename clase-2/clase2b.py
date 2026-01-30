listaEstudiantes = [
    ["Juan",20,"Full stack"],
    ["Fede",30,"Back"],
    ["Diego",40,"Front"]
]

for estudiante in listaEstudiantes:
    nombre=estudiante[0]
    edad=estudiante[1]
    rol=estudiante[2]

    print(f"Se llama: {nombre},tiene años:{edad},Se dedica:{rol}",)

    listaTabla = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(min(listaTabla))
print(max(listaTabla))

numeros = [4,8,10]
print(sum(numeros))

promedio = sum(numeros)/len(numeros)
print(promedio)

valoresBoleanos = [True,True,True]
valoresBoleanosFalse = [False,True,True]

print(all(valoresBoleanos))
print(all(valoresBoleanosFalse))
print(any(valoresBoleanosFalse))

todosPositivos = all(n>0 for n in numeros)
print(todosPositivos)

# Dupla no se puede modificar
crearDupla = (1,2,3)
duplaSimple = ("Hola",)
duplaSimpleSinParantesis = "Pizza",1
print(type(duplaSimpleSinParantesis))

fecha = (30,1,2025)
anio,*_,dia=fecha
print(anio)
print(dia)