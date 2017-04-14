import pandas as pd


waySDF = pd.read_csv('wayS.csv',index_col='Unnamed: 0')

columnas_set = set()

def obtener_columnas(row):
    linea = row.Tags.strip('{}').split(',')
##    print(linea)
##    print(lon_linea)
    for i,x in enumerate(linea):
##        print(x)
        x = x.split(':')[0].strip().strip("'")
##        print(x)
        columnas_set.add(x)
##        print(list(columnas_set))

def meter_columnas(row):
    linea = row.Tags.strip('{}').split(',')
    for i,x in enumerate (linea):
        x = x.split(': ')
        if(len(x)>=2):
            k = x[0].strip().strip("'")
            v = x[1].strip().strip("'")
            row['{}'.format(k)] = v
    return row

waySDF.apply(obtener_columnas,axis=1)
print(columnas_set)


print(waySDF)
columnas_DF = pd.DataFrame(columns=list(columnas_set))

ways_con_columnas_vacias = pd.concat([waySDF,columnas_DF],axis=1)
print(ways_con_columnas_vacias)

ways_con_columnas_vacias.to_csv('ways_final.csv')

ways_final = ways_con_columnas_vacias.apply(meter_columnas,axis=1)

print(ways_final)
ways_final.to_csv('ways_final.csv')
