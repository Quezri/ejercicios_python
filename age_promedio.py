edad = int (input('Escribe tú edad: '))
promedio = float (input('Escribe tú promedio: '))

if edad < 6:
    print ('kinder')
elif edad >= 6 and edad < 12:
    print ('primaria')
    if promedio >= 9.5:
        print('Tienes un promedio aceptable')
    else:
        print ('Tienes promedio inaceptable')
elif edad >= 12 and edad <15:
    print ('Secundaria')
    if promedio >= 9.5:
        print('Tienes un promedio aceptable')
    else:
        print ('Tienes promedio inaceptable')
elif edad >= 15 and edad <18:
    print ('Bachillerato')
    if promedio >= 9.5:
        print('Tienes un promedio aceptable')
    else:
        print ('Tienes promedio inaceptable')
elif edad >= 18 and edad <23:
    print ('Universidad')
    if promedio >= 9.5:
        print('Tienes un promedio aceptable')
    else:
        print ('Tienes promedio inaceptable')
else:
    print ('Profesionista')
