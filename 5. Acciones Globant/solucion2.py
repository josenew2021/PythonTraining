def solucion():
    
    archivo = open('GLOBANT.csv')
    x = csv.reader(archivo)

    Date = []
    Open = []
    High = []
    Low = []
    Close = []
    adj_close = []
    Volume = []
    
    next(x, None)
    for columna in x:
        Date.append(columna[0])
        Open.append(float(columna[1]))
        High.append(float(columna[2]))
        Low.append(float(columna[3]))
        Close.append(float(columna[4]))
        adj_close.append(float(columna[5]))
        Volume.append(float(columna[6]))
    
    archivo.close()
    comportamiento = []
    media = []
    k = 0
    j = 0
    m = 0
    
    for i in range (len(Open)):
        resta = Close[i] - Open[i]
        media.append(0.5*(High[i])-(Low[i]))
        
        if resta > 0:
            comportamiento.append('SUBE')
            k += 1
            
        elif resta < 0: 
            comportamiento.append('BAJA')
            j += 1
        
        elif resta == 0:
            comportamiento.append('ESTABLE')
            m += 1
    
    with open('analisis_archivo.csv', 'w') as file:
        file.write('fecha\tComportamiento de la accion\tPunto medio HIGH-LOW\n')
        
        for i in range (len(Date)):
            file.write('%s\t' % Date[i])
            file.write('%s\t' % comportamiento[i])
            file.write('%s\t' % media[i])
        file.close()
    
    data = {}
    lowest = min(Low)
    highest = max(High)
    
    for i in range(len(Date)):
        
        if lowest == Low [i]:
            data['date_lowest_price'] = Date[i]
            data['lowest_price'] = Low[i
            
        elif highest == High[i]:
            data['date_highest_price'] = Date[i]
            data['highest_price'] = High[i]
    
    data['cantidad_veces_sube'] = k
    data['cantidad_veces_baja'] = j
    data['cantidad_veces_estable'] = m
    
    with open('detalles.json', 'w') as file:
        json.dump(data, file)

solucion()
