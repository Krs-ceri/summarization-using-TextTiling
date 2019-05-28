#!/usr/bin/python

import sys
import os
import os.path
import shutil
import nltk
import math
import re
import pylab
from nltk.corpus import stopwords
from nltk.tokenize import TextTilingTokenizer
try: 
    import numpy
except ImportError:
    pass


directory = "srt/trs"
tmp = "{}/tmp/".format(directory)
    
tiling = "{}/test/".format(directory)
if os.path.exists(tiling):
    shutil.rmtree(tiling)
os.mkdir(tiling)
i = 0    
for filename in os.listdir(tmp):
    current = open(tmp+filename, "r")
         
    destination = open(tiling + filename, "w")
           
    ttt = TextTilingTokenizer(w=35,k=5)
    i=i+1
    print(i ,"/",len(os.listdir(tmp)))
    print("  " + filename)
       #token = nltk.word_tokenize(t)
        
        #x=nltk.word_tokenize(t)
    tokens = ttt.tokenize(current.read())
        #text = nltk.Text(tokens)
        #print(tokens)
    for token in tokens:
        paragraph = token.replace("\n", " ")
        destination.write(paragraph)
        destination.write("\n\n") 
    current.close()
    destination.close() 
    
