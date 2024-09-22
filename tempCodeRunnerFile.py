lista_magos= ["Harry Houdini", "David Blaine", "Teller"]
lista_cientificos= ["Einstein", "Hawking","Newton" ]
otros=["Messi", "Pele", "Juanes"]
lista_completa = ["Harry Houdini", "David Blaine", "Teller", "Einstein", "Hawking","Newton","Messi", "Pele", "Juanes" ]

def hacer_grandioso (mago1, mago2, mago3):
    print ("El gran", mago1)
    print ("El gran", mago2)
    print ("El gran", mago3)
    

hacer_grandioso ("Harry Houdini", "David Blaine", "Teller")

print ("----------------------------------------------------")

def imprimir_nombres (lista_completa): 
    for lista in lista_completa:
       print (lista)

imprimir_nombres (lista_completa)

imprimir_nombres (lista_magos, lista_cientificos, otros)

imprimir_nombres(lista_magos, "Magos grandiosos: ")
imprimir_nombres(lista_cientificos, "Científicos: ")
imprimir_nombres (otros, "Otros: ")