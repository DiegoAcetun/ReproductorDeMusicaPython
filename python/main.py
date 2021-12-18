import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import easygui
import random
import xml.etree.ElementTree as ET
from tkinter import messagebox
from graphviz import Graph
from graphviz import Digraph
import graphviz
import copy
import mutagen
import threading
import time
import datetime
from pygame import mixer
from os import system
import traceback
system('clear')
ruta = ''; cancion = ''; pausa = False; botonReproducir = None; botonPausa = None; imgPausa = None; imgPlay = None
reproducir = True; botonNext = None; txtLabel = 'Cancion: \n Artista: \n Album:' ; text = None; label= None
Aleatorio = None; pila = []; pilaNombre = []; eliminado = None; bandera = False; posicionPila=0
auxEliminado = None; imgCancion = None; labelImgCancion=None; albumActual = None
reproduciendoAlbum = False
from tkinter import *
from ListaDobleAlbum import ListaDobleAlbum
from ListaDobleCancion import ListaDobleCancion
from ListaDobleArtista import ListaDobleArtista
from ListaDoble import ListaDoble
from Cancion import Cancion
from ListaCircular import ListaCircular
listaAlbumes = ListaDobleAlbum()
listaCanciones = ListaDobleCancion()
listaArtistas = ListaDobleArtista()
listaC = ListaDobleCancion()
listaVar = ListaDoble()
listasCirculares = ListaDobleCancion()
listasReproduccion = ListaCircular()
cancionActual = None
listaActual = None
listasReproduccionBox = []
albumesBox = []
id = 0
listasCircularesAlbumes = ListaDoble()
listaAlbum = ListaCircular()
ListaArtistas2=ListaDobleArtista()
ListaAlbumes2=ListaDobleAlbum()

# pp=0
# hilo=True; b=0
# def a():
#     global pausa, reproducir, pp, hilo
#     tiempo = 20
#     while hilo:
#         if pp>=tiempo:
#             hilo=False
#             break
#         if pausa==False:
#             pass
#         else:
#             print(pp)
#             time.sleep(1)       
#             pp+=1
# def h():
#     global pausa, b, hilo
#     if b==0:
#         pass
#     else:
#         hilo=False

#     if pausa:
#         pausa=False

#         return
#     else:
#         pausa=True
#     hilo=True
#     t = threading.Thread(target=a)        
#     t.start()
#     b+=1
    
    
    

def Play():
    global ruta, cancion, pausa, botonPausa, botonReproducir, imgPausa, imgPlay, reproducir, cancionActual
    global combo, listaActual, txtLabel, label, Aleatorio, bandera, posicionPila, imgCancion, labelImgCancion
    #ultimo en agregar primero en salir  
    global pila, combo, pilaNombre, eliminado, reproduciendoAlbum, albumActual
    if reproduciendoAlbum:
        cancionActual = albumActual.primero #Esta es la primera cancion de  la lista
        # print(cancionActual)
        # print(cancionActual.dato.ruta)
        mixer.init()
        
        cancion = cancionActual.dato.ruta
        
        cancion = cancion.replace('"', '')
        
        if reproducir:
            txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
            label.config(text=txtLabel)
            cancionActual.dato.reproducciones+=1
            mixer.music.load(cancion)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            reproducir = False
            botonReproducir.configure(image=imgPausa)
            imgCancion = PhotoImage(file=cancionActual.dato.imagen)
            labelImgCancion.config(image=imgCancion)
            return
        if pausa:
            mixer.music.unpause()
            botonReproducir.configure(image=imgPausa)
            # botonReproducir.image = imgPausa
            pausa = False
        else:
            mixer.music.pause()
            botonReproducir.configure(image=imgPlay)
            # botonReproducir.image = imgPausa
            pausa = True
        return
    
    if Aleatorio.get():
        if combo.get()== '':
            msj = 'No se ha seleccionado ninguna lista de reproducción'
            messagebox.showwarning(message=msj, title="Lista de reproduccion")
            return
    
        if reproducir:
                # posicion 0 es el nombre de la lista,  posicon 1 nombre de la cancion
        # print(pila[0][0], pila[0][1].nombre)
        # print('largo', len(pilaNombre), len(pila))
            for i in range(len(pilaNombre)):
                if combo.get() == pilaNombre[i]:
                    # print(pilaNombre[i])
                    posicionPila = i
                    break
            actual = random.randint(0, len(pila[posicionPila])-1)
            print(len(pila[posicionPila]), 'llll')

            # print(actual, 'actual')
            eliminado = pila[posicionPila][actual]
            pila[posicionPila].pop(actual)
    

            

            # for j in range(len(pila[posicionPila])):
            #     print('cancion', pila[i][j].nombre, 'reproducida', pila[i][j].reproducciones, 'veces')
            #     # print(random.randint(0, len(pila[i])-1))
            mixer.init()
            cancion = eliminado.ruta
            cancion = cancion.replace('"', '')
            txtLabel = f'Cancion: {eliminado.nombre} \n Artista: {eliminado.artista} \n Album: {eliminado.album}'
            label.config(text=txtLabel)
            mixer.music.load(cancion)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            eliminado.reproducciones+=1
            reproducir = False
            botonReproducir.configure(image=imgPausa)
            imgCancion = PhotoImage(file=eliminado.imagen)
            labelImgCancion.config(image=imgCancion)

            return
        if pausa:
            mixer.music.unpause()
            botonReproducir.configure(image=imgPausa)
            # botonReproducir.image = imgPausa
            pausa = False
        else:
            mixer.music.pause()
            botonReproducir.configure(image=imgPlay)
            # botonReproducir.image = imgPausa
            pausa = True
        
    else:
        if combo.get()== '':
            msj = 'No se ha seleccionado ninguna lista de reproducción'
            messagebox.showwarning(message=msj, title="Lista de reproduccion")
            return
        cancionActual = listasCirculares.primero #Aqui estan todas las listas circulares
        listaActual = listasCirculares.primero

        while cancionActual != None:
            # print('sxsx',listaActual.dato.nombre)
            if cancionActual.dato.nombre == combo.get(): #Este es el nombre de la lista seleccionada
                # print(listaActual.dato.nombre, 'es igual a ', combo.get())
                break
            cancionActual = cancionActual.siguiente 
            pass
        
        # print(listasCirculares.size)
        # print(cancionActual.dato)#Esto es una lista circular
        
        cancionActual = cancionActual.dato.primero #Esta es la primera cancion de  la lista
        # print(cancionActual)
        # print(cancionActual.dato.ruta)
        mixer.init()
        cancion = cancionActual.dato.ruta
        
        cancion = cancion.replace('"', '')
        
        if reproducir:
            txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
            label.config(text=txtLabel)
            cancionActual.dato.reproducciones+=1
            mixer.music.load(cancion)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            reproducir = False
            botonReproducir.configure(image=imgPausa)
            imgCancion = PhotoImage(file=cancionActual.dato.imagen)
            labelImgCancion.config(image=imgCancion)
            return
        if pausa:
            mixer.music.unpause()
            botonReproducir.configure(image=imgPausa)
            # botonReproducir.image = imgPausa
            pausa = False
        else:
            mixer.music.pause()
            botonReproducir.configure(image=imgPlay)
            # botonReproducir.image = imgPausa
            pausa = True

def Siguiente():
    global cancion, cancionActual, botonReproducir, imgPlay, imgPausa, pausa
    global pila, combo, pilaNombre, eliminado, Aleatorio, posicionPila, bandera, auxEliminado
    global imgCancion, labelImgCancion, reproduciendoAlbum
    mixer.music.stop()
    if reproduciendoAlbum:
        cancionActual = cancionActual.siguiente
        # print(cancionActual.dato.nombre)

        cancion = cancionActual.dato.ruta
        txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancion = cancion.replace('"', '')
        cancionActual.dato.reproducciones+=1
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        imgCancion = PhotoImage(file=cancionActual.dato.imagen)
        labelImgCancion.config(image=imgCancion)
        pausa = False
        return
    if Aleatorio.get():
        actual = random.randint(0, len(pila[posicionPila])-1)
        # print(actual, 'actual')
        print(len(pila[posicionPila]), 'ssss')

        auxEliminado = eliminado
        eliminado = pila[posicionPila][actual]
        pila[posicionPila].pop(actual)
        bandera = True
        pila[posicionPila].append(auxEliminado)
        # print('aux', auxEliminado.nombre, 'el', eliminado.nombre)


        
        # print(cancionActual.dato.nombre)
        cancion = eliminado.ruta
        txtLabel = f'Cancion: {eliminado.nombre} \n Artista: {eliminado.artista} \n Album: {eliminado.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancion = cancion.replace('"', '')
        eliminado.reproducciones+=1
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        pausa = False
        imgCancion = PhotoImage(file=eliminado.imagen.replace('"',''))
        labelImgCancion.config(image=imgCancion)

        
    else:
        cancionActual = cancionActual.siguiente
        # print(cancionActual.dato.nombre)
        cancion = cancionActual.dato.ruta
        txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancion = cancion.replace('"', '')
        cancionActual.dato.reproducciones+=1
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        imgCancion = PhotoImage(file=cancionActual.dato.imagen)
        labelImgCancion.config(image=imgCancion)
        pausa = False
def Anterior():
    global cancion, cancionActual, botonReproducir, imgPlay, imgPausa, pausa, imgCancion, labelImgCancion    
    global pila, combo, pilaNombre, eliminado, Aleatorio, posicionPila, bandera, auxEliminado, reproduciendoAlbum
    mixer.music.stop()
    if reproduciendoAlbum:
        cancionActual = cancionActual.anterior
        txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancionActual.dato.reproducciones+=1
        mixer.music.stop()
        cancion = cancionActual.dato.ruta
        cancion = cancion.replace('"', '')
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        imgCancion = PhotoImage(file=cancionActual.dato.imagen)
        labelImgCancion.config(image=imgCancion)
        pausa = False
        return
    if Aleatorio.get():


        
        # print(cancionActual.dato.nombre)
        cancion = auxEliminado.ruta
        txtLabel = f'Cancion: {auxEliminado.nombre} \n Artista: {auxEliminado.artista} \n Album: {auxEliminado.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancion = cancion.replace('"', '')
        auxEliminado.reproducciones+=1
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        pausa = False
        imgCancion = PhotoImage(file=auxEliminado.imagen)
        labelImgCancion.config(image=imgCancion)

        auxEliminado = eliminado
        eliminado = pila[posicionPila].pop()
        pila[posicionPila].append(auxEliminado)
        
        bandera = True
        
        # print('aux', auxEliminado.nombre, 'el', eliminado.nombre)

    else:
        cancionActual = cancionActual.anterior
        txtLabel = f'Cancion: {cancionActual.dato.nombre} \n Artista: {cancionActual.dato.artista} \n Album: {cancionActual.dato.album}'
        label.config(text=txtLabel)
        botonReproducir.configure(image=imgPausa)
        cancionActual.dato.reproducciones+=1
        mixer.music.stop()
        cancion = cancionActual.dato.ruta
        cancion = cancion.replace('"', '')
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        imgCancion = PhotoImage(file=cancionActual.dato.imagen)
        labelImgCancion.config(image=imgCancion)
        pausa = False
    

def Cargar():
    global ruta, cancion, pausa, botonReproducir, botonPausa, imgPausa, listasCirculares
    try:

        ruta = easygui.fileopenbox()  
        print(ruta)
        LeerXml()
        Albumes()
        messagebox.showinfo(message='Archivo Cargado', title='Cargar Archivo')
        
    except:
        messagebox.showerror(message='Ocurrió un error al abrir el archivo', title='Cargar Archivo')
        traceback.print_exc()
        
    
    # print(ruta)
    
    # cancion = '../Musica/Alone.mp3'
def Pausa(): 
    global pausa, botonPausa, botonReproducir, imgPausa
    mixer.music.pause()
    pausa = True
    
def Stop():
    global pausa, botonPausa, botonReproducir, imgPausa, reproducir, reproduciendoAlbum, pila, eliminado
    mixer.music.stop()
    if Aleatorio.get() and reproducir==False:
        pila[posicionPila].append(eliminado)
    pausa = False
    reproducir = True
    botonReproducir.configure(image=imgPlay)
    reproduciendoAlbum = False

    
    Aleatorio.set(False)
def recorrerListas():
    global var, listaC, listasReproduccion, listasCirculares
    aux = listasCirculares.primero
    aux2 = aux.dato.primero
    
    while aux != None:
        while aux2:
            

            print(aux2.dato.nombre) #Estas son las canciones agregadas a la lista de reproduccion
            # print(aux.dato.size)
            if aux2 == aux.dato.ultimo:
                break
            aux2 = aux2.siguiente
        # print(aux2.dato)

        aux = aux.siguiente
'''aqui se crea la lista de reprodcucición, se obtienen las canciones seleccionadas'''
def obtenerOpcion():
    global var, listaC, listasReproduccion, listasCirculares,c, listasReproduccionBox, text
    global pila, pilaNombre
    contador = 0
    aux = listaC.primero
    aux2 = listaVar.primero
    aux3 = listaCanciones.primero
    # print('*'*25)
    listasReproduccion = ListaCircular()
    pilaAux = []

    while aux != None:
        #cget devuelve el nombre de la cancion, dato.get es la lista de varString
        #Devuelve True o False si esta seleccionada

        # print(aux.dato.cget('text'), aux2.dato.get(), aux3.dato)
        if aux2.dato.get():
            
            objetoCancion = Cancion()
            objetoCancion.nombre = aux3.dato.nombre
            objetoCancion.ruta = aux3.dato.ruta
            objetoCancion.imagen = aux3.dato.imagen
            objetoCancion.artista = aux3.dato.artista
            objetoCancion.album = aux3.dato.album




            
            listasReproduccion.agregarFinal(objetoCancion) #aux3.dato es un objeto cancion

            pilaAux.append(objetoCancion)
            contador+=1
        

            
        aux = aux.siguiente
        aux2 = aux2.siguiente
        aux3 = aux3.siguiente
    
    if listasCirculares.vacia():
        pass
    else:
        aux = listasCirculares.primero
        # print(aux.dato.nombre)
        while aux!= None:
            if text.get(1.0, 'end-1c') == aux.dato.nombre:
                msj = 'Ya existe una lista con este nombre, ingresar un nombre distinto'
                messagebox.showwarning(message=msj, title='Lista de reproduccion')
                return
            aux = aux.siguiente
    if text.get(1.0, 'end-1c') != '':
        if contador == 0:
            msj = 'No se ha seleccionado ninguna cancion '
            messagebox.showerror(message=msj, title="Lista de reproduccion")
        else:
            msj = 'Lista de reproduccion '+ text.get(1.0, 'end-1c')+ ' ha sido creada'
            messagebox.showinfo(message=msj, title="Nueva Lista")
            listasReproduccion.nombre = text.get(1.0, 'end-1c')
            listasCirculares.agregarFinal(listasReproduccion)
            listasReproduccionBox.append(listasReproduccion.nombre)
            pila.append(pilaAux[:])
            pilaNombre.append(text.get(1.0, 'end-1c'))


            

            combo.configure(values=(listasReproduccionBox))

    else:
        msj = 'Ingrese un nombre para la lista '
        messagebox.showerror(message=msj, title="Nueva Lista")

    text.delete(1.0, 'end-1c')


    
    '''quitamos la seleccion de los checkbox cada vez que creamos una lista de reproduccion'''
    
    aux2 = listaVar.primero #Essta es la variable booleana de los botones
    while aux2 != None:
        # print(aux.dato)#Esto es un objeto checkbutton
        aux2.dato.set(False)
        
        aux2 = aux2.siguiente

    # recorrerListas()

def Pila():
    #ultimo en agregar primero en salir  
    global pila, combo, pilaNombre
    aux = 0
    # posicion 0 es el nombre de la lista,  posicon 1 nombre de la cancion
    # print(pila[0][0], pila[0][1].nombre)
    # print('largo', len(pilaNombre), len(pila))
    for i in range(len(pilaNombre)):
        if combo.get() == pilaNombre[i]:
            print(pilaNombre[i])
            aux = i
            break
    actual = random.randint(0, len(pila[i])-1)
    
    eliminado = pila[i][actual]
    pila[i].pop(actual)

    for j in range(len(pila[i])):
        print('cancion', pila[i][j].nombre, 'reproducida', pila[i][j].reproducciones, 'veces')
        # print(random.randint(0, len(pila[i])-1))
    
    
    pass

def LeerXml():
    global ruta, listaAlbumes, listaCanciones, listaArtistas, ventana, var, listaC, listaVar
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for i in range(len(root)): #root.tag es biblioteca
            nombreCancion = (root[i].attrib) #Por cada iteracion guadar el nombre de cada cancion en un dicc
                                            #el tag es cancion
            nombreCancion = nombreCancion["nombre"] #Esto devuelve solo el nombre de la cancion sin la etiqueta
            nuevaCancion = Cancion()
            
            nuevaCancion.nombre = nombreCancion
            #nombre
            #Posicion 0 de la lista es la etiqueta cancion
            # print(root[0][0].text)
            # print(nombreCancion)
            #Recorriendo etiqueta cancion
            for j in range(len(root[0])):
                if root[i][j].tag== 'album':
                    # print(root[i][j].text)
                    if root[i][j].text.strip(' ')== '':
                        nuevaCancion.album = 'single'
                    else:
                        nuevaCancion.album = root[i][j].text.strip(' ').replace('"', '')
                elif root[i][j].tag == 'ruta':
                    nuevaCancion.ruta = root[i][j].text.strip(' ').replace('"', '')
                elif root[i][j].tag == 'imagen':
                    nuevaCancion.imagen = root[i][j].text.strip(' ').replace('"', '')
                elif root[i][j].tag == 'artista':
                    nuevaCancion.artista = root[i][j].text.strip(' ').replace('"', '')
            
            listaCanciones.agregarFinal(nuevaCancion)
    except:
        messagebox.showerror(message='Error al leer xml', title='Lectura xml')
    # AnidarListas()
    conectarListas()
    CrearCheckbox()
    # aux = listaCanciones.primero #Esta es la primera lista aux cancion
    # #Recorriendo la lista de canciones
    # while aux != None:
    #     if listaAlbumes.vacia():
    #         listaAlbumAux = ListaDobleAlbum()
    #         listaAlbumAux.agregarFinal(aux.dato)
    #         listaAlbumAux.artista = aux.dato.artista
    #         listaAlbumAux.album = aux.dato.album
    #         # print(aux.dato.album, aux.dato.artista)
            
    #         listaAlbumes.agregarFinal(listaAlbumAux)

    #         # print(aux.dato.nombre)
    #         #seguir creando las listas album cuando ya hay elementos,
    #         #recorrer la lista 
    #         aux2 = listaAlbumes.primero

    #     else:
    #         albumEncontrado = False
    #         # print(aux.dato.album, aux.dato.artista)
    #         aux3 = listaAlbumes.primero
    #         while aux3 != None:
    #             # print(aux3.dato)
    #             aux4=aux3.dato #aux4 tiene la lista album aux
    #             # print(aux4.primero.dato.nombre) # Esto es el objeto cancion
    #             # print(aux4.album)
    #             aux3 = aux3.siguiente
    #             if aux4.album == aux.dato.album: #Recorremos para ver si el album ya existe
    #                 aux4.agregarFinal(aux.dato) #Le agregamos la cancion a ese album
    #                 albumEncontrado = True
    #                 break
            
    #         if albumEncontrado:
    #             pass
    #         else:
    #             listaAlbumAux = ListaDobleAlbum()
    #             listaAlbumAux.agregarFinal(aux.dato)
    #             listaAlbumAux.artista = aux.dato.artista
    #             listaAlbumAux.album = aux.dato.album
    #             # print(listaAlbumAux.primero.dato.nombre) Con esto se accede a los atributos de la lista
    #             #de canciones desde la lista aux album
    #             listaAlbumes.agregarFinal(listaAlbumAux)

    #             # print(aux.dato.nombre)



    #     #print(aux.dato.ruta)#asi se accede a los atrubutos desde el auxiliar
    #     aux=aux.siguiente

    # #Recorriendo listas albumes
    # aux = listaAlbumes.primero


    # #Aqui solo se obtienen datos, no se crea nada
    # while aux!=None:
    #     aux2 = aux.dato #Esto es la lista album auxiliar
    #     aux3 = aux.dato.primero
    #     # print('*'*25)
    #     # print('Canciones del album', aux.dato.album, 'artista', aux.dato.artista) #Aqui se imprime la info
    #     #Descomentar para ver
    #     while aux3 !=None:
    #         # print(aux3.dato.nombre) descomentar para obtener atrib de la cancion
    #         aux3=aux3.siguiente

    #     # print(aux2.primero.dato.nombre) #Imprimo nombre de la cancion
    #     aux = aux.siguiente


    # #Aqui se anidan listasArtista y listaALbum
    # aux = listaAlbumes.primero
    # # print(aux.dato) #esto es un album auxiliar
    # artistaEncontrado = False
    # while aux != None: #Aqui recorro los 5 albumes
    #     aux2 = aux.dato #Aqui estan los atributos de cada album
    #     aux2 = aux2.artista
    #     # print(aux.dato.size)
    #     if listaArtistas.vacia():
    #         listaAuxArtistas = ListaDobleArtista()
    #         listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
    #         listaAuxArtistas.artista = aux2
    #         listaArtistas.agregarFinal(listaAuxArtistas)
    #         aux3 = listaArtistas.primero

    #     else:
    #         #aqui recorro las listas artistas
    #         aux3 = listaArtistas.primero
    #         while aux3 != None:
    #             # print(aux2+aux3.dato.artista+'valores') #esta es una lista artista con atributos
    #             #Verificamos si ya existe el artista y solo le agregamos el album
    #             #aux 3 es lista artista
    #             # print(aux2 == aux3.dato.artista, 'comparacion')
    #             if aux2 == aux3.dato.artista:
        
    #                 aux3.dato.agregarFinal(aux.dato)

    #                 artistaEncontrado = True
                    

    #                 # print('iguales', aux2)
    #                 break
    #             aux3 = aux3.siguiente
                    
                
    #         #Si el artista no existe creamos una nueva instancia
    #         if artistaEncontrado == False:
    #             # print('no existe')
    #             listaAuxArtistas = ListaDobleArtista()
    #             listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
    #             listaAuxArtistas.artista = aux2
    #             listaArtistas.agregarFinal(listaAuxArtistas)
    #         artistaEncontrado = False
                    
    #     # print('sxsx')
                


            
        

    #     aux = aux.siguiente

    # #Verificando los datos en la lista artista
    # aux = listaArtistas.primero
    # # print(listaArtistas.size)
    # while aux != None:
    #     # print('*'*25)
    #     # print('artista', aux.dato.artista, )
    #     # print(aux.dato.primero.dato)
    #     aux2 = aux.dato.primero 
    #     # aux4 = aux.dato.primero
    #     # print('albumes', end='   ')
    #     #Recorriendo albumes de los artistas para obtener solo los albumes
    #     # while aux4 != None:
            
    #     #     print(aux4.dato.album, end='   ')
    #     #     aux4 = aux4.siguiente


    #     #Recorremos los albumes del artista para obtener las canciones
        
    #     while aux2 != None:
            
    #         # print('album', aux2.dato.album)
    #         aux3 = aux2.dato.primero
    #         #Recorriendo el album para pbtener las canciones
    #         # print('CANCIONES')
    #         while aux3 != None:
    #             # print(aux3.dato.nombre)
    #             aux3 = aux3.siguiente

    #         aux2 = aux2.siguiente
    #         # print(aux2)
        


        
    #     aux = aux.siguiente

    # aux = listaCanciones.primero
    # posy = 0
    # #Creamos los checkbox de las canciones
    # while aux != None:
    #     var = tk.BooleanVar()
    #     # var = aux.dato.nombre
    #     opcionCancion = tk.Checkbutton(ventana, text=aux.dato.nombre, variable=var)
    #     opcionCancion.pack
    #     opcionCancion.place(x=20, y=160+posy)
    #     listaAux = ListaDoble()
    #     listaAux.agregarFinal(opcionCancion)
    #     listaVar.agregarFinal(var)

    #     listaC.agregarFinal(opcionCancion)
    #     # print(var.get())
        
    #     posy+=20
    #     aux = aux.siguiente
def CrearCheckbox():
    global ruta, listaAlbumes, listaCanciones, listaArtistas, ventana, var, listaC, listaVar
    aux = listaCanciones.primero
    posy = 0
    #Creamos los checkbox de las canciones
    while aux != None:
        var = tk.BooleanVar()
        # var = aux.dato.nombre
        opcionCancion = tk.Checkbutton(ventana, text=aux.dato.nombre, variable=var)
        opcionCancion.pack
        opcionCancion.place(x=20, y=160+posy)
        listaAux = ListaDoble()
        listaAux.agregarFinal(opcionCancion)
        listaVar.agregarFinal(var)

        listaC.agregarFinal(opcionCancion)
        # print(var.get())
        
        posy+=20
        aux = aux.siguiente

def AnidarListas():
    global ruta, listaAlbumes, listaCanciones, listaArtistas, ventana, var, listaC, listaVar

    aux = listaCanciones.primero #Esta es la primera lista aux cancion
    #Recorriendo la lista de canciones
    while aux != None:
        if listaAlbumes.vacia():
            # if aux.dato.album == 'single':
            #     aux=aux.siguiente

            #     print('a')
            #     continue
            listaAlbumAux = ListaDobleAlbum()
            listaAlbumAux.agregarFinal(aux.dato)
            listaAlbumAux.artista = aux.dato.artista
            listaAlbumAux.album = aux.dato.album
            # print(aux.dato.album, aux.dato.artista)
            
            listaAlbumes.agregarFinal(listaAlbumAux)

            # print(aux.dato.nombre)
            #seguir creando las listas album cuando ya hay elementos,
            #recorrer la lista 
            aux2 = listaAlbumes.primero

        else:
            # if aux.dato.album == 'single':
            #     aux=aux.siguiente

            #     print('iii')
            #     continue
            albumEncontrado = False
            # print(aux.dato.album, aux.dato.artista)
            aux3 = listaAlbumes.primero
            while aux3 != None:
                # print(aux3.dato)
                aux4=aux3.dato #aux4 tiene la lista album aux
                # print(aux4.primero.dato.nombre) # Esto es el objeto cancion
                # print(aux4.album)
                aux3 = aux3.siguiente
                # print('a'+aux4.album+'a'+' a'+aux.dato.album+'a')
                if aux4.album == aux.dato.album: #Recorremos para ver si el album ya existe
                    aux4.agregarFinal(aux.dato) #Le agregamos la cancion a ese album
                    albumEncontrado = True
                    
                    # print(aux4.album, 'no se crea')

                    break
            
            if albumEncontrado:
                pass
            else:
                listaAlbumAux = ListaDobleAlbum()
                listaAlbumAux.agregarFinal(aux.dato)
                listaAlbumAux.artista = aux.dato.artista
                listaAlbumAux.album = aux.dato.album
                # print(listaAlbumAux.primero.dato.nombre) Con esto se accede a los atributos de la lista
                #de canciones desde la lista aux album
                listaAlbumes.agregarFinal(listaAlbumAux)

                # print(aux.dato.nombre)



        #print(aux.dato.ruta)#asi se accede a los atrubutos desde el auxiliar
        aux=aux.siguiente

    #Recorriendo listas albumes
    aux = listaAlbumes.primero


    #Aqui solo se obtienen datos, no se crea nada
    while aux!=None:
        aux2 = aux.dato #Esto es la lista album auxiliar
        aux3 = aux.dato.primero
        # print('*'*25)
        # print('Canciones del album', aux.dato.album, 'artista', aux.dato.artista) #Aqui se imprime la info
        #Descomentar para ver
        while aux3 !=None:
            # print(aux3.dato.nombre) descomentar para obtener atrib de la cancion
            aux3=aux3.siguiente

        # print(aux2.primero.dato.nombre) #Imprimo nombre de la cancion
        aux = aux.siguiente


    #Aqui se anidan listasArtista y listaALbum
    aux = listaAlbumes.primero
    # print(aux.dato) #esto es un album auxiliar
    artistaEncontrado = False
    while aux != None: #Aqui recorro los 5 albumes
        aux2 = aux.dato #Aqui estan los atributos de cada album
        aux2 = aux2.artista
        # print(aux.dato.size)
        
        if listaArtistas.vacia():
            listaAuxArtistas = ListaDobleArtista()
            listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
            listaAuxArtistas.artista = aux2
            listaArtistas.agregarFinal(listaAuxArtistas)
            aux3 = listaArtistas.primero

        else:
            #aqui recorro las listas artistas
            aux3 = listaArtistas.primero
            album=False
            while aux3 != None:
                # print(aux2+aux3.dato.artista+'valores') #esta es una lista artista con atributos
                #Verificamos si ya existe el artista y solo le agregamos el album
                #aux 3 es lista artista
                # print(aux2 == aux3.dato.artista, 'comparacion')
                if aux2 == aux3.dato.artista:                   
                    aux3.dato.agregarFinal(aux.dato)
                    artistaEncontrado = True
                    

                    # print('iguales', aux2)
                    break
                aux3 = aux3.siguiente
                    
                
            #Si el artista no existe creamos una nueva instancia
            if artistaEncontrado == False:
                # print('no existe')
                listaAuxArtistas = ListaDobleArtista()
                listaAuxArtistas.agregarFinal(aux.dato) #aux dato contiene el album a agregar
                listaAuxArtistas.artista = aux2
                listaArtistas.agregarFinal(listaAuxArtistas)
            artistaEncontrado = False
                    
        # print('sxsx')
                


            
        

        aux = aux.siguiente

    #Verificando los datos en la lista artista
    aux = listaArtistas.primero
    # print(listaArtistas.size)
    while aux != None:
        # print('*'*25)
        # print('artista', aux.dato.artista, )
        # print(aux.dato.primero.dato)
        aux2 = aux.dato.primero 
        # aux4 = aux.dato.primero
        # print('albumes', end='   ')
        #Recorriendo albumes de los artistas para obtener solo los albumes
        # while aux4 != None:
            
        #     print(aux4.dato.album, end='   ')
        #     aux4 = aux4.siguiente


        #Recorremos los albumes del artista para obtener las canciones
        
        while aux2 != None:
            
            # print('album', aux2.dato.album)
            aux3 = aux2.dato.primero
            #Recorriendo el album para pbtener las canciones
            # print('CANCIONES')
            while aux3 != None:
                # print(aux3.dato.nombre)
                aux3 = aux3.siguiente

            aux2 = aux2.siguiente
            # print(aux2)
        


        
        aux = aux.siguiente
    print(listaArtistas.primero.dato.size)
    # print('size', listaAlbumes.size)

    #Nuevo codigo
    
# def Graphviz():
#     global id, listaArtistas, listaAlbumes, listaCanciones
#     # g = Digraph('ejemplo', format='png')
#     # g.node(str(id), 'King Arthur')
#     # id+=1
#     # g.node(str(id), 'Sir Bedevere the Wise')
#     # id+=1
#     # g.node(str(id), 'Sir Lancelot the Brave')

#     # g.edges(['01', '02', '10'])
#     # g.edge('1', '2', constraint='false')
#     # g = Digraph('archivo', format='png')
#     contador = 0
#     aux = listaArtistas.primero
#     print(listaArtistas.size)

#     g = Digraph('ejemplo', format='png')
#     g.node(str(id), aux.dato.artista)
    

#     # g.node('0', 'a')
#     # g.node('1', 'b')

#     # g.edge('0', '1', constraint='false')
#     id0=str(id)
#     idArtista=str(id)
    
#     id+=1
#     idPrimero=0
#     idSegundo=0
#     bandera=False
#     bandera2=False
#     while aux != None:
#         # if id>1:
            
#         # print('*'*25)
#         # # print('artista', aux.dato.artista, )
#         # # print(aux.dato.primero.dato)
#         aux2 = aux.dato.primero 
#         # # aux4 = aux.dato.primero
#         # # print('albumes', end='   ')
#         # #Recorriendo albumes de los artistas para obtener solo los albumes
#         # # while aux4 != None:
            
#         # #     print(aux4.dato.album, end='   ')
#         # #     aux4 = aux4.siguiente


#         #Recorremos los albumes del artista para obtener las canciones
#         contador = 0
#         while aux2 != None:
#             if contador==0:
#                 if bandera:
#                     # print('entra')
#                     g.node(str(id), aux2.dato.album)
#                     id1=str(id)
#                     g.edge(idArtista, str(id), dir='both')
#                     g.edge(id2, str(id), constraint='false', dir='both')
#                     idAlbum=str(id)
#                     id2=str(id)
#                     id+=1
#                     contador+=1
#                     pass
#                 else:
#                     g.node(str(id), aux2.dato.album)
#                     id1=str(id)
#                     g.edge(idArtista, str(id), dir='both')
#                     idAlbum=str(id)
#                     id2=str(id)
#                     id+=1
                    
#                     contador+=1
#         #     # print('album', aux2.dato.album)
#             aux3 = aux2.dato.primero
#             #Recorriendo el album para pbtener las canciones
#             # print('CANCIONES')
#             contador2=0
            
#             while aux3 != None:
#                 # print(aux3.dato.nombre)
#                 if contador2 == 0:
                    
                    
#                         g.node(str(id), aux3.dato.nombre)
#                         g.edge(idAlbum, str(id), dir='both')
                        
#                         # g.edge(id3, str(id), constraint='false')
#                         # id2=str(id)
#                         if bandera2:
#                             # g.edge('10', '14', dir='both', constraint='false')
#                             print('desde b', id3, str(id))
#                             pass
#                         id3=str(id)
                        
#                         id+=1
#                         contador2+=1
                        

#                 aux3 = aux3.siguiente
#                 bandera2=True
                
#                 if aux3!= None:
#                     # print('entra dddd')
#                     g.node(str(id), aux3.dato.nombre, dir='both', constraint='false')
#                     g.edge(idAlbum, str(id), dir='both')
#                     g.edge(id3, str(id), constraint='false', dir='both')
#                     id3=str(id)
#                     print('desde none', id3)
#                     id+=1
        

                
#             aux2 = aux2.siguiente
#             bandera=True

#             if aux2 != None:
#                 # print('aa', aux2.dato.album)
#                 g.node(str(id), aux2.dato.album)
#                 id1=str(id)
#                 g.edge(idArtista, str(id))
#                 g.edge(id2, str(id), constraint='false', dir='both')
#                 id2=str(id)
#                 idAlbum=str(id)
#                 id+=1


#         #     # print(aux2)
        


#         # # break
#         aux = aux.siguiente
#         if aux !=None:
#             g.node(str(id), aux.dato.artista)
#             id1=str(id)
#             g.edge(id0, id1, constraint='false', dir='both')
#             id0=id1
#             idArtista = str(id)

#             id+=1
#         # print(id)
#         # break
        
        
        




#     g.view()   

#     pass

def Grafo():
    global listaArtistas, listaAlbumes, listaCanciones, id
    listaIdArtista=ListaDoble()
    listaIdAlbumes=ListaDoble()
    id=0
    aux = listaArtistas.primero
    # print('lisA', listaArtistas.size)
    try:

        g = Digraph('Grafo', format='png')
        g.node(str(id), aux.dato.artista)
        idPrimerArtista=id
        idArtistaIzquierda=id
        listaIdArtista.agregarFinal(id)
        id+=1
        #conectamos los artistas
        while aux != None:
            aux = aux.siguiente
            if aux!=None:
                g.node(str(id), aux.dato.artista)
                g.edge(str(idArtistaIzquierda), str(id), constraint='false', dir='both')
                idArtistaIzquierda=id
                listaIdArtista.agregarFinal(id)

                id+=1
            # print(id)


        #Conectamos albumes
        idAlbumIzquierda=id
        aux = listaArtistas.primero
        c=0
        auxIdArtista=listaIdArtista.primero; bandera=False
        while aux!=None:
            #Recorro los albumes de los artistas
            aux2=aux.dato.primero
            bandera=False
            while aux2!= None:
                # print(auxIdArtista.dato)
                # print(aux2.dato.album)
                g.node(str(id), aux2.dato.album)
                g.edge(str(auxIdArtista.dato), str(id), dir='both')
                aux2=aux2.siguiente
                if bandera:
                    g.edge(str(idAlbumIzquierda), str(id), constraint='false', dir='both')
                idAlbumIzquierda=id
                listaIdAlbumes.agregarFinal(id)
                id+=1
                    
                bandera=True
            aux=aux.siguiente
            auxIdArtista=auxIdArtista.siguiente
            
        aux = listaAlbumes.primero
        auxIdAlbumes=listaIdAlbumes.primero
        idCancionIzquierda=id
        bandera = False
        # print(listaAlbumes.size, 'size es estre')
        while aux!= None:
            aux2= aux.dato.primero
            # print('*'*25)
            # print('album', aux.dato.album)
            bandera=False
            while aux2 !=None:
                g.node(str(id), aux2.dato.nombre)
                g.edge(str(auxIdAlbumes.dato), str(id), dir='both')
                # print(aux2.dato.nombre)
                if bandera:
                    # print(idCancionIzquierda, id)
                    g.edge(str(idCancionIzquierda), str(id), constraint='false', dir='both')
                    pass
                idCancionIzquierda=id
                id+=1
                bandera=True
                aux2=aux2.siguiente
            aux=aux.siguiente
            
            auxIdAlbumes=auxIdAlbumes.siguiente
                
            pass
        g.view()
        id=0
        g2 = Digraph('Grafo2', format='png')
        aux = listasCirculares.primero
        # print(aux.dato)
        aux = aux.dato.primero
        g2.node(str(id), aux.dato.nombre)
        id1=id
        idPrimero=id
        id+=1
        while aux:
            # print(aux.dato.nombre)
            aux=aux.siguiente
            
            if aux==listasCirculares.primero.dato.primero:
                break
            g2.node(str(id),aux.dato.nombre)
            g2.edge(str(id1), str(id), constraint='false', dir='both')
            id1=id
            id+=1
        g2.edge(str(idPrimero), str(id1), constraint='false', dir='both')
        g2.view()

        id=0
        g3 = Digraph('Grafo3', format='png')
        aux = listaAlbumes.primero
        print(aux.dato,'ooo')
        aux = aux.dato.primero
        g3.node(str(id), aux.dato.nombre)
        id1=id
        idPrimero=id
        id+=1
        while aux:
            print(aux.dato.nombre)
            aux=aux.siguiente
            
            if aux!=None:
                g3.node(str(id),aux.dato.nombre)
                g3.edge(str(id1), str(id), constraint='false', dir='both')
                id1=id
                id+=1
        g3.edge(str(idPrimero), str(id1), constraint='false', dir='both')
        g3.view()

        

    except:
        messagebox.showerror(message='Error al generar el grafo', title='Grafo')
    pass
def conectarListas():
    global ListaAlbumes2, listaCanciones, ListaArtistas2, listaAlbumes
    aux = listaCanciones.primero #Esta es la primera lista aux cancion
    #Recorriendo la lista de canciones
    while aux != None:
        if listaAlbumes.vacia():
            # if aux.dato.album == 'single':
            #     aux=aux.siguiente

            #     print('a')
            #     continue
            listaAlbumAux = ListaDobleAlbum()
            listaAlbumAux.agregarFinal(aux.dato)
            listaAlbumAux.artista = aux.dato.artista
            listaAlbumAux.album = aux.dato.album
            # print(aux.dato.album, aux.dato.artista)
            
            listaAlbumes.agregarFinal(listaAlbumAux)

            # print(aux.dato.nombre)
            #seguir creando las listas album cuando ya hay elementos,
            #recorrer la lista 
            aux2 = listaAlbumes.primero

        else:
            # if aux.dato.album == 'single':
            #     aux=aux.siguiente

            #     print('iii')
            #     continue
            albumEncontrado = False
            # print(aux.dato.album, aux.dato.artista)
            aux3 = listaAlbumes.primero
            while aux3 != None:
                # print(aux3.dato)
                aux4=aux3.dato #aux4 tiene la lista album aux
                # print(aux4.primero.dato.nombre) # Esto es el objeto cancion
                # print(aux4.album)
                aux3 = aux3.siguiente
                # print('a'+aux4.album+'a'+' a'+aux.dato.album+'a')
                if aux4.album == aux.dato.album: #Recorremos para ver si el album ya existe
                    aux4.agregarFinal(aux.dato) #Le agregamos la cancion a ese album
                    albumEncontrado = True
                    
                    # print(aux4.album, 'no se crea')

                    break
            
            if albumEncontrado:
                pass
            else:
                listaAlbumAux = ListaDobleAlbum()
                listaAlbumAux.agregarFinal(aux.dato)
                listaAlbumAux.artista = aux.dato.artista
                listaAlbumAux.album = aux.dato.album
                # print(listaAlbumAux.primero.dato.nombre) Con esto se accede a los atributos de la lista
                #de canciones desde la lista aux album
                listaAlbumes.agregarFinal(listaAlbumAux)

                # print(aux.dato.nombre)



        #print(aux.dato.ruta)#asi se accede a los atrubutos desde el auxiliar
        aux=aux.siguiente

    '''aqui se conectan las listas'''   
    aux=listaCanciones.primero
    #Recorremos las canciones cargadas
    while aux!=None:
        #Primero creamos los artristas
        if ListaArtistas2.vacia():
            # print('vacia')
            listaAuxArtista=ListaDobleArtista()
            listaAuxAlbum=ListaDobleAlbum()
            listaAuxArtista.artista=aux.dato.artista
            # print(aux.dato.artista, 'agregado')
            listaAuxAlbum.artista=aux.dato.artista
            listaAuxAlbum.album=aux.dato.album
            listaAuxAlbum.agregarFinal(aux)
            listaAuxArtista.agregarFinal(listaAuxAlbum)
            # print(listaAuxArtista.primero, 'ss')
            ListaArtistas2.agregarFinal(listaAuxArtista)
        else:
            #primero ver si el artista ya existe
            artistaEncontrado=False
            aux2=ListaArtistas2.primero
            while aux2!=None:
                if aux.dato.artista == aux2.dato.artista:
                    aux3=aux2.dato.primero
                    #aqui recorro la lista de albumes del artista
                    albumEncontrado=False
                    while aux3!= None:
                        if aux3.dato.album == aux.dato.album:

                            albumEncontrado=True
                            break
                        aux3=aux3.siguiente
                    if albumEncontrado:
                        aux3.dato.agregarFinal(aux)
                    else:
                        listaAuxAlbum=ListaDobleAlbum()
                        # print(aux.dato.artista, 'agregado')
                        listaAuxAlbum.artista=aux.dato.artista
                        listaAuxAlbum.album=aux.dato.album
                        listaAuxAlbum.agregarFinal(aux)
                        aux2.dato.agregarFinal(listaAuxAlbum)
                        # print(listaAuxArtista.primero, 'ss')
                        
                        # print(aux3.dato)
                    artistaEncontrado=True
                    break
                aux2=aux2.siguiente
            '''si el artista ya esta creado pasamos a la siguiente iteracion'''
            if artistaEncontrado:
                pass
            else:
                listaAuxArtista=ListaDobleArtista()
                listaAuxAlbum=ListaDobleAlbum()
                listaAuxArtista.artista=aux.dato.artista
                # print(aux.dato.artista, 'agregado')
                listaAuxAlbum.artista=aux.dato.artista
                listaAuxAlbum.album=aux.dato.album
                listaAuxAlbum.agregarFinal(aux)
                listaAuxArtista.agregarFinal(listaAuxAlbum)
                # print(listaAuxArtista.primero, 'ss')  
                ListaArtistas2.agregarFinal(listaAuxArtista)

        aux = aux.siguiente
    #Obteniendo datos
    aux = ListaArtistas2.primero
    while aux!= None:
        print('*'*25)
        print('artista', aux.dato.artista)
        aux2=aux.dato.primero
        '''Aqui se recorren los albumes del artista'''
        while aux2!= None:
            print('album', aux2.dato.album)
            aux3=aux2.dato.primero
            print('CANCIONES')
            while aux3!= None:
                print(aux3.dato.dato.nombre)
                aux3 = aux3.siguiente
            aux2=aux2.siguiente
        aux = aux.siguiente

def grf():
    global id, ListaArtistas2
    listaIdArtistas=ListaDoble()
    listaIdAlbumes=ListaDoble()
    id=0
    aux = ListaArtistas2.primero
    g = Digraph('gr', format='png')
    g.node(str(id), aux.dato.artista)
    idArtista1=id
    listaIdArtistas.agregarFinal(id)
    id+=1
    while aux!= None:
        aux=aux.siguiente
        if aux!= None:
            g.node(str(id), aux.dato.artista)
            g.edge(str(idArtista1), str(id), constraint='false')
            idArtista1=id
            listaIdArtistas.agregarFinal(id)
            id+=1
    auxArtista = listaIdArtistas.primero        
    aux = ListaArtistas2.primero
    while aux!= None:
        aux2=aux.dato.primero
        g.node(str(id), aux2.dato.album)
        listaIdAlbumes.agregarFinal(id)
        g.edge(str(auxArtista.dato), str(id))
        IdAlbum1 = id
        id+=1
    #Aqui se unen los albumes
        while aux2!= None:
            aux2 = aux2.siguiente
            if aux2!= None:
                g.node(str(id), aux2.dato.album)
                g.edge(str(IdAlbum1), str(id), constraint='false')
                g.edge(str(auxArtista.dato), str(id))
                listaIdAlbumes.agregarFinal(id)         
                IdAlbum1=id
                id+=1
                pass
        auxArtista=auxArtista.siguiente       
        aux = aux.siguiente
    #Ahora solo recorro las listas de artistas
    aux=ListaArtistas2.primero
    auxAlbum=listaIdAlbumes.primero

    while aux!= None:
        aux2=aux.dato.primero
        while aux2!=None:
            aux3 = aux2.dato.primero
            g.node(str(id), aux3.dato.dato.nombre)
            g.edge(str(auxAlbum.dato), str(id))
            idCancion1=id
            id+=1
            while aux3!= None:
                aux3 = aux3.siguiente
                if aux3!= None:
                    g.node(str(id), aux3.dato.dato.nombre)
                    g.edge(str(idCancion1), str(id), constraint='false')
                    g.edge(str(auxAlbum.dato), str(id))
                    idCancion1=id
                    id+=1

                    pass
            aux2=aux2.siguiente
            auxAlbum=auxAlbum.siguiente

        aux=aux.siguiente
    g.view()
    # while aux!= None:
    #     aux = aux.siguiente
    #     if aux!= None:
    #         g.node(str(id), aux.dato)
    #         print('*'*25)
    #         print('artista', aux.dato.artista)        
    #         aux2=aux.dato.primero
    #         '''Aqui se recorren los albumes del artista'''
    #         while aux2!= None:
    #             print('album', aux2.dato.album)
    #             aux3=aux2.dato.primero
    #             print('CANCIONES')
    #             while aux3!= None:
    #                 print(aux3.dato.dato.nombre)
    #                 aux3 = aux3.siguiente
    #             aux2=aux2.siguiente
    
def ReporteHtml():
    global listaActual, combo, listasCirculares
    contenido=''
    if combo.get()=='':
        msj='No se ha seleccionado ninguna lista de reproducción'
        messagebox.showwarning(message=msj, title="HTML")
        return
    try:

        listaOrdenada = copy.deepcopy(listasCirculares.primero)

        while listaOrdenada != None:
            # print('sxsx',listaActual.dato.nombre)
            if listaOrdenada.dato.nombre == combo.get():
                # print(listaActual.dato.nombre, 'es igual a ', combo.get())
                break
            listaOrdenada = listaOrdenada.siguiente
        
        # listaOrdenada = listaActual
        # listaOrdenada = copy.deepcopy(aux.dato)#Clonamos la lista de reproducción
        # print(listaOrdenada.dato.primero.dato.nombre, listasCirculares.primero.dato.primero.dato.nombre, 'primera cancion')
        listaOrdenada.dato.Ordenar()
        # print(listasCirculares.primero.dato.primero.dato.nombre, 'primera cancion')
        # listaActual.dato.Ordenar()
        titulo = combo.get()
        titulo = titulo+'.html'
        # self.textoConsola+='/n'+'REPORTASO'+str(j)            
        reporte = open(titulo, 'w')
        
        title = 'Reporte lista de reporduccion '+ combo.get()
        celdas = f'''<tr>
        <th>Cancion</th>
        <th>Album</th>
        <th>Artista</th>
        <th>Numero de veces reproducida</th>
        </tr>
        '''
        

            
        aux = listaOrdenada.dato.primero
        # print(listaActual.dato, 'llll')
        #tr son filas
        while aux:
            # print(aux.dato.nombre, aux.dato.reproducciones)
            
            celdas+=f'''<tr>
            <td>{aux.dato.nombre}</td>
            <td>{aux.dato.album}</td>   
            <td>{aux.dato.artista}</td>   
            <td>{aux.dato.reproducciones}</td>   

            </tr>
            '''

            aux = aux.siguiente
            if aux == listaOrdenada.dato.primero:
                break
        
        contenido=(f'''<html>
        <head>
        <style type="text/css">
        table, th, td {{
        border: 1px solid black;
            border-collapse: collapse;;
            }}
            
            </style>
            <title>REPORTE1</title>
            <body>
            <h1 style="text-align: center;"> {title} </h1>
            <table style="margin: 0 auto; width:75%">
            {celdas}
            </table>
        
        </body>
        <head>
        </html>
        ''')
        reporte.write(contenido)
        reporte.close()
        msj = 'Reporte HTML generado'
        messagebox.showinfo(message=msj, title='HTML')
    except:
        msj='Error al generar reporte HTML'
        messagebox.showerror(message=msj, title='Reporte HTML')

    
    
    # print(listaActual.dato) #Esto es uuna lista de reproduccion
    # print(listaActual.dato.primero.dato)

    # aux = listaActual.dato.primero
    # while aux:
    #     print(aux.dato.nombre, aux.dato.reproducciones)
    #     aux = aux.siguiente
    #     if aux == listaActual.dato.primero:
    #         break


def generarXml():
    global listasCirculares, listasReproduccion
    try:
        titulo = 'listasReproduccion.xml'
        reporte = open(titulo, 'w')
        
        contenido = '<?xml version="1.0" encoding="UTF-8"?>\n<ListasReproducción>\n'
        
        aux = listasCirculares.primero #Esta es la primera lista de reproduccion
        # print(aux.dato)
        # print(aux2, '2')
        # print(aux.dato.primero, '1')
        #Recorriendo las listas de reproduccion
        while aux !=None:
            aux2 = aux.dato.primero #Esta es la primera cancion

            contenido+=f'   <Lista nombre="{aux.dato.nombre}">\n'
            
            while aux2:
                
                contenido+=f'   <cancion nombre="{aux2.dato.nombre}">\n'
                contenido+=f'       <artista> {aux2.dato.artista} </artista>\n'
                contenido+=f'       <album> {aux2.dato.album} </album>\n'
                contenido+=f'       <vecesReproducidas> {aux2.dato.reproducciones} </vecesReproducidas>\n'
                contenido+=f'       <imagen> {aux2.dato.imagen} </imagen>\n'
                contenido+=f'       <ruta> {aux2.dato.ruta} </ruta>\n'
                contenido+=f'   </cancion>\n'



                aux2 = aux2.siguiente
                if aux2 == aux.dato.primero:
                    break
            contenido+='    </Lista>\n'
            aux = aux.siguiente
        
        contenido+='</ListasReproducción>\n'
        reporte.write(contenido)
        reporte.close()
        msj = 'Archivo xml generado'
        messagebox.showinfo(message=msj, title="xml")
    except:
        messagebox.showerror(message='Error al generar xml', title='archivo xml')

    
        
def CargarMILista():
    global ruta, listaAlbumes, listaCanciones, listaArtistas, ventana, var, listaC, listaVar
    global listasCirculares, listasReproduccion, listasReproduccionBox, pila, ruta, pilaNombre
    try:

        ruta = easygui.fileopenbox()
        messagebox.showinfo(message='Archivo cargado', title='Cargar archivo')
    except:
        messagebox.showerror(message='Error al cargar el archivo de las listas', title='Cargar archivo')
    tree = ET.parse(ruta)
    root = tree.getroot()
    for i in range (len(root)):
        listasReproduccion = ListaCircular()
        listasReproduccion.nombre = root[i].attrib["nombre"].strip(' ').replace('"',' ')
        pilaAux = []
        for j in range(len(root[i])):
            

            nuevaCancion = Cancion()
            
            nuevaCancion.nombre = root[i][j].attrib["nombre"]
            # print(nuevaCancion.nombre)
            for k in range(len(root[i][j])):
                if root[i][j][k].tag == 'artista':
                    nuevaCancion.artista = root[i][j][k].text.strip(' ').replace('"', '')
                elif root[i][j][k].tag == 'album':
                    nuevaCancion.album = root[i][j][k].text.strip(' ').replace('"', '')
                elif root[i][j][k].tag == 'vecesReproducidas':
                    nuevaCancion.reproducciones = int(root[i][j][k].text.strip(' ').replace('"', ''))
                elif root[i][j][k].tag == 'imagen':
                    nuevaCancion.imagen = root[i][j][k].text.strip(' ').replace('"', '')
                elif root[i][j][k].tag == 'ruta':
                    nuevaCancion.ruta = root[i][j][k].text.strip(' ').replace('"', '')
            # listaCanciones.agregarFinal(nuevaCancion)
            listasReproduccion.agregarFinal(nuevaCancion)
            pilaAux.append(nuevaCancion)

        listasCirculares.agregarFinal(listasReproduccion)
        listasReproduccionBox.append(listasReproduccion.nombre)
        pila.append(pilaAux[:])
        pilaNombre.append(listasReproduccion.nombre)
        combo.configure(values=(listasReproduccionBox))


    # AnidarListas()
    # CrearCheckbox()
def ReproducirAlbum():
    global comboAlbumes, albumActual, reproducir, pausa, reproduciendoAlbum, listasCircularesAlbumes
    global listaAlbum
    if comboAlbumes.get()== '':
        msj = 'No se ha seleccionado ningun album'
        messagebox.showwarning(message=msj, title="HTML")
        return
    try:
        aux = listaAlbumes.primero
        albumActual = ListaCircular()
        while aux!= None:
            aux2 = aux.dato.primero
            if aux.dato.album == comboAlbumes.get():
                while aux2 != None:

                    # print(aux2.dato.nombre)
                    albumActual.agregarFinal(aux2.dato)
                    aux2 = aux2.siguiente
                
                reproduciendoAlbum = True
                break
            
            aux = aux.siguiente
        Play()
    except:
        messagebox.showerror(message='Error al reproducir album', title='Reproducir album')

    pass
def Albumes():
    global listaAlbumes, albumesBox
    aux = listaAlbumes.primero
    while aux!= None:
        if aux.dato.album == 'single':
            pass
        else:
            albumesBox.append(aux.dato.album)
        aux = aux.siguiente

    comboAlbumes.config(values=albumesBox)

            

ventana = tk.Tk()
var = tk.StringVar()

fuente = tkFont.Font(family="Arial", size=15)
fuenteLabel = tkFont.Font(family="Arial", size=35)

ventana.geometry('1500x1000+170+10')
ventana.title('Manejo Grid')
ventana.configure(bg='white')

botonCargar = tk.Button(ventana, text="Seleccionar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonCargar.pack()
botonCargar.place(x=25, y=10)

botonRHtml = tk.Button(ventana, text="Reporte HTML", command=ReporteHtml, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonRHtml.pack()
botonRHtml.place(x=250, y=10)

botonRGraphviz = tk.Button(ventana, text="Reporte Graphviz", command=grf, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonRGraphviz.pack()
botonRGraphviz.place(x=475, y=10)

imgPlay = PhotoImage(file=f'../Img/play1.png')
botonReproducir = tk.Button(ventana, command=Play, image=imgPlay)
botonReproducir.pack()
botonReproducir.place(x=750, y=100)

imgNext = PhotoImage(file='../Img/next.png')
botonNext = tk.Button(ventana, command=Siguiente, image=imgNext)
botonNext.pack()
botonNext.place(x=1300, y=800)

imgAnterior = PhotoImage(file='../Img/anterior.png')
botonAnterior = tk.Button(ventana, command=Anterior, image=imgAnterior)
botonAnterior.pack()
botonAnterior.place(x=750, y=800)

imgStop = PhotoImage(file='../Img/stop.png')
botonStop = tk.Button(ventana, command=Stop, image=imgStop)
botonStop.pack()
botonStop.place(x=1300, y=100)

imgPausa = PhotoImage(file=f'../Img/pausa1.png')



label = tk.Label(ventana, fg='black', bg='thistle', text=txtLabel, font=fuenteLabel)
label.pack()
label.place(x=820, y=270, width=600, height=500)
label.configure(justify="left")

imgCancion = PhotoImage(file='../Img/blanco.png')
labelImgCancion = tk.Label(ventana, image=imgCancion, width=300, height=300)
labelImgCancion.pack()
labelImgCancion.place(x=500, y=350)

labelCanciones = tk.Label(ventana, text='Canciones Disponibles', font=fuente, bg='red', fg = 'white')
labelCanciones.pack()
labelCanciones.place(x=20, y =100)

botonCrearListaReproduccion = tk.Button(ventana, command=obtenerOpcion, text='Crear Lista de Reproduccion', font=fuente, bg='midnightblue', fg = 'white', activebackground="powderblue")
botonCrearListaReproduccion.pack()
botonCrearListaReproduccion.place(x=400, y=900)

LabelCbox = tk.Label(ventana,text='LISTAS DE REPRODUCCION DISPONIBLES', font=fuente)
LabelCbox.pack()
LabelCbox.place(x=900, y=25)
combo = ttk.Combobox(ventana, state="readonly")
combo.place(x=1000, y=100)
combo['values'] = (listasReproduccionBox)

labelNombreLista = tk.Label(ventana, text='Nombre de la lista', font=fuente, bg='red', fg = 'white')
labelNombreLista.pack()
labelNombreLista.place(x=250, y =800)

text = tk.Text(ventana, font = fuente, width=25, height=1)
text.pack()
text.place(x=430, y =800)

Aleatorio = BooleanVar()
Aleatorio.set(False)
RedioButonNormal = tk.Radiobutton(ventana, text='Normal', value=False, font=fuente, variable=Aleatorio, bg='lavender', fg = 'black', activebackground="powderblue").place(x=920, y=850)
RedioButonAleatorio = tk.Radiobutton(ventana, text='Aleatorio', value=True, font=fuente, variable=Aleatorio, bg='lavender', fg = 'black', activebackground="powderblue").place(x=1100, y=850)

botonGenerarXml = tk.Button(ventana, text="Exportar listas", command=generarXml, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonGenerarXml.pack()
botonGenerarXml.place(x=700, y=10)

botonCragarMiLista = tk.Button(ventana, text="Cargar Mis Listas", command=CargarMILista, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonCragarMiLista.pack()
botonCragarMiLista.place(x=470, y=720)

LabelCboxAlbumes = tk.Label(ventana,text='Albumes disponibles', font=fuente, bg='red', fg = 'white')
LabelCboxAlbumes.pack()
LabelCboxAlbumes.place(x=300, y=100)
comboAlbumes = ttk.Combobox(ventana, state="readonly")
comboAlbumes.place(x=300, y=150)
comboAlbumes['values'] = (albumesBox)

botonReproducirAlbum = tk.Button(ventana, command=ReproducirAlbum, text='Reproducir Album', font=fuente, bg='midnightblue', fg = 'white', activebackground="powderblue")
botonReproducirAlbum.pack()
botonReproducirAlbum.place(x=290, y=200)

# LeerXml()
# Graphviz()
# funcion()
# Albumes()
ventana.mainloop()
# opcionCancion = tk.Radiobutton(ventana, text='cancion 1', value=1, variable=var)
# opcionCancion.pack
# opcionCancion.place(x=20, y=200)






