import pandas as pd

#Este módulo lee un archivo .osm y genera dos archivos .csv con los Nodes[Id y Coordenadas] y Ways[Id y referencia de nodos](coge solo los de tipo highway)
#El modulo permite tambien obtener los Relations entre los distintos elemnentos, aunque esta parte no esta acabada ni testeada 

def main():
    
    #Cargamos el archivo .osm
    osm_granada = open('map',encoding = 'utf-8')

    #Creamos los distintos dataframes que nos van a hacer falta
    
    nodeDF = pd.DataFrame(columns=['Nod_Id','Nod_Lat','Nod_Lon','Nod_Highway'])
    wayDF  = pd.DataFrame(columns=['Way_Id','Nod_ref','Tags'])

    #Variables de control
    nodtag = way = relation = False
    n_v = 0
    nd_way_list = []
    kv_way_dict = {}

    #Este contador se utilizo para ir desarrollando el modulo   
    #contador = 0

    #Empezamos a iterar el archivo. Primero los nodes,luego ways y por ultimo relations
    for linea in osm_granada:
        #print('contador:' ,contador)
        #contador +=1 
        linea = linea.strip()         #Quitamos los espacios anteriores y posteriores

        if (('<node id=' in linea) & (linea.endswith('/>'))):# & (contador<200)):  #Estamos ante un nodo sin tag
        #Sacaremos solo los valores que nos interesan. ID,LAT,LON Y HIGHWAY
            
            linea_df = linea.partition(' version=')[0]     
            linea_df = linea_df.split(' ')                 
            n_id = linea_df[1].replace('id=','').strip('"')
            n_lat = linea_df[2].replace('lat=','').strip('"')
            n_lon = linea_df[3].replace('lon=','').strip('"')

            joinDF = pd.Series(data=[n_id , n_lat , n_lon , 0],
                                    index=['Nod_Id','Nod_Lat','Nod_Lon','Nod_Highway'])
            nodeDF = nodeDF.append(joinDF,
                                   ignore_index=True)
            continue

        elif (('<node id=' in linea) & (linea.endswith('>'))):# & (contador<200)):   #Estamos ante un nodo con tag

            linea_df = linea.partition(' version=')[0]
            linea_df = linea_df.split(' ')
            n_id = linea_df[1].replace('id=','').strip('"')
            n_lat = linea_df[2].replace('lat=','').strip('"')
            n_lon = linea_df[3].replace('lon=','').strip('"')
            
            nodtag = True                                           #Ahora sabemos que va a entrar en nodtag            
            continue

        elif (nodtag):# & (contador<200)):
            if ('highway' in linea):  #De momento solo cogemos los de tipo highway
                n_v = linea.partition(' v=')[2].strip('"/>')                
                continue
            
            elif ('</node>' in linea):
                joinDF = pd.Series(data=[n_id , n_lat , n_lon , n_v],
                                        index=['Nod_Id','Nod_Lat','Nod_Lon','Nod_Highway'])    #Si va a salir del node ya tenemos toda la info que queremos
                nodeDF = nodeDF.append(joinDF,
                                       ignore_index=True)                                
                nodtag = False
                n_v = 0                         # En caso de que el siguiente no tenga tag highway, para que
                                                # no coja el equivocado
                continue


        elif (('<way id=' in linea)):# & (contador<118000)):           #Estamos ante el inicio de un way
            linea_df = linea.partition(' version=')[0]
            linea_df = linea_df.split(' ')[1]
            w_id = linea_df.replace('id=','').strip('"')
            way = True
            continue
        elif (way & ('<nd ref=' in linea)):#& (contador<118000)):
        
            linea_df = linea.partition(' ref="')[2].strip('"/>')
            nd_way_list.append(linea_df)      #Llenamos una lista con los nodes de ese way
            continue
        elif (way & ('<tag k=' in linea)):#& (contador<118000)):
            linea_df = linea.partition(' k="')[2].strip('"/>')  #Nos queda key y value
            linea_df = linea_df.partition(' v=')
            k_way = linea_df[0].strip('"')
            
            v_way = linea_df[2].strip('"')
            
            kv_way_dict[k_way]=v_way
            continue
        elif (way & ('</way>' in linea)):#& (contador<118000)):         
            joinDF = pd.DataFrame([(w_id,nd_way_list,kv_way_dict)],columns=['Way_Id','Nod_ref','Tags'])
            wayDF = wayDF.append(joinDF,ignore_index=True)
            
            way = False
            nd_way_list = []
            kv_way_dict = {}
            continue
##      A PARTIR DE AQUI TRATA TAMBIEN LOS RELATION, QUE ESOS NO LOS HEMOS USADO
##        elif (('<relation id=' in linea)):
##            linea_df = linea.partition(' version=')[0]
##            r_id = linea_df.split(' ')[1].replace('id=','').strip('"')
##            relation = True
##            print(r_id)
##            
##            continue
##        elif(('<member type="way"' in linea) & relation):
##            linea_df = linea.strip('/>').partition(' role=')
##            r_role = linea_df[2].strip('"')
##            linea_df = linea_df[0].partition(' ref=')
##            r_ref = linea_df[2].strip('"')
##            r_type = linea_df[0].partition(' type=')[2].strip('"')
##            print(r_ref,r_type,r_role)
##            continue
##        
##        elif(('<member type="node"' in linea) & relation):
##            linea_df = linea.strip('/>').partition(' role=')
##            r_role = linea_df[2].strip('"')
##            linea_df = linea_df[0].partition(' ref=')
##            r_ref = linea_df[2].strip('"')
##            r_type = linea_df[0].partition(' type=')[2].strip('"')
##            print(r_ref,r_type,r_role)
##            continue
##        
##        elif(('<member type="relation"' in linea) & relation):
##            linea_df = linea.strip('/>').partition(' role=')
##            r_role = linea_df[2].strip('"')
##            linea_df = linea_df[0].partition(' ref=')
##            r_ref = linea_df[2].strip('"')
##            r_type = linea_df[0].partition(' type=')[2].strip('"')
##            print(r_ref,r_type,r_role)
##            print(nodeDF)
##            
##            continue
##        elif(('<tag k="type"' in linea) & relation):
##            linea_df = linea.partition(' v=')
##            r_k = linea_df[0].partition(' k=')[2].strip('"')
##            r_v = linea_df[2].strip('"/>')
##            print(r_k,r_v)
##            
##        elif(('<tag k="name"' in linea) & relation):
##            linea_df = linea.partition(' v=')
##            r_k = linea_df[0].partition(' k=')[2].strip('"')
##            r_v = linea_df[2].strip('"/>')
##            print(r_k,r_v)
##            break
    return (wayDF,nodeDF)
wayDF, nodeDF = main()
##print(wayDF)
##print(nodeDF)
wayDF.to_csv('wayS.csv')
nodeDF.to_csv('nodeS.csv')

