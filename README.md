## Graficador de grafos

### Instalación
Para la instalación primero, vamos a necesitar descargar py-gnuplot o `pip install py-gnuplot`, este paquete nos
va a permitir interactuar con *GnuPlot* desde Python.   

O también se puede instalar py-gnuplot manualmente:
```
wget http://downloads.sourceforge.net/project/gnuplot-py/Gnuplot-py/1.8/gnuplot-py-1.8.tar.gz
tar xzf gnuplot-py-1.8.tar.gz
cd gnuplot-py-1.8/
python setup.py install
```
Luego instalamos gnuplot con `sudo apt-get install gnuplot` o `dnf install gnuplot` en Fedora
o [compilándolo](https://sourceforge.net/projects/gnuplot/files/gnuplot/) con `./configure --enable-qt && sudo make clean install`.  
Obs.: Me compiló pero no me instaló la terminal qt, debería instalarse con soporte para la terminal qt que viene incluído en el caso de instalarlo con `apt-get` y también viene instalado con `dnf` en el caso de Fedora.

### Para iniciarlo
`python gg.py nombre del archivo`  
Se puede mirar cualquiera de los archivos en el directorio "ejemplos" para entender el formato de entrada.

