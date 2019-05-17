#!/usr/bin/python

#L3 Internship

#authors : Nizar Rezaigui
#date : 16/05/2019
#Implementation of the TextTiling 

import sys
import os
import os.path
import shutil

class bcolors:
    FAIL = '\033[95m'
    ENDC = '\033[95m'

def TextTiling(directory):
    '''
        tokenize and return segment
    '''
    t = "{}/tmp/".format(directory)
    from nltk.tokenize import TextTilingTokenizer
    ttt = TextTilingTokenizer()
    for filename in os.listdir(t):
        tokens = ttt.tokenize(filename)
    #TODO
    
    
    
def nl2text(filename,source,destination):
    '''
        get a txt from parsing natural language to change into simple text (withouts time, speakers and context)
    '''
    lines = []
    for line in source:
		lines.append(line) 
        
    #TODO
    return 

    
def get_data_txt(directory):
    '''
        get data from result and change them for text-tiling
    '''
    tmp = "{}/tmp".format(directory)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    for filename in os.listdir(directory):
        if filename.endswith('.txt') :
            remote = "{0}/tmp/".format(directory)
            origin = "{0}/".format(directory)
            source =  open(origin+filename, "r")
            destination = open(remote+filename, "w")
            
            nl2text(filename,source, destination)
            source.close()
            destination.close()    

def get_data_ctm(directory):
    '''
        get data from result and change them for text-tiling
    '''
    tmp = "{}/tmp".format(directory)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    for filename in os.listdir(directory):
        if filename.endswith('.ctm_amis') :
            remote = "{0}/tmp/".format(directory)
            origin = "{0}/".format(directory)
            source =  open(origin+filename, "r")
            destination = open(remote+filename, "w")
            
            nl2text(filename,source, destination)
            source.close()
            destination.close() 

current = os.getcwd()
if len(sys.argv) == 1
    print("No argument provided !")
    directory = "results"
else:    
    directory = sys.argv[1]
if not os.path.exists(directory):
	print(bcolors.FAIL + "arg not found" + bcolors.ENDC)
    sys.exit(2)
else:
	get_data_txt(directory)
   

