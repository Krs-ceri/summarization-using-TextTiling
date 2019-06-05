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
from nltk.corpus import stopwords
from nltk.tokenize import TextTilingTokenizer


class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OK = '\033[92m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    
    
    
def CountNbLine(filename):
    '''
        Count and return the numbers of sentence in one file            
    '''
    count = 0
    for line in filename:
        count += 1
    return count-2

def outputSystem(directory):
    '''
        output(txt) to comput and evaluate 
    '''
    t = "{}/tiling/".format(directory)
    res = "{}/output/".format(directory)
    if os.path.exists(res):
        shutil.rmtree(res)
    os.mkdir(res)
    print(bcolors.OKBLUE + "process text " +bcolors.ENDC ,len(os.listdir(t)))
    
    for filename in os.listdir(t):
        #open files with the same filename in others directory
        current = open(directory+"/tiling/"+filename, "r")
        output = open(res  +  filename, "w")
        
        lia = open(directory + "/" + filename, "r")
        maxi = CountNbLine(lia)
        
        count = -1
        lenght = []
        paragraph = []
        paragraph = current.read().split("\n\n") 
        #paragraph = paragraph[:len(paragraph)-1]
        
        for i in paragraph:
            #count the numbers of ' .' to operate the numbers of sentences
            lenght = i.split(" .")
                     
            if count == -1:
                #case of the first sentence
                count = count + len(lenght)
                output.write(str(count))
            else:
                if count + len(lenght) < maxi:
                    #others with result under maximum calculated with original file
                    count = count + len(lenght)
                    output.write("\n"+str(count))
        output.write("\n"+str(maxi))
        current.close()
        output.close()              
    print(bcolors.OKBLUE +  "processed output " + bcolors.ENDC,len(os.listdir(res)))
    print("done" )
    shutil.rmtree(t)    
    
    
def TextTiling(directory, word, sentence):
    '''
        tokenize and return text tiled txt separated by '\n\n'
    '''
    tmp = "{}/tmp/".format(directory)
    tiling = "{}/tiling/".format(directory)
    if os.path.exists(tiling):
        shutil.rmtree(tiling)
    os.mkdir(tiling)
    
    j = 0        
    print(bcolors.HEADER + "\n       Text-tiling\n"+ bcolors.ENDC)
    
    for filename in os.listdir(tmp):
        #open files with the same filename in others directory    
        current = open(tmp+filename, "r")
        destination = open(tiling + filename, "w")
        #function and parameters needed for texttiling    
        ttt = TextTilingTokenizer(w=int(word), k=int(sentence))
        j=j+1
        print("["+ str(j) + "/"+ str(len(os.listdir(tmp))) + "] :" + bcolors.WARNING + filename + bcolors.ENDC)
        
        #x=nltk.word_tokenize(t)
        tokens = ttt.tokenize(current.read())
        for token in tokens:
            #for token, write in file without '\n'
            paragraph = token.replace("\n", " ")
            destination.write(paragraph)
            destination.write("\n\n") 
        current.close()
        destination.close() 
    shutil.rmtree(tmp)
    
def nl2text(source,destination):
    '''
    get a txt from parsing natural language to change into simple text (withouts time, speakers and context)
    '''
    cpt = 0
    i = []
    for line in source:
        if cpt != 0:
            i = line.split("\t")
            myString = i[4]
            token = nltk.word_tokenize(myString)    
            myString = myString.replace(" ."," .\n\n")
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
    
    print(bcolors.OKBLUE + "process data " +bcolors.ENDC,len(os.listdir(directory)))
    for filename in os.listdir(directory):
        if filename.endswith('.txt') :
            #create in tmp a txt
            remote = "{0}/tmp/".format(directory)
            destination = open(remote+filename, "w")
            #open original
            origin = "{0}/".format(directory)
            source =  open(origin+filename, "r")
            #call for each files to transform
            nl2text(source, destination)
            #close files
            source.close()
            destination.close()
                
    print( bcolors.OKBLUE +  "processed text " + bcolors.ENDC,len(os.listdir(tmp)))
    return True


if len(sys.argv) == 1:
    print("No argument provided !")
    '''
    if no argument, default directory will be used
    '''
    directory = "srt/trs"
    word = 35
    sentence = 12
else:
    if len(sys.argv) == 2:    
        directory = sys.argv[1]
        word = 35
        sentence = 12
    elif len(sys.argv) == 4:
        directory = sys.argv[1]
        word = sys.argv[2]
        sentence = sys.argv[3]
        print(word+" "+sentence)
    else:
        print(bcolors.FAIL + "arg not found" + bcolors.ENDC)
        sys.exit(2)  
if not os.path.exists(directory):
    print(bcolors.FAIL + "arg not found" + bcolors.ENDC)
    sys.exit(2)
else:
    if(get_data(directory) == True):         
        TextTiling(directory, word, sentence)
        outputSystem(directory)
    else:
        print("Data not found !")   
   
