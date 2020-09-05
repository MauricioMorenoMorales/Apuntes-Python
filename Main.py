# ------------------------------------Listas------------------------------------

mi_lista=['maria','pepe','marta','antonio','pablo','andres','jorge']
mi_lista.insert(2,"Xd")
print(mi_lista[0:3])
print(mi_lista[3:])
print(mi_lista[:3])
print(mi_lista.index('pepe'))
print('pepe' in mi_lista)
mi_lista.remove("pepe")

mi_lista2=['diana','javier','emilio']*9
mi_lista.pop()
print(mi_lista)
print('pepe' in mi_lista)
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

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