import random                         # Importa el módulo 'random' para poder barajar (shuffle) las cartas.

class DequeEmptyError(Exception):     # Define una excepción propia para "deque (cola doble) vacío".
    pass                             

# Clase Carta


class Carta: #defino cartas
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible = True #false para no ver la carta y true para si ver la carta

  
    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

  
    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        self._palo = palo

    # valores
    def _valor_numerico(self):
        valores = ['J','Q','K','A']
        if self.valor in valores:
            idx = valores.index(self.valor)
            return (11 + idx)
        return int(self.valor)    
    # comparo
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()

    # dado vuelta
    def __str__(self):
        if self.visible == False:
            return "-X"
        else:
            return self.valor + self.palo
    
    def __repr__(self):
        return str(self)


# Nodo para lista doble

class Nodo:
    def __init__(self, dato):        
        self.dato = dato             
        self.sig = None               
        self.ant = None              


# Lista doblemente enlazada
class ListaDobleEnlazada:
    def __init__(self):               
        self.cabeza = None           
        self.cola = None              
        self._tamanio = 0             

    def agregar_final(self, dato):   
        nuevo = Nodo(dato)            
        if self.cola is None:         
            self.cabeza = self.cola = nuevo  
        else:                         
            self.cola.sig = nuevo     
            nuevo.ant = self.cola    
            self.cola = nuevo         
        self._tamanio += 1            

    def extraer_inicio(self):         
        if self.cabeza is None:      
            raise DequeEmptyError("La lista está vacía")  
        dato = self.cabeza.dato       
        self.cabeza = self.cabeza.sig 
        if self.cabeza:               
            self.cabeza.ant = None    
        else:                         
            self.cola = None          
        self._tamanio -= 1            
        return dato                   

    def __len__(self):                
        return self._tamanio          

