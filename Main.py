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

# --------------------------------------Bucles If--------------------------------------

print('Programa de evaluacion notas de alumnos')

notaAlumno = int(input('Introduce la nota del alumno: ')) #Los inputs siempre seran strings

def evaluacion(nota):
    valoracion = 'Aprobado'
    if nota < 5:
        valoracion = 'Reprobado'
    return valoracion               #Retorna el resultado de toda la funcion

print(evaluacion(notaAlumno))

# --------------------------------------Bucles If--------------------------------------

print('Verificacion de acceso')

edadUsuario = int(input('Introduce tu edad por favor: '))

if edadUsuario < 18:
    print('No puedes pasar')
elif edadUsuario > 100:
    print('No puedes tener mas de 100 anhos')
else:
    print('Puedes pasar')

notaAlumno = int(input('Introduce tu calificacion: '))

if notaAlumno < 5: # Si escribes if en todos el flujo continua por eso se escribe el elif mejor ya que el primer if en cumplirse retornara
    print('Reprobado')
elif notaAlumno < 6:
    print('Suficiente')
elif notaAlumno < 7:
    print('Bien')
elif notaAlumno < 9:
    print('Notable')
else:
    print('Sobresaliente')

# --------------------------------------Bucles If--------------------------------------

edad = 145

if 0 < edad < 100:
    print('Edad correcta')
else:
    print('Edad incorrecta')

salarioPresidente = int(input('Introduce salario presidente '))
print('Salario presidente: ' + str(salarioPresidente))

salarioDirector = int(input('Introduce salario director '))
print('Salario director ' + str(salarioDirector))

salarioJefeArea = int(input('Introduce salario jefe area '))
print('Salario Jefe Area: ' + str(salarioJefeArea))

salarioAdministrativo = int(input('Introduce salario Administrativo '))
print('Salario Administrativo ' + str(salarioAdministrativo))

if salarioAdministrativo < salarioJefeArea < salarioDirector < salarioPresidente:
    print('Todo funciona correctamente')
else:
    print('Algo falla en esta empresa')

# --------------------------------------Bucles If--------------------------------------

print('Programa de becas Anho 2017')
distanciaEscuela = int(input('Introduce la distancia a la escuela en km: '))
print(distanciaEscuela)

numeroHermanos = int(input('Introduce el numero de hermanos en el centro: '))
print(numeroHermanos)

salarioFamiliar = int(input('Introduce salario anual bruto: '))
print(salarioFamiliar)

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    print('Tienes derecho a beca')
else:
    print('No tienes derecho a beca')

# --------------------------------------Bucles If (IN)--------------------------------------

print('Asignaturas Optativas anho 2017')
print('Asignaturas optativas: Informatica gráfica - Pruebas de Software - Usabilidad y Accesibilidad')

opcion = input('Escribe la asignatura escogida: ')
asignatura = opcion.lower()

if asignatura in ('informatica grafica', 'pruebas de software','usabilidad y accesibilidad'):
    print('Asignatura elegida ' + asignatura)
else:
    print('La asignatura escogida no esta contemplada')

# --------------------------------------Bucles If (IN)--------------------------------------

for estaciones in ["Primavera", True, 23 ]:
    print('Hola')

# ------------------------------------ Bucles for ----------------------------------------

for i in ['Pildoras','Informaticas',20]:
    print('Hola xd', end = ' ') #Con esto puedes hacer que las impresiones se hagan en una sola linea

contador = 0
miEmail = input('Introduce tu direccion de email: ')

for i in miEmail:
    if(i == '@' or i == '.'):
        contador = contador + 1

if contador == 2:
    print('Email Correcto')
else:
    print('Email incorrecto')

for i in range(3): #Ejecuta un bucle determinada cantidad de veces
    print('Hola')

# ------------------------------------ Bucles for parte 2----------------------------------------

for i in range(6): #Esto imprime numeros seguidos
    print(f'valor de la variable {i}') # La 'f' y las comillas actua como un template string, solo se elimina tambien el $ antes de{}

for i in range(12, 20, 2): # Esto inicia un rango desde 12 hasta 20 y avanza de 2 en 2
    print(f'valor de la variable {i}')

valido = False
email = input('Introduce tu email: ')

for i in range(len(email)):
    if email[i] == '@':
        valido = True

if valido:
    print('Email correcto')
else:
    print('Email incorrecto')