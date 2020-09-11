
print('Programa de evaluacion notas de alumnos')

notaAlumno = input()

def evaluacion(nota):
    valoracion = 'Aprobado'
    if nota < 5:
        valoracion = 'Reprobado'
        return valoracion

print(evaluacion(notaAlumno))