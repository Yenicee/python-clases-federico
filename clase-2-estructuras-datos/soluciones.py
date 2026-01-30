# ==========================================
# EJERCICIO INTEGRADOR - CLASE 2
# ==========================================
# Sistema de Gestión de Cursos Online
#
# Vas a crear un programa que gestione información de cursos,
# estudiantes y sus inscripciones usando todas las estructuras
# que vimos hoy.

# PARTE 1: Crear datos
# Crear una lista de cursos (cada curso es un diccionario)
cursos = [
    {
        "id": 1,
        "nombre": "Python para Data Science",
        "duracion_horas": 40,
        "estudiantes": ["Federico", "María", "Juan"]
    },
    {
        "id": 2,
        "nombre": "Machine Learning Básico",
        "duracion_horas": 60,
        "estudiantes": ["Federico", "Pedro", "Ana"]
    },
    {
        "id": 3,
        "nombre": "Deep Learning",
        "duracion_horas": 80,
        "estudiantes": ["María", "Ana", "Carlos"]
    }
]

# PARTE 2: Análisis de datos

# 1. Usar SETS para encontrar:
#    - Todos los estudiantes únicos (sin duplicados)
#    - Estudiantes que están en "Python para Data Science" Y "Machine Learning"
#    - Estudiantes que están solo en uno de esos dos cursos

# Tu código aquí:


# 2. Usar LISTAS para:
#    - Ordenar los cursos por duración (de menor a mayor)
#    - Encontrar el curso con más estudiantes
#    - Calcular el promedio de duración de todos los cursos

# Tu código aquí:


# 3. Usar DICCIONARIOS para:
#    - Crear un nuevo diccionario que tenga como clave el nombre del estudiante
#      y como valor la lista de cursos en los que está inscrito
#    Ejemplo: {"Federico": ["Python para Data Science", "Machine Learning Básico"], ...}

# Tu código aquí:


# 4. Usar TUPLAS para:
#    - Crear una función que retorne (nombre_curso, cantidad_estudiantes)
#      del curso con más estudiantes

# Tu código aquí:


# PARTE 3: Modificaciones

# 5. Agregar un nuevo estudiante "Laura" a "Python para Data Science"
# 6. Eliminar a "Carlos" de "Deep Learning"
# 7. Crear un nuevo curso "SQL para Análisis" con 3 estudiantes
# 8. Mostrar un resumen final con formato bonito (print(f'Resumen con este formato lindo {} '))