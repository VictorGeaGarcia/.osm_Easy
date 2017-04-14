import pandas as pd

highways = pd.read_csv('waysDF_highway.csv', index_col = 'Unnamed: 0')
highways = highways.drop('color_size',axis=1)
#Vamos a quedarnos solo con las columnas que verdaderamente nos interesan
highways = highways[['Nod_ref', 'Way_Id','highway',
       'junction', 'lanes', 'name','color', 'size1',
       'size2']]

#Limpiamos la columna con los nodos, y la convertimos en una lista

def limpiar_nodref(row):
    linea_limpia = []
    linea = row.Nod_ref.strip('[]').split(',')
    for i,x in enumerate(linea):
        linea_limpia.append(int(x.strip().strip("'")))
    return linea_limpia
highways['Nod_ref'] = highways.apply(limpiar_nodref,axis=1)
##print(highways.columns)
print(highways)
##print(highways['junction'].dropna().index.size)

# Ahora cargamos el archivo con los nodos. Para cada fila en highways, de su Nod_ref cogemos cada uno de los
# nodos y obtenemos su lon,lat que cargamos en dos listas en columnas Lon,Lat (que tenemos que crear)

nodes = pd.read_csv('/home/vilgegar/Documents/Proyecto SETIC/Sistema Integral/OpenStreetMap/nodeS.csv',
                    index_col='Unnamed: 0')

print(nodes)
print(nodes['Nod_Lon'].dtype)



def lon(row):
    lon_list = []
    linea = row.Nod_ref
    
    for i,x in enumerate(row.Nod_ref):
        long = nodes[nodes.Nod_Id==x].Nod_Lon.values[0]
        lon_list.append(long)
    return lon_list
def lat(row):
    lat_list = []
    linea = row.Nod_ref
    
    for i,x in enumerate(row.Nod_ref):
        latt = nodes[nodes.Nod_Id==x].Nod_Lat.values[0]
        lat_list.append(latt)
    return lat_list
              
highways['Lon'] = highways.apply(lon,axis=1) 
highways['Lat'] = highways.apply(lat,axis=1)

highways.to_csv('highways.csv')
print(highways)
