# Author github : https://github.com/Krs-ceri/summarization
#Summarization text-tiling
### ******* version 1.0.0 *******
Convert folder of txt, to output system using text tiling.
#### Authors:

-Nizar REZAIGUI -----> Krs-ceri

#### Prerequisites :
```console
sudo pip3 install -U nltk
```
#### Installing :
additional libraries for nltk :
```console
$ python3
>>>import nltk
>>>nltk.download('punkt')
>>>nltk.download('stopwords')
```

#### How to use :
to launch, just enter program and your directory to change : 
```console
$ python3 texttiling.py   
$ python3 texttiling.py Papers
$ python3 texttiling.py Papers 35 12     
```
By default, a directory "srt/trs" is launched when no argument provided with 35 for words in sentence and 12 average sentences in blocks
Need 
Treated files go in Directory/output.
program also create Directory/tiling and Directory/tmp in order to convert files and generate output.


