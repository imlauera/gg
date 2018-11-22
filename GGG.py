#! /usr/bin/env python3

import argparse
import Gnuplot
import logs

class LayoutGraph:
  def __init__(self, grafo, iters, refresh, c1, c2, verbose=False):
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

    # Inicializo estado
    self.posiciones = {}
    self.fuerzas = {}        
    
    self.iters = iters
    self.refresh = refresh
    self.c1 = 1.0
    self.c2 = 2.5


  def randomize_node_positions(self):
    ''' Inicializa en forma aleatoria las posiciones de los nodos'''
    (V,E) = self.grafo
    for v in V:
      self.posiciones[v] = (random.random()*width,random.random()*height)
    pass


  def step(self):
    ''' Efectua un paso de la simulacion fisica y actualiza las posiciones de los nodos'''

    # 1: Calcular repulsiones de nodos (actualiza fuerzas)
    # 2: Calcular atracciones de aristas (actualiza fuerzas)
    # 3: Calcular fuerza de gravedad (opcional)
    # 4: En base a fuerzas, actualizar posiciones, setear fuerzas a cero
    
    pass


  def create_view(self,width,height):
    ''' Inicializa GNUplot o la alternativa usada '''
    self.gplot = gp.Gnuplot()
    size = 'set terminal qt size {},{}'.format(width,height)
    self.gplot(size)

    # TODO: Usar variables para representar la cantidad de puntos en los ejes.
    self.gplot('
      set terminal qt persist;
      set key off;
      unset xtics;unset ytics;unset border;unset key;
      set xrange [0:880];  set yrange[0:550]
      ')

    self.gplot('plot NaN')

  def dibujar(self):
    ''' Dibuja el estado del grafo en pantalla'''
    for V,E in self.grafo:
      
      
    self.gplot('replot NaN')


  def leer_grafo(self,file_path):
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
    for i in range(0, self.iters):
        # Realizar un paso de la simulacion
        self.step()
            
        # Si es necesario, lo mostramos por pantalla
        if (self.refresh > 0 and i % self.refresh == 0):
            self.dibujar()
    
    # Ultimo dibujado al final
    self.dibujar()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', 
                        action='store_true', 
                        help='Muestra mas informacion')

    parser.add_argument('--iters', type=int, 
                        help='Cantidad de iteraciones a efectuar', 
                        default=50)

    parser.add_argument('file_name', 
                        help='Archivo del cual leer el grafo a dibujar')

    args = parser.parse_args()

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(
        layout_gr.leer_grafo(file_name), 
        iters=args.iters,
        refresh=1,
        c1=2.0,
        c2=2.5,
        )
    
    # Ejecutamos el layout
    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
