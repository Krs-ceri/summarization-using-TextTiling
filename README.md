# LIA github : https://github.com/Krs-ceri/summarization
#Summarization text-tiling
### ******* version 1.0.0 *******
Convert folder of txt, to output system tiled.
#### Authors:

-Nizar REZAIGUI -----> Krs-ceri

#### Prerequisites :
vous devez installez :
```console
nltk
```
#### Installing :
additional libraries for nltk :
````console
$ python3 nltk.download('punkt')
$ python3 nltk.download('stopwords')
````
nltk intaller :
````console
$ sudo apt-get install nltk
````

#### How to use :
to launch, just enter program and your directory to change : 
    ```console

    $ python3 texttiling.py Papers   \\txt to tiled txt

    $ python3 texttiling.py      \\ txt to tiled txt using default directory

    ```
By default, a directory "srt/trs" is launched when no argument provided
    
   
Treated files go in Directory/output.
program also create Directory/tiling and Directory/tmp in order to convert files and generate output.


