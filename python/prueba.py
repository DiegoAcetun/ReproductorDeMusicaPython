contenido = ''
contenido+='<ListaReproduccion>'

for i in range(5):
    contenido+='<Lista nombre="milista">'
    contenido+='<cancion nombre="x">'

contenido+='</ListaReproduccion>'

archivo = open('nuevo.xml', 'w')
archivo.write(contenido)
archivo.close