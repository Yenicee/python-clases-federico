""" 
    SETS - OPERACIONES Y MÉTODOS
    Los sets son una estructura que NO existe en JavaScript (al menos no nativamente hasta ES6). 
    Son como listas pero con dos diferencias clave: 1) No tienen orden, 2) No permiten duplicados. 
    Son súper útiles para eliminar duplicados y hacer operaciones matemáticas de conjuntos."
    """
    
# Crear sets
numeros_set = {1, 2, 3, 4, 5}
lenguajes_set = {"Python", "JavaScript", "Java"}

# Set vacio (NO usar {}, eso es un diccionario vacio)
set_vacio = set()  # Correcto


# Crear set desde lista (elimina duplicados automaticamente)
numeros_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
numeros_unicos = set(numeros_con_duplicados)
print(numeros_unicos)  # {1, 2, 3, 4, 5}

# Sets NO tienen orden (no se puede acceder por índice)
# print(numeros_set[0])  # Error

# Sets NO permiten duplicados
lenguajes = {"Python", "JavaScript", "Python", "Java"}
print(lenguajes) 

# "Los sets son perfectos cuando necesitas asegurarte de que no haya duplicados. 
# Por ejemplo, si tenés una lista de emails de usuarios 
# y queres saber cuantos usuarios unicos hay, convertis la lista a set."

#Metodos 
# Crear set
lenguajes = {"Python", "JavaScript"}

# 1. ADD - Agregar un elemento
lenguajes.add("Java")
lenguajes.add("Python")  # No hace nada (ya existe)
print(lenguajes) 

# 2. REMOVE - Eliminar (da error si no existe)
lenguajes.remove("Java")
lenguajes.remove("C++")  # Error! KeyError

# 3. DISCARD - Eliminar (NO da error si no existe)
lenguajes.discard("Java")  # No hace nada (ya no existe)
lenguajes.discard("C++")   # No da error

# 4. POP - Eliminar y retornar un elemento aleatorio
lenguaje = lenguajes.pop()
print(lenguaje)  # Retorna alguno (orden aleatorio)

# 5. CLEAR - Vaciar el set
lenguajes_copia = lenguajes.copy()
lenguajes_copia.clear()
print(lenguajes_copia) 

# 6. IN - Verificar pertenencia (MUY RAPIDO en sets)
print("Python" in lenguajes) 


#OPERACIONES DE CONJUNTOS
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 1. UNION - Todos los elementos de ambos sets (sin duplicados)
union = set_a | set_b  # Operador |

union = set_a.union(set_b)
print(union) 

# 2. INTERSECCION - Solo elementos que estan en AMBOS sets
interseccion = set_a & set_b  # Operador &

interseccion = set_a.intersection(set_b)
print(interseccion) 

# 3. DIFERENCIA - Elementos en A pero NO en B
diferencia = set_a - set_b  # Operador -

diferencia = set_a.difference(set_b)
print(diferencia) 

# 4. DIFERENCIA SIMETRICA - Elementos en A o B pero NO en ambos
dif_simetrica = set_a ^ set_b  # Operador ^

dif_simetrica = set_a.symmetric_difference(set_b)
print(dif_simetrica)

# EJEMPLO PRACTICO: Analisis de habilidades
skills_federico = {"Python", "JavaScript", "React", "Node"}
skills_requeridas = {"Python", "SQL", "Machine Learning", "JavaScript"}

# Que skills tiene Federico de las requeridas?
skills_match = skills_federico & skills_requeridas
print(f"Skills que cumple: {skills_match}")  

# Que skills le faltan?
skills_faltantes = skills_requeridas - skills_federico
print(f"Skills faltantes: {skills_faltantes}") 

# Que skills extra tiene?
skills_extra = skills_federico - skills_requeridas
print(f"Skills extra: {skills_extra}")  

"""Las operaciones de conjuntos son MUY utiles en analisis de datos. 
   Por ejemplo, si tenes dos listas de clientes
   y queres saber que clientes estan en ambas listas
   o solo en una (diferencia), los sets son perfectos para eso.
"""


#CUANDO USAR SETS
# CASO 1: Eliminar duplicados
emails = ["juan@email.com", "maria@email.com", "juan@email.com", "pedro@email.com"]
emails_unicos = list(set(emails))
print(emails_unicos) 

# CASO 2: Verificacion rapida de pertenencia
# Sets son MUCHO mas rapidos que listas para verificar si un elemento existe
# Lista: O(n) - tiene que revisar elemento por elemento
# Set: O(1) - verificacion instantanea

# Malo (lista):
usuarios_lista = ["user1", "user2", "user3", ... ]  # 1 millon de usuarios
if "user500000" in usuarios_lista:  # Lento!
    print("Usuario existe")

# Bueno (set):
usuarios_set = {"user1", "user2", "user3", ... }  # 1 millon de usuarios
if "user500000" in usuarios_set:  # Instantaneo!
    print("Usuario existe")
    
    """
     En Machine Learning, cuando trabajes con features o categorias, 
     los sets te van a servir mucho para encontrar valores unicos,
     hacer comparaciones rapidas, y eliminar duplicados.
    """



#DICCIONARIOS AVANZADOS#
persona = {
    "nombre": "Federico",
    "edad": 30,
    "ciudad": "España",
    "skills": ["Python", "JavaScript"]
}

# 1. KEYS - Obtener todas las claves
claves = persona.keys()
print(claves) 
print(list(claves)) 

# 2. VALUES - Obtener todos los valores
valores = persona.values()
print(valores)  
print(list(valores)) 
# 3. ITEMS - Obtener pares (clave, valor)
items = persona.items()
print(items)

# Iterar sobre items 
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 4. GET con valor por defecto
edad = persona.get("edad", 0)  # Si no existe, retorna 0
print(edad) 

pais = persona.get("pais", "Desconocido")  # No existe 'pais'
print(pais)  

# 5. UPDATE - Actualizar con otro diccionario
info_adicional = {
    "profesion": "Full Stack Developer",
    "años_experiencia": 2
}
persona.update(info_adicional)
print(persona)

# 6. POP - Eliminar y retornar valor
edad = persona.pop("edad")
print(edad) 
print(persona)  # Ya no tiene 'edad'

# 7. POPITEM - Eliminar y retornar ultimo par (clave, valor)
ultimo = persona.popitem()
print(ultimo)  

# 8. SETDEFAULT - Obtener valor o establecer si no existe
persona = {"nombre": "Federico"}
edad = persona.setdefault("edad", 30)
print(edad)  
print(persona) 

nombre = persona.setdefault("nombre", "Juan")  # Ya existe, no cambia
print(nombre)

#VERIFICACION Y BUSQUEDA#
persona = {
     "nombre": "Federico",
     "edad": 30,
     "ciudad": "España"
}

# Verificar si existe una CLAVE
print("nombre" in persona)  
print("apellido" in persona)

# Verificar si existe un VALOR 
print("Federico" in persona.values())  
print(30 in persona.values())  

# Buscar clave por valor (manual)
def buscar_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None

clave = buscar_clave_por_valor(persona, "España")
print(clave)

#DICCIONARIOS ANIDADOS ##
# Diccionario de diccionarios (muy comun en JSON/APIs)  esto ya lo has visto en JS
empresa = {
    "empleado1": {
        "nombre": "Federico",
        "edad": 30,
        "departamento": "Desarrollo"
    },
    "empleado2": {
        "nombre": "María",
        "edad": 25,
        "departamento": "Data Science"
    }
}

# Acceder a valores anidados
print(empresa["empleado1"]["nombre"]) 
print(empresa["empleado2"]["departamento"]) 

# Modificar valores anidados
empresa["empleado1"]["edad"] = 31

# Agregar nuevo empleado
empresa["empleado3"] = {
    "nombre": "Juan",
    "edad": 28,
    "departamento": "Backend"
}

# Iterar sobre diccionario anidado
for id_empleado, datos in empresa.items():
    nombre = datos["nombre"]
    edad = datos["edad"]
    dpto = datos["departamento"]
    print(f"{id_empleado}: {nombre}, {edad} años, {dpto}")

