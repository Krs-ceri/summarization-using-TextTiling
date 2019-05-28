#!/usr/bin/python

#authors : Nizar Rezaigui
#date : 16/05/2019
#Implementation of the TextTiling Algorithm

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

class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OK = '\033[92m'


def outputSystem(directory):
    print("hello")
    t = "{}/tiling/".format(directory)
    res = "{}/output/".format(directory)
    if os.path.exists(res):
        shutil.rmtree(res)
    os.mkdir(res)
    for filename in os.listdir(t):
        #newname = filename.replace('_start_segmented','_text-tiling')

        current = open(directory+"/tiling/"+filename, "r")
        #lia = open(directory +"/"+ filename, "r" )
        output = open(res  +  filename, "w")
        
        lec = current.read()
        count = 0
        
        lenght = []
        paragraph = []
        paragraph = lec.split("\n\n") 
        for i in paragraph:
            #print(i)
            lenght = i.split(" . ")
            if count == 0:
                count = count + len(lenght)
                output.write(str(count-1))
            else:
                count = count + len(lenght)
                output.write("\n"+str(count-1))
        ciunt=count-1
        current.close()
        #lia.close()
        output.close()              
    print("done")
        
def TextTiling(directory):
    '''
        tokenize and return text tiled txt
    '''
    tmp = "{}/tmp/".format(directory)
    
    tiling = "{}/tiling/".format(directory)
    if os.path.exists(tiling):
        shutil.rmtree(tiling)
    os.mkdir(tiling)
    i = 0    
    for filename in os.listdir(tmp):
        current = open(tmp+filename, "r")
         
        destination = open(tiling + filename, "w")
           
        ttt = TextTilingTokenizer(w=40,k=15)
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
    
def nl2text(source,destination):
    '''
    get a txt from parsing natural language to change into simple text (withouts time, speakers and context)
    '''
    cpt = 0
    i = []
    for line in source:
        if cpt == 0:
            print("[INFO]: " + bcolors.OK + line.replace("-1\t# ","") + bcolors.ENDC)
        else:
            i = line.split("\t")
            myString = i[4]
            token = nltk.word_tokenize(myString)
            '''
            if(len(token) < 20 ):
                myString = myString.replace("\n"," ")
            else:'''    
            myString = myString.replace(" ."," .\n\n")
            #myString = myString.replace(",","")
            destination.write(myString)    
        cpt = cpt + 1
    return True


def get_data(directory):
    '''
    get data from result and change them for text-tiling
    '''
    tmp = "{}/tmp".format(directory)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    for filename in os.listdir(directory):
        if filename.endswith('.txt') :
            #newname = filename.replace('_start_segmented','_text-tiling')
            
            remote = "{0}/tmp/".format(directory)
            destination = open(remote+filename, "w")
            
            origin = "{0}/".format(directory)
            source =  open(origin+filename, "r")
            
            
            nl2text(source, destination)
            source.close()
            destination.close()    
    return True
current = os.getcwd()
if len(sys.argv) == 1:
    print("No argument provided !")
    directory = "srt/trs"
else:    
    directory = sys.argv[1]
if not os.path.exists(directory):
    print(bcolors.FAIL + "arg not found" + bcolors.ENDC)
    sys.exit(2)
else:
    if(get_data(directory) == True):
        print(bcolors.FAIL + "\n       Text-tiling\n"+ bcolors.ENDC)         
        TextTiling(directory)
        outputSystem(directory)
   
   
