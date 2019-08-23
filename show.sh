#!/usr/bin/bash

File="GGG.py"
NOP=5
Dir="ejemplos"

echo -ne "\033[1mLeyendo archivos desde $Dir/: \033[0m \n"
for i in $(ls $Dir); do 
  echo -ne "\033[91m$i\033[0m, "
  (
    sleep $NOP;
    echo -e '\n'
  ) | python2 $File $Dir/$i > /dev/null || break
done

