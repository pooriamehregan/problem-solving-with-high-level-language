# Project Summary
Creating a web visualization about how **Covid-19** cases for different counties have been. This is achieved by:  
1. Extracting data about covid-19 from CSV files, downloaded from Folkehelseinstituttet (FHI).
2. Creating a web server using Python, Flask, HTML and JavaScript.
3. Visualizing the given data on the web page as charts, by using Pandas and Altair in addition to those mentioned above. 
4. Adding script documentation (*Sphinx*) on the web page.
5. Peer-reviewing another students solutions to this assignment. You can see the peer-reviewing instruction inside 
the assignment folder, called *"Peer_Review.pdf"*.
   
Check out the *"assignment.pdf"* inside assignment folder for more details on the project.


# General info
The (server) page looks very simple, only satisfying required functionalities.


## Environment Requirements before running the scripts:
Recommended python version = 3.9 .
I would also recommend setting up virtual environment like *venv*.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a 
script with the directory path:
```
$ python3 -m venv tutorial-env
```
Once you’ve created a virtual environment, you may activate it.
```
$ source tutorial-env/bin/activate
```

## Dependencies:
Install dependencies listed below, if you haven't already do it:

Sphinx
``` bash
$ pip install sphinx
```
Altair
```bash
$ pip install altair
```
Altair Viewer
```
$ pip install altair_viewer
```  
Flask
```
$ pip install flask
```

## How to run scripts
#### Web Server
you can easily call:
```
$ python3 web_server.py
```

#### Web Visualization (*Optional*):
Since methods return altair charts, you have to use a tool like *altair viewer* to show them. That is why it is easier 
to call these methods with the given instructions below rather than the traditional way (which is $ pythons3 script.py). 

- both_ploth(): 
```bash
$ python3 -c 'from  web_visualization import *; plot_both().show()'
```
- plot_cumulative_cases():
```bash
$ python3 -c 'from  web_visualization import *; plot_cumulative_cases().show()'
```    
- plot_reported_cases():
```
$ python3 -c 'from  web_visualization import *; plot_reported_cases().show()'
```

## 6.1 (referring to assignment pdf)
plot_reported_cases and plot_cumulative_cases functions can be called with three optional arguments:
- county: default is set to all counties, but other choices are:
    - agder
    - all_counties
    - innlandet
    - more_og_romsdal
    - nordland
    - oslo
    - rogaland
    - troms_og_finnmark
    - trondelag
    - vestfold_og_telemark
    - vestland
    - viken
    
- time_start: default is 2020-01-01 (year/month/day)
- time_end: default is 2020-11-10

## 6.2 (referring to assignment pdf)
plot_both() takes one more argument than methods above, namely "*aggr*". *aggr* determines how the two graphs should be 
concatenated.
Default argument for aggr is '**layer**', but can also be:
   - **h**: for horizontal aligning
   - **v**: for vertical aligning
   
 
