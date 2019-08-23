#!/usr/bin/bash

File="GGG.py"
NOP=5
Dir="ejemplos"

echo -ne "\e[1mLeyendo archivos desde la carpeta \e[42m$Dir\e[0m: \e[0m \n"
for i in $(ls $Dir); do 
  echo -ne "\033[34m$i\033[0m, "
  (
    sleep $NOP;
    echo -e '\n'
  ) | python2 $File $Dir/$i > /dev/null || break
done

