import pandas as pd

waysDF = pd.read_csv('ways_final.csv',index_col='Unnamed: 0')

##waysDF.drop(['abandoned','access','addr:city','addr:country','addr:housename',
##             'addr:street','admin_level','aeroway','alt_name','alt_name_1','alt_name_2','alt_name_3',
##             'addr:housenumber','addr:postcode','type','trail_visibility','url','use','unnamed','tracktype',
##             'vehicle','voltage','website','wheelchair',
##             'wifi','wikidata','wikipedia','wikipedia:en'],axis=1,inplace=True)



##  Aqui vamos a dividir el subset en las distintas categorias (al menos las mas importantes) que
##  aparecen en la pagina de wiki.openstree.../Map_Features

##Con esto comparamos el tamano total del dataset(habiendo quitado algunas columnas ya)
##y el tamano de la categoria highway
waysDF_highway = waysDF.dropna(axis =0, subset=['highway'])
print('El DF tiene en total: ',waysDF.index.size,' filas')
print('Categoria Highway tiene: ',waysDF_highway.index.size)

#Categoria amenity
waysDF_amenity = waysDF.dropna(axis =0, subset=['amenity'])
print('Categoria amenity tiene: ',waysDF_amenity.index.size)

#Categoria barrier
waysDF_barrier = waysDF.dropna(axis =0, subset=['barrier'])
print('Categoria Barrier tiene: ',waysDF_barrier.index.size)

#Categoria building
waysDF_building = waysDF.dropna(axis =0, subset=['building'])
print('Categoria building tiene: ',waysDF_building.index.size)

#Categoria landuse
waysDF_landuse = waysDF.dropna(axis =0, subset=['landuse'])
print('Categoria landuse tiene: ',waysDF_landuse.index.size)

#Categoria leisure
waysDF_leisure = waysDF.dropna(axis =0, subset=['leisure'])
print('Categoria leisure tiene: ',waysDF_leisure.index.size)

#Categoria natural
waysDF_natural = waysDF.dropna(axis =0, subset=['natural'])
print('Categoria natural tiene: ',waysDF_natural.index.size)

###Categoria public_transport
##waysDF_public_transport = waysDF.dropna(axis =0, subset=['public_transport'])
##print('Categoria public_transport tiene: ',waysDF_public_transport.index.size)

#Categoria railway
waysDF_railway = waysDF.dropna(axis =0, subset=['railway'])
print('Categoria railway tiene: ',waysDF_railway.index.size)

#Categoria waterway
waysDF_waterway = waysDF.dropna(axis =0, subset=['waterway'])
print('Categoria waterway tiene: ',waysDF_waterway.index.size)

##########################################################################################


##  En primer lugar vamos a tratar la categoria highway, por ser de las mas interesantes y mas numerosa

print(waysDF.highway)

#Vamos a quitar aquellas columnas en que no nos interesen, o que esten llenas de NaN
waysDF_highway = waysDF_highway.dropna(axis=1,how='all')
waysDF_highway = waysDF_highway.drop(['alt_name', 'alt_name_1','alt_name_2', 'alt_name_3','construction',
                     'converted_by', 'covered','created_by', 'crossing', 'cutting','destination',
                     'embankment', 'emergency', 'fixme', 'foot', 'footway', 'ford','horse',
                     'incline', 'int_ref','lit', 'maxheight', 'maxspeed','maxweight', 'motor_vehicle',
                     'motor_vehicle:conditional', 'mtb','mtb:scale','noexit', 'noname', 'old_name',
                     'old_name_1','passing_places', 'place', 'postal_code','ramp','sac_scale', 'segregated',
                     'service', 'short_name', 'short_name_1','short_name_2', 'short_name_3', 'shoulder',
                     'shoulder:width','sloped_curb', 'smoothness', 'source', 'source:date','source:name',
                     'trail_visibility', 'tunnel', 'unnamed', 'vehicle', 'website','wheelchair', 'width',
                     'wikipedia'],axis=1)
print('EL numero de columnas tras el primer drop es:',waysDF_highway.columns.values.size)
print('Ahora estos son los valores que quedan de highway: ', waysDF_highway.highway)


#Vamos a sacar los distintos valores que toma highway:
print('Los distintos valores que toma highway son: ' ,waysDF_highway.highway.drop_duplicates().values)
print('Las columnas que quedan de waysDF_highway son: ',waysDF_highway.columns)
## Ahora vamos a introducir una columna en el DF waysDF_higway con el color que ha de tomar esa linea y el tamano
    #Aqui abajo nos queda analizar las junction
def color_size_func(row):
    value = row.highway
    if (value == 'motorway'):
        color = '#DC143C'
        size1 = 'grande'
        size2 = 2
        return ([color,size1,size2])
    elif (value == 'motorway_link'):
        color = '#DC143C'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'trunk'):
        color = '#FA8072'
        size1 = 'grande'
        size2 = 2
        return ([color,size1,size2])
    elif (value == 'trunk_link'):
        color = '#FA8072'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'primary'):
        color = '#FFA07A'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'primary_link'):
        color = '#FFA07A'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'secondary'):
        color = '#FFFF00'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'secondary_link'):
        color = '#FFFF00'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'tertiary'):
        color = '#FFFFFF'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'tertiary_link'):
        color = '#FFFFFF'
        size1 = 'grande'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'residential' or value == 'unclassified' or value =='service' or
          value == 'road'): #el valor de road lo asigno aqui, pero es muy general (ver web wiki,
                            #es una categoria entera que engloba motorway,primary....
        color = '#FFFFFF'
        size1 = 'medio'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'pedestrian' or value == 'living_street'):
        color = '#A9A9A9'
        size1 = 'peque'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'steps'):
        color = '#FF0000'
        size1 = 'peque'
        size2 = 1
        return ([color,size1,size2])
    elif (value == 'footway' or value == 'path' or value == 'cycleway'):
        color = '#FF6347'
        size1 = 'linea'
        size2 = 1
        return ([color,size1,size2])
    else: #quedan track(agricultura),bridleway(caballos),proposed (planeadas), construction(under construction)
        return (0,0,0)#no hacemos nada,


waysDF_highway['color_size']  = waysDF_highway.apply(color_size_func,axis=1)

print(waysDF_highway)
waysDF_highway [['color','size1','size2']] = waysDF_highway['color_size'].apply(lambda x: pd.Series([x[0],x[1],x[2]]))

print(waysDF_highway)
waysDF_highway.to_csv('waysDF_highway.csv')
