#!/usr/bin/bash

File="gg.py"
NOP=7
Dir="ejemplos"

#for i in $(ls $Dir); do 
#  while : ; do
#    python $File $Dir/$i  &
#    PID=$!
#    echo -n "Otra vez? [y/N]"; read AGAIN; kill -9 $PID
#    echo $AGAIN
#    if [ -z $AGAIN ]; then break; fi
#  done
#done


echo -ne "\033[92mLeyendo archivos: $i \033[0m"
for i in $(ls $Dir); do 
  python $File $Dir/$i  &
  echo -e "\033[91m$i \033[0m"
  PID=$!
  sleep $NOP; kill -9 $PID > /dev/null
done

