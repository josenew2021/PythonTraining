#Se realiza la importacion de la libreria NUMPY 
#Se realiza la importacion de ramdom 
import numpy as np
import random

def encriptado(texto):
    texto2 = texto

    valor = 0 #Se inicia con este número la comprobación del cuadrado más cercano
              #y mayor a la cantidad de caracteres que tenga la variable 'texto'

    while True:
        if pow(valor,2) < len(texto):   #Se verifica si valor^2 < longitud de 'texto'
            valor = valor + 1
        else:                           #Si valor^2 > longitud de 'texto' ya se tiene
                                        #la dimensión mínima de una matriz cuadrada
                                        #valor x valor
            
            relleno = pow(valor,2) - len(texto) #'relleno' es la cantidad de entradas
                                                #que no llenará el texto en la matriz
                                                #valor x valor
            break                               #Acá se para la marcha del while

    
    
    for i in range(relleno):                    #Se define como agregar guiones de
                                                #pie a la variable 'texto' para llenar
                                                #la matriz valor x valor
        texto2 = texto2 + "_"

    clave = []
    mensaje_lista = []                          #Lista  vacía para llenarla con los
                                                #caracteres de la variable 'texto'
   
   
    for i in range(len(texto2)):
        entero_letra = ord(texto2[i])           #Llenado de la lista con los valores
                                                #en Unicode de los caractes de 'texto'
        mensaje_lista.append(entero_letra)
        clave.append(i)
        
        

    random.shuffle(clave)                       #Se aleatorizan las posiciones de
                                                #las letras del mensaje

    ceros1 = np.zeros(len(clave))               #Se crea un array de ceros
    i = 0
    for item in clave:                          #Se reemplazan los ceros del array
                                                #de ceros con los enteros que
                                                #representan cada letra del mensaje
                                                #en el orden de la lista de posiciones
                                                #aleatorizada
        ceros1[i] = mensaje_lista[item]
        i += 1

    mensaje_array = np.array(mensaje_lista)
    mensaje_encriptado = mensaje_array.reshape((valor,valor))

    return mensaje_encriptado, clave




def desencriptado(array_encriptado, clave):

    array1 = array_encriptado.flatten()

    ceros2 = np.zeros(len(clave))

    for item in clave:
        ceros2[item] = array1[item]

    ceros2 = ceros2.astype(int)

    lista_recuperada = ceros2.tolist()

    lista_mensaje_recuperado = []
    for codigo in lista_recuperada:
        letra = chr(codigo)
        lista_mensaje_recuperado.append(letra)

    recortador = "_"
    while recortador == "_":
        if lista_mensaje_recuperado[len(lista_mensaje_recuperado) - 1] == "_":
            del lista_mensaje_recuperado[len(lista_mensaje_recuperado) - 1]
            recortador = lista_mensaje_recuperado[len(lista_mensaje_recuperado) - 1]
        else:
            break

    texto = ""
    for i in range(len(lista_mensaje_recuperado)):
        texto = texto + lista_mensaje_recuperado[i]
