import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import easygui
import xml.etree.ElementTree as ET

from pygame import mixer
ruta = ''; cancion = ''; pausa = False; botonReproducir = None; botonPausa = None; imgPausa = None; imgPlay = None
reproducir = True; botonNext = None; txtLabel = 'Cancion: \n Artista: \n Album:'
from tkinter import *
from ListaDoble import ListaDoble

def Play():
    global ruta, cancion, pausa, botonPausa, botonReproducir, imgPausa, imgPlay, reproducir
    mixer.init()
    cancion = '../Musica/heroes.mp3'
    if reproducir:
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        reproducir = False
        botonReproducir.configure(image=imgPausa)
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
    global cancion
    mixer.music.stop()
    cancion = '../Musica/alone.mp3'
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    

def Cargar():
    global ruta, cancion, pausa, botonReproducir, botonPausa, imgPausa
    ruta = easygui.fileopenbox()  
    print(ruta)
    cancion = '../Musica/Alone.mp3'
def Pausa(): 
    global pausa, botonPausa, botonReproducir, imgPausa
    mixer.music.pause()
    pausa = True
    
def Stop():
    global pausa, botonPausa, botonReproducir, imgPausa, reproducir
    mixer.music.stop()
    pausa = False
    reproducir = True
    botonReproducir.configure(image=imgPlay)

def LeerXml():
    global ruta
    tree = ET.parse("../archivos/1.xml")
    root = tree.getroot()
    for i in range(len(root)):

        nombreCancion = (root[i].attrib) #Por cada iteracion guadar el nombre de cada cancion en un dicc

        nombreCancion = nombreCancion["nombre"] #Esto devuelve solo el nombre de la cancion sin la etiqueta
        #nombre
        #Posicion 0 de la lista es la etiqueta cancion
        # print(root[0][0].text)

        #Recorriendo etiqueta cancion
        for j in range(len(root[0])):
            print(root[i][j].text)
        print('*'*20)
    
    
    

    pass


ventana = tk.Tk()
fuente = tkFont.Font(family="Arial", size=15)
fuenteLabel = tkFont.Font(family="Arial", size=35)

ventana.geometry('1500x1000+170+10')
ventana.title('Manejo Grid')
ventana.configure(bg='white')

botonCargar = tk.Button(ventana, text="Seleccionar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonCargar.pack()
botonCargar.place(x=25, y=10)

botonRHtml = tk.Button(ventana, text="Reporte HTML", command=LeerXml, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
botonRHtml.pack()
botonRHtml.place(x=250, y=10)

botonRGraphviz = tk.Button(ventana, text="Reporte Graphviz", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue", font=fuente)
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
botonAnterior = tk.Button(ventana, command=Play, image=imgAnterior)
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

imgCancion = PhotoImage(file='../Img/alone.png')
labelImgCancion = tk.Label(ventana, image=imgCancion)
labelImgCancion.pack()
labelImgCancion.place(x=500, y=350)
# ventana.mainloop()
LeerXml()