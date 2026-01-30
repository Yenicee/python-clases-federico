#DIFERENCIAS CLAVES 
# if(edad > 18){
    
# }

# edad = 20
# if edad > 18:
    
    
x = 89
y =738

# variable comun 
nombre = "Juan"
PI = 3.4656 #MAYUSCULA INDICA CONSTANTE (pero no es inmutable)

# es valido de usar comparaciones multiples 
edad = 25
if 18 <= edad < 65:
    print(
        'edad laboral'
    )
    
#f-strings (como template de JS ) ${}
print(f"hola {nombre}, soy nuevo")
txt = """este es un texto  multilinea 
"""

#metodos strtings
texto = "hola mundo, todo bien"
print(texto.upper()) 
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.startswith("mundo"))
print(texto.endswith("mundo"))

print("Data" in texto) 
#indice negativo
print(texto[-1])

# 0:3  :4 : 3: ::2  ::-1 

#tuplas son como listas , inmutables 
mi_tupla = (1,2,3,"hola")

#diccionario son como los objetos en JS , pares clave-valor
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "cualidades": ["amable", "inteligente"]
}

#acceder
print(persona["nombre"])
print(persona.get("edad"))
