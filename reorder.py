#!/usr/bin/python

import os, math, sys

src = sys,argv[1] if len(sys.argv) > 2 else : '.'
  

def newNameFactory(list_size):
  
  pad = int(math.log10(list_size-1))+1 if list_size > 1 else 0
  
  def newName(file): 
    (name, ext) = os.path.splitext(file)
    number = int(name)
    newPos = list_size -1 - number / 2 if ((number % 4) in (0,3)) else number / 2
    computedName = str(newPos).zfill(pad)
    return computedName, name, ext
  
  return newName
    
  
files = [f for f in os.listdir(src) if not f.startswith('.')]

newName = newNameFactory(len(files))

for f in files:
  (computedName, oldName, ext) = newName(f)
  print src + '/'+ f, src+'/_'+ computedName + ext
  os.rename(src + '/'+ f, src+'/_'+ computedName +ext)
  
for f in os.listdir(src):
  os.rename(src + '/'+ f, src+'/'+ f[1:])
  