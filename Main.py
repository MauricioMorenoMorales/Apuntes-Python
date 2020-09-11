# ------------------------------------Listas------------------------------------

miLista = ['Maria','Pepe','Marta','Antonio','Mauricio','Gabriela']
print(miLista[:])#Forma correcta de imprimir listas
print(miLista[2])#Imprime una posición de la lista solamente
print(miLista[-2])#Empieza a contar desde el final al inicio
print(miLista[2:4])#Imprime una porcion de la lista
print(miLista[2:])#Imprime de la posición 2 en adelante
print(miLista[:2])#Imprime hasta la posición 2
print(miLista[-2:])#Imprime hasta la posición 2 en reversa
print(miLista[:-2])#Imprime hasta la posición 2 en reversa que sería la posicion 4 normal

miLista.append('Sandra')#Agrega al final
print(miLista[:])
miLista.insert(2,'Samuel')#Agrega en cierta posicion (2)
print(miLista[:])
miLista.extend(['Sandra','Ana','Lucia'])#Agrega una porción
print(miLista[:])
print(miLista.index('Sandra'))#Imprime la primera posicion en la que encuentre un 'sandra',
print('Pepe' in miLista)#Devuelve True si se encuentra el primer parametro -in- una lista

miLista2 = ['Maria',5, True, 88.45]
miLista2.remove('Maria')#Elimina un valor de la lista
print(miLista2)
miLista2.pop()#Elimina la ultima posición
print(miLista2)
miLista3 = miLista + miLista2 #Se pueden fusionar varias listas por este metodo
print(miLista3)

# --------------------------------------Tuplas--------------------------------------

mitupla = ('Juan',12,33,1994);
# mitupla.append('Pepe') dará error ya que no se puede agregar contenido a las tuplas
print(mitupla[2]) #Acceder a valores
milista = list(mitupla) #Convertir tupla en listas
print(milista)
print(mitupla)
misegundatupla = tuple(milista) #convertir lista en tuplas
print(misegundatupla)
print('Juan' in mitupla) #Ver si una tupla contiene algo
print(mitupla.count(12)) #Ver en que posición se encuentra el valor del parametro
print(len(mitupla))

tuplaunitaria = ('juan',) # Tiene que tener una coma al final
print(len(tuplaunitaria))

tuplSinParantesis = 'juan',13,1,1995 #Empaquetado de tupla
print(tuplSinParantesis)

tuplaEmpaquetada = ('Juan',13,1,1995)
nombre, dia ,mes ,anho = tuplaEmpaquetada #Separar en varias variables el contenido de una tupla
print(nombre)
print(mes)
print(dia)
print(anho)

# --------------------------------------Diccionarios--------------------------------------

miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espanha":"Madrid"}
print(miDiccionario["Francia"]); #Asi se accede directamente a un valor
print(miDiccionario['Espanha'])
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)
miDiccionario["Italia"] = "Roma" #Asi se reescribe el valor de una unidad
print(miDiccionario)
del miDiccionario["Reino Unido"] #Así se elimina una parte de un diccionario
print(miDiccionario)

miDiccionario2 = {'Alemania':'Berlin',23:'Jordan','Mosqueteros':3}
print(miDiccionario2)

mitupla = ['Espnha','Francia','Reino Unido','Alemania']
miDiccionario3 = {mitupla[0]:'Madrid',mitupla[1]:'Paris',mitupla[2]:'Londres',mitupla[3]:'Berlin'}
print(miDiccionario3)

miDiccionario4 = {23:'Jordan','Nombre':'Michael','Equipo':'Chicago','Anillos':[{'temporadas' : [1991,1992,1993,1996,1997,1998]}]}
print(miDiccionario4)
print(miDiccionario4['Anillos'])
print(miDiccionario4.keys())
print(miDiccionario4.values())
print(len(miDiccionario4))