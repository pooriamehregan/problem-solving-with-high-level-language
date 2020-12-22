#Project summary
1. Make Html requests, then save (*in the folder named requesting_url*) and return the response as html data.
2. Using **Regular Expression** to filter out:
    - general hyperlinks
    - only wikipedia hyperlinks
      
   from html body.
3. Use regex to collect *dates* from HTML body, then put them in the following format: YYYY-MM-DD.
4. Use **BeautifulSoup**, **regex** and Browser (**Google Chrome** in developer mode) to navigate and extract data about
skiing tournament from html. Then use markdown to create a betting slip to send to your friends. 
5. Navigate through html pages and extract statistics about NBA teams and players. Then use that data to plot chart,
using **matplotlib**.
6. Peer-reviewing another students solutions to this assignment. You can see the peer-reviewing instruction inside 
the assignment folder, called *"Peer_Review.pdf"*.
   
Check out the *"assignment.pdf"* inside assignment folder for more details on the project.

#General info
There are 5 folders for each task, containing the results from last run. You could as well check them out before
you run your own commands.

I have used a logging library to show the user execution progress. Logging can be turned off using the following
`logging.disable(logging.INFO).`

##Environment Requirements:
Make sure you hav *python3* installed.

Then install virtual environment by executing these commands:
```
$ cd ~
$ pip3 install --user virtualenv
$ export PATH=$PATH:~/.local/bin
$ virtualenv -p python3 venv-web_programming
$ source venv-web_programming/bin/activate
```

##Dependencies:
BeautifulSoup
```bash
$ pip install beautifulsoup4
```

matplotlib
```bash
$ pip install matplotlib
```

requests
```bash
$ pip install requests
```

lxml
```
$ pip install lxml
```


##How to run the scripts:
You can run this script which in turn calls methods that run solutions for task 5.1, 5.2, and 5.3 :
```
python3 main.py
``` 

time_planner.py:
```
python3 time_planner.py
```

fetch_player_statistics.py:
```
python3 fetch_player_statistics.py
````

#Decision explanation
I could have included the code for executing *time planner* and *fetch player statistics* in `main.py` like I did for 
tasks *5.1, 5.2, 5.3* but since assignment text explicitly mentioned that they should be inside their own script, then
I followed the assignment text and called them from inside their own scripts. That's why you need only one command 
for executing the first three tasks, but each of the remaining tasks need to be called with their own specific command. 



    
