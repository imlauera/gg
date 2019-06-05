#!/usr/bin/bash

File="GGG.py"
File2="gg.py"
NOP=5
Dir="ejemplos"

#for i in $(ls $Dir); do 
#  python $File2 $Dir/$i  &
#  PID=$!
#  sleep $NOP; kill -9 $PID
#done



echo -ne "\033[92mLeyendo archivos: $i \033[0m"
for i in $(ls $Dir); do 
  echo -e "\033[91m$i \033[0m"
  (
    sleep $NOP;
    echo -e "\n"
  ) | python2 $File $Dir/$i  
done

