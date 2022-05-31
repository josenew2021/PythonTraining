def modificar_materia(pensum, semestre, materia, nombre, creditos):
   

    if semestre not in range(1, len(pensum) + 1):
        mensaje = 'Ingrese un semestre válido'
    
    elif len(pensum[semestre - 1]) == 0:
        mensaje = 'El semestre no tiene materias'
    
    else:
        if materia not in pensum[semestre -1]:
            mensaje = 'La materia no existe'
    
        else:
            pensum[semestre -1][materia]['nombre'] = nombre
            pensum[semestre -1][materia]['créditos'] = creditos
            mensaje = 'Modificada con éxito'
            
    return mensaje
