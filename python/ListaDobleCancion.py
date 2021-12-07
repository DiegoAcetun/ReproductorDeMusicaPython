from Nodo import Nodo
class ListaDobleCancion():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nombre = None
        self.ruta = None
        self.imagen = None
        self.album = None
        self.artista = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)

        else:
            aux =  self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux

        self.size+=1

    def eliminarFinal(self):
        if self.vacia():
            print('la lista esta vacia')
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0

        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

    def agregarInicio(self, dato):
        if self.vacia(): 
            self.primero = self.ultimo = Nodo(dato)

        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux

        self.size+=1

    def eliminarInicio(self):
        if self.vacia():
            print('lista vacia')
        elif self.primero.siguiente == None: #Solo hay un elemento en la lista
            self.primero = self.ultimo = None
            self.size = 0

        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -=1

    def recorrerInicio(self):
        aux = self.primero
        while aux!=None:
            print(aux.dato) 
            aux = aux.siguiente

    def recorrerFinal(self):
        aux = self.ultimo
        while aux!=None:
            print(aux.dato)
            aux = aux.anterior