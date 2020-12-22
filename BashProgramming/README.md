#Project summary
move:
- A bash function "*move*", which moves all the files in a directory to another user defined directory.
- Optionally choose between moving all files in a directory or only files of one type for example move 
  only *.txt-files, *.dat-files.
- If the directory or LOGFILE does not exist, it gets created automatically.
- Creating a directory in the new destination that has the name of the current date and time in the 
  format YYYY-MM-DD-hh-mm.
  
track.sh:
- A bash program "*track*" tracking the time spent on various tasks
- The time tracking data will be stored in a file whose name is specified by a permanent environment variable 
  called LOGFILE.
- A log command, that displays the time spent on each task in the format HH:MM:SS

For detailed info about these tasks, see the pdf file named "*assignment*".

#General info
The *LOGFILE* that you see in this folder is just a copy from the original LOGFILE which I created in ∼/.local/share/.

I created the "*move*" like an executable command file, and "track.sh" like a script (that contains 3 functions) to 
demonstrate I was capable of doing both. 

First function in track.sh is called *track* and can be called from command line since I export it to .bashrc, and 
second function is just a helper function to *log* function and log() is the function that does the logging. In this
function I took care of a special case where a task is not finished yet, in that case start time and label for
that task is shown to user as the logging time.


###move
First source move.sh:
```bash
$ source move.sh 
```
Takes two commandline arguments: 
- the source, where the files you want to move are located, called src, 
- and the destination, where the files should be moved to, called dst.
```bash
$ move src dst [*.extension] 
```
Hint: dst variable should have the full path to the destination directory:
```bash
$ move ~/Desktop/source/ ~/Desktop/destination "*.txt"
```

###track.sh
- Step one:
change the <username> at line 2 in track.sh to be able to test track.sh on the pc you're on.
- step two: source track.sh
```bash
$ source track
```
then you can start, stop, and see the status of a task in the following way:
```bash
$ track start [label]
$ track stop
$ track status
```
