#!/usr/bin/python

import math
import sys
import string
import time
import Gnuplot as gp
import random
import numpy

def iniciar_vertices(V,ancho,alto):
  pos = {}
  for v in V:
    pos[v] = (random.random()*800,random.random()*300)
  return pos

def fa(x,k):
  return float((x**2)/k)
def fr(x,k):
  return float((k**2)/x)
def cool(t):
  if t > 1:
    return t - 0.15
  elif t > 0:
    return t - 0.001
  else:
    return 0

def modulo_vector(x,y):
  return math.sqrt((x)**2+(y)**2)

def run_layout(grafo,ancho,alto,M):
  while True:
    try:
      (V,E) = grafo
      V = set(V)
      area = ancho*alto
      k = float(0.6*math.sqrt(area/len(V)))

      t = float(10.0)

      disp = {}
      for v in V:
        disp[v] = (0.0,0.0)

      pos = iniciar_vertices(V,ancho,alto)
      for i in range(0,M):
        #print "El valor de M es: %s",M
        for v in V:
          disp[v] = (0.0,0.0)
          # Fuerza repulsion
          for u in V:
            if (u != v):
              Delta = tuple(numpy.subtract(pos[v],pos[u]))
              x,y = Delta
              Modulo_Delta = modulo_vector(x,y)
              Delta_sobre_modulo = tuple(d/Modulo_Delta for d in Delta)
              # aux = D/|D| * fr(|D|)
              aux = tuple(q*fr(Modulo_Delta,k) for q in Delta_sobre_modulo)
              # v.disp = v.disp + D/|D| * fr(|D|)
              disp[v] = tuple(numpy.add(disp[v],aux))
        # Fuerza atraccion.
        for (g,h) in E:
          Delta = tuple(numpy.subtract(pos[g],pos[h]))
          
          x,y = Delta
          Modulo_Delta = modulo_vector(x,y)
          
          Delta_sobre_modulo = tuple(float(d)/float(Modulo_Delta) for d in Delta)
          aux = tuple(p*fa(Modulo_Delta,k) for p in Delta_sobre_modulo)
          disp[g] = tuple(numpy.subtract(disp[g],aux))
          disp[h] = tuple(numpy.add(disp[h],aux))
          # Limitamos desplazamiento.
          # Esta forma de calcular la posicion del vertice es una basura.
        for v in V:
          a,b = disp[v]
          displen = modulo_vector(a,b)
          aux = tuple( (dd/(displen)*t) for dd in disp[v])
          pos[v] = tuple(numpy.add(pos[v],aux))
          a,b = pos[v]
          pos[v] = (min(ancho/2,max(-ancho/2,a)),
               min(alto/2,max(-alto/2,b)))

        t = cool(t)
        yield pos,V,E

    except ZeroDivisionError:
      continue
    break

def dibujar_vertice():
  cmd = 'set object %s circle front center %s,%s size 6 fc rgb'
  colores = ['"white"']
  black = '"#000000"';
  cmd =  cmd + "{} fs solid border lc rgb {}".format(random.choice(colores),black)
  return cmd

def dibujar_arista():
        cmd = 'set arrow nohead from %s,%s to %s,%s filled back lw 3 lc rgb'
        colores = ['"#913188"','"#ff0042"','"#237b34"','"#267396"','"#aab319"','"#a91a70"']
        cmd =  cmd+random.choice(colores)
        return cmd


ancho_ventana = 'set term qt size %s,%s'

def graficar(G,ancho,alto,M):
  g = gp.Gnuplot()
  cmd = ancho_ventana % (ancho,alto)
  g(cmd)
  #g('set terminal svg persist')
  g('set key off')
  #g('set background rgb black')
  g('unset xtics')
  g('unset ytics')
  g('unset border')
  g('unset key')
  
  # Cantidad de puntos en el rango x e y
  g(('set xrange [0:{}]; set yrange [0:{}]').format(800,550))
  
  g('plot NaN')
  for pos,V,E in run_layout(G,ancho,alto,M):
    g('unset arrow')
    # Dibujamos vertices
    id_vertice = 1
    for v in V:
      x,y = pos[v]
      cmd = dibujar_vertice()
      cmd = cmd % (id_vertice,x,y)
      g(cmd)
      id_vertice += 1
    # Dibujamos aristas
    for ar in E:
      a,b = pos[ar[0]]
      c,d = pos[ar[1]]
      cmd = dibujar_arista()
      cmd = cmd % (a,b,c,d)
      g(cmd);
    g('replot')
  while True:
    time.sleep(100)

def lee_grafo_archivo(file_path):
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
  if len(sys.argv) < 2:
    print('Uso: python gg.py <archivo>')
    return

  G = lee_grafo_archivo(sys.argv[1])
  graficar(G,1000,550,250)


if __name__ == '__main__':
  main()
