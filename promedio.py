name = input('Escribe tú nombre:')
calif_1 = float (input('Escribe tu primer calificación: ' ))
calif_2 = float (input('Escribe tú segunda calificación: ' ))
calif_3 = float (input(' Escribe Tú tercer calificación: ' ))

prom = (calif_1 + calif_2 + calif_3) / 3 

if prom >= 7:
    print('Aprobaste la materia, felicidades!')
else:
    print('Reprobaste la materia, lo siento.')