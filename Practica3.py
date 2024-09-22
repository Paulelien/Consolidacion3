lista_magos = ["Harry Houdini", "David Blaine", "Teller"]
lista_cientificos = ["Einstein", "Hawking", "Newton"]
otros = ["Messi", "Pele", "Juanes"]
lista_completa = lista_magos + lista_cientificos + otros

# Magos grandiosos
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]
        
# Hacer grandiosos a los magos
hacer_grandioso(lista_magos)

# Función para imprimir los nombres
def imprimir_nombres(lista, titulo):
    print(titulo)
    for nom in lista:
        print(nom)
    print("----------------------------------")  # Línea en blanco para separar

# Imprimir la lista completa

imprimir_nombres(lista_completa, "Lista completa:")

# Imprimir los magos, científicos y otros
imprimir_nombres(lista_magos, "Magos grandiosos:")
imprimir_nombres(lista_cientificos, "Científicos:")
imprimir_nombres(otros, "Otros:")
