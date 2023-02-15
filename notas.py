notas_estudiantes = { 
    "Harry": 8.1,
    "Ron": 7.8,
    "Hermione": 9.9,
    "Draco": 7.4,
    "Neville": 6.2,
}

calificaciones_estudiantes = {}

for estudiante in notas_estudiantes:
    if notas_estudiantes[estudiante] >= 9.1:
     calificaciones_estudiantes[estudiante] = "Excelente"
    elif notas_estudiantes[estudiante] >= 8.1:
        calificaciones_estudiantes[estudiante] = "Muy Bueno"        
    elif notas_estudiantes[estudiante] >= 7.1:
        calificaciones_estudiantes[estudiante] = "Bueno"
    else:
        calificaciones_estudiantes[estudiante] = "Necesita mejorar"

print(calificaciones_estudiantes)



