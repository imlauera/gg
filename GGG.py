#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import Gnuplot as gp
import math
import random
import numpy

class LayoutGraph:
  def __init__(self, grafo, iters, refresh, c1, c2, width, height, verbose=False):
    '''    
    Parametros de layout:
    iters: cantidad de iteraciones a realizar
    refresh: Numero de iteraciones entre actualizaciones de pantalla. 
    0 -> se grafica solo al final.
    c1: constante usada para calcular la repulsion entre nodos
    c2: constante usada para calcular la atraccion de aristas
    '''

    # Guardo el grafo
    self.grafo = grafo
    (self.V,self.E) = grafo
    self.width,self.height = width,height
    self.area = self.width*self.height

    # Inicializo estado
    self.posiciones = {}
    self.fuerzas = {}        
    
    self.iters = iters
    self.refresh = refresh
    # self.c1*fa(x,k)
    self.c1 = c1
    self.c2 = c2
    # x11,qt o wxt
    self.term = 'x11'

    # Ejes
    # Ancho
    self.max_x1,self.max_x2 = 50,600
    # Alto
    self.max_y1,self.max_y2 = -100,400


    self.formato_arista = 'set arrow nohead from {},{} to {},{} filled back lw 7 lc rgb {}'
    self.lista_colores_arista = ['"#7c79ff"','"#4493ed"','"#757cf4"']
    #self.lista_colores_arista = ['"#fc5226"','"#000"']
    self.formato_vertice = 'set object {} circle front center {},{} size 5 fc rgb {} fs solid noborder'
    self.lista_colores_vertice = ['"#dcb2dc"']


    self.k = float(0.6*math.sqrt(self.area/len(self.V)))
    self.t = float(24.0)


  def randomize_node_positions(self):
    for v in self.V:
      self.posiciones[v] = (random.random()*self.width/1.5,random.random()*self.height/1.7)
  # Fuerza atraccion
  def fa(self,delta):
    return float(self.c2*(delta**2)/self.k)
  # F. repulsion
  def fr(self,delta):
    return float(self.c1*(self.k**2)/delta)
  def cool(self):
    if self.t > 1:
      self.t = self.t - 0.15
    elif self.t > 0:
      self.t = self.t - 0.001
    else:
      return 0

  def step(self):
    ''' Efectua un paso de la simulacion fisica y actualiza las posiciones de los nodos'''
    for v in set(self.V):
      self.fuerzas[v] = (0.0,0.0)
      for u in set(self.V):
        if (u != v):
          Delta = tuple(numpy.subtract(self.posiciones[v],self.posiciones[u]))
          x,y = Delta
          Modulo_Delta = math.sqrt(x**2+y**2)
          if (Modulo_Delta != 0):
            Delta_sobre_modulo = tuple(d/Modulo_Delta for d in Delta)
            aux = tuple(q*self.fr(Modulo_Delta) for q in Delta_sobre_modulo)
            self.fuerzas[v] = tuple(numpy.add(self.fuerzas[v],aux))

    # Fuerza atraccion
    for (g,h) in self.E:
      Delta = tuple(numpy.subtract(self.posiciones[g],self.posiciones[h]))
      x,y = Delta
      Modulo_Delta = math.sqrt(x**2+y**2)
      if(Modulo_Delta != 0):
        Delta_sobre_modulo = tuple(float(d)/float(Modulo_Delta) for d in Delta)
        aux = tuple(p*self.fa(Modulo_Delta) for p in Delta_sobre_modulo)
        self.fuerzas[g] = tuple(numpy.subtract(self.fuerzas[g],aux))
        self.fuerzas[h] = tuple(numpy.add(self.fuerzas[h],aux))
    # Limitamos el desplazamiento.
    for v in set(self.V):
      a,b = self.fuerzas[v]
      displen = math.sqrt(a**2+b**2)
      aux = tuple( (dd/(displen) * min(displen,self.t)) for dd in self.fuerzas[v])
      self.posiciones[v] = tuple(numpy.add(self.posiciones[v],aux))
      a,b = self.posiciones[v]
      '''
      Funciona pero no lo necesito porque agrando los ejes y me deja como un cuadrado el c15
      self.posiciones[v] = (min(self.width/2,max(-self.width/2,a)),
                            min(self.height/2,max(-self.height/2,b)))
      '''
    self.cool()

  def actualizar_ejes(self):
    for x,y in self.posiciones.values():
      if(x>= self.max_x2):
        self.max_x2 = x;
      elif (x<=self.max_x1):
        self.max_x1 = x-20;
      elif(y >= self.max_y2):
        self.max_y2 = y+50;
      elif(y<=self.max_y1):
        self.max_y1 = y-50
      self.gplot(('set xrange [{}:{}]; set yrange [{}:{}]').format(self.max_x1,self.max_x2,self.max_y1,self.max_y2))


  def create_view(self):
    self.gplot = gp.Gnuplot()

    size = "set term {} linewidth 6.5 size {},{}".format(self.term,self.width,self.height)
    # size = "set term {} size {},{}".format(self.term,self.width,self.height)
    self.gplot(size)

    self.gplot(('''
      unset border;
      unset xtics;
      unset ytics;
      unset key;
      set xrange [{}:{}];
      set yrange [{}:{}];''').format(self.max_x1,self.max_x2,self.max_y1,self.max_y2))

    self.gplot('plot NaN')


  def dibujar(self):
    ''' Dibuja el estado del grafo en pantalla'''
    # Limpiar anterior dibujo.
    self.gplot('unset arrow')
    id_vertice = 1
    for v in set(self.V):
      x,y = self.posiciones[v]
      Dibujar_Vertice = (self.formato_vertice+" ").format(id_vertice,x,y,random.choice(self.lista_colores_vertice))
      self.gplot(Dibujar_Vertice)
      id_vertice += 1
    for e in self.E:
      a,b = self.posiciones[e[0]]
      c,d = self.posiciones[e[1]]
      Dibujar_Arista = (self.formato_arista+" ").format(a,b,c,d,random.choice(self.lista_colores_arista))
      self.gplot(Dibujar_Arista)

    #self.actualizar_ejes()
    self.actualizar_ejes()
    self.gplot('replot')

  def layout(self):
    '''
    Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar) 
    un layout        
    '''
    # Inicializamos la 'pantalla'
    self.create_view()

    # Inicializamos las posiciones
    self.randomize_node_positions()

    # Si es necesario, lo mostramos por pantalla
    if (self.refresh > 0):
        self.dibujar()

    # Bucle principal
    for i in range(0,self.iters):
        # Realizar un paso de la simulacion
        self.step()

        # Si es necesario, lo mostramos por pantalla
        if (self.refresh > 0 and i % self.refresh == 0):
            self.dibujar()
    
    # Ultimo dibujado al final
    self.dibujar()


def leer_grafo(file_path):
  ''' Lee grafo desde un archivo '''
  count = 0 
  with open(file_path,'r') as f:
    cantidad = int(f.readline())

    Vertices = []
    for i in range(0,cantidad):
      elem = f.readline().strip()
      Vertices.append(elem)
    
    Aristas = []
    for line in f:
      elem = line.strip().split()
      Aristas.append(tuple(elem))

  G = (Vertices,Aristas)

  return G


def main():
  parser = argparse.ArgumentParser()

  parser.add_argument('-v', '--verbose', 
                      action='store_true', 
                      help='Muestra mas informacion')
  parser.add_argument('--iters', type=int, 
                      help='Cantidad de iteraciones a efectuar', 
                      default=250)
  parser.add_argument('file_name', 
                      help='Archivo del cual leer el grafo a dibujar')
  args = parser.parse_args()

  # Creamos nuestro objeto LayoutGraph
  layout_gr = LayoutGraph(
    leer_grafo(args.file_name), 
    iters=args.iters,
    refresh=1,
    # Repulsion
    c1=0.4,
    # Atraccion
    c2=0.5,
    width=800,
    height=650
  )
    
  # Ejecutamos el layout
  layout_gr.layout()
  print("Press enter to exit")
  raw_input()
  return

if __name__ == '__main__':
    main()
