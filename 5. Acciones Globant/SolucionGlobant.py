import csv
import json

def solucion():
    with open('GLOBANT.csv') as globant_csv:
        globant_data = csv.reader(globant_csv)
        analisis_header = ["fecha", "comportamiento de la accion","Punto medio HIGH-LOW" ]
        analisis_contend = list()
        
        analisis_contend.append(analisis_header)
        next(globant_data) #Me salto el encabezado
        
        for index, row_data in enumerate(globant_data):
            if index == 0:
                detalles_dict = {
                    "date_lowest_price": row_data[0],
                    "lowest_price": float(row_data[3]),
                    "date_highest_price": row_data[0],
                    "highest_price": float(row_data[2]),
                    "cantidad_veces_sube": 0,
                    "cantidad_veces_baja": 0,
                    "cantidad_veces_estable":0
                }
            
            else:
                if detalles_dict['lowest_price'] > float(row_data[3]):
                    detalles_dict['lowest_price'] = float(row_data[3])
                    detalles_dict['date_lowest_price'] = row_data[0]
                
                if detalles_dict['highest_price'] > float(row_data[2]):
                    detalles_dict['highest_price'] = float(row_data[2])
                    detalles_dict['date_highest_price'] = row_data[0]
                    
            row_analisis = [row_data[0]]
            
            if float(row_data[4]) - float(row_data[1]) > 0:
                row_analisis.append('SUBE')
                detalles_dict['cantidad_veces_sube'] += 1
                
            elif float(row_data[4]) - float(row_data[1]) < 0:
                row_analisis.append('BAJA')
                detalles_dict['cantidad_veces_baja'] += 1
                
            else:
                row_analisis.append('ESTABLE')
                detalles_dict['cantidad_veces_estable'] +=1
            
            row_analisis.append((float(row_data[2]) - float(row_data[3])) /2)
            analisis_contend.append(row_analisis)

        with open('analisis_archivo.csv', 'w') as analisis_file:
            analisis_writer = csv.writer(analisis_file, delimiter='\t')
            analisis_writer.writerows(analisis_contend)
            
        with open('detalles.json', 'w') as detalles_json:
            json.dump(detalles_dict, detalles_json)

            
                