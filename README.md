## Graficador de grafos

### Instalación
Para la instalación primero, vamos a necesitar descargar [py-gnuplot](http://sourceforge.net/projects/gnuplot-py/files/latest/download?source=files).
Lo descomprimimos y ejecutamos: `python setup.py install`, es lo que nos va a permitir interactuar con *GnuPlot* desde Python.
Luego instalamos gnuplot con `sudo apt-get install gnuplot` en el caso de Ubuntu,Linux Mint, Debian o `dnf install gnuplot` en Fedora
o compilándolo desde acá: [gnuplot](https://sourceforge.net/projects/gnuplot/files/gnuplot/) con 
`./configure --enable-qt && sudo make clean install`.

#### Para iniciarlo:  
`python gg.py ejemplos/k8.tgf`
