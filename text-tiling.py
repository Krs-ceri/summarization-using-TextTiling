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
try: 
    import numpy
except ImportError:
    pass

class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OK = '\033[92m'

def TextTiling(directory):
    '''
        tokenize and return segment
    '''
    t = "{}/tmp/".format(directory)
    from nltk.tokenize import TextTilingTokenizer
    ttt = nltk.tokenize.TextTilingTokenizer(demo_mode=True)
    for filename in os.listdir(t):
        with open(directory+"/tmp/"+filename, "r") as f:
            s, ss, d, tokens = ttt.tokenize(f)
            print(tokens)
    #TODO
    
    
def nl2text(source,destination):
    '''
    get a txt from parsing natural language to change into simple text (withouts time, speakers and context)
    '''
    cpt = 0
    i = []
    for line in source:
        if cpt == 0:
            print(bcolors.OK + line + bcolors.ENDC)
        else:
            i = line.split("\t")
            myString = i[4]
            myString = myString.replace(" .","")
            myString = myString.replace(" ,","")
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
            newname = filename.replace('_start_segmented','_text-tiling')
            
            remote = "{0}/tmp/".format(directory)
            destination = open(remote+newname, "w")
            
            origin = "{0}/".format(directory)
            source =  open(origin+filename, "r")
            
            
            nl2text(source, destination)
            source.close()
            destination.close()    

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
    get_data(directory)
    TextTiling(directory)
   
