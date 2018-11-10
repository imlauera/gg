## Graficador de grafos

### Instalación
Para la instalación primero, vamos a necesitar descargar [py-gnuplot](http://sourceforge.net/projects/gnuplot-py/files/latest/download?source=files).  
Lo descomprimimos y ejecutamos: `python setup.py install`, es lo que nos va a permitir interactuar con *GnuPlot* desde Python. 
Luego instalamos gnuplot con `sudo apt-get install gnuplot` o `dnf install gnuplot` en Fedora
o [compilándolo](https://sourceforge.net/projects/gnuplot/files/gnuplot/) con `./configure --enable-qt && sudo make clean install`.  
Observación: Debería instalarse con suporte para la terminal qt que viene incluído en el caso de instalarlo con `apt-get`.

#### Para iniciarlo:  
`python gg.py archivo`  
Se puede mirar cualquiera de los ejemplos para entender el formato de entrada.

### Pruebas
![alt text](/img/k8.png)
![alt text](/img/k2-3.png)
![alt text](/img/r4.png)
![alt text](/img/k1-12.png)
![alt text](/img/butterfly.png)
