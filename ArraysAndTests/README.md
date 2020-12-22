#Project summary
- test driven development
- implementing class Arrays (like numpy) in python.
- writing tests using pytest
- code documentation
- code structuring
- debugging
- bash
   
Check out the *"assignment.pdf"* inside assignment folder for more details on the project.

#Environment requirement
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

#Dependencies
pytest 6.2.1
```
$ pip install -U pytest
```

#How to run scripts
tests:
```
$ pytest
```
What '**wc**' does is it prints a single line *'a b c fn'* where a is the number of lines in the file, b the number of 
words, c the number of characters, and fn the filename. It can also process a whole directory or all files with 
specific file extensions. 

wc script can be called in this way:
```
$ ./scripts/wc.py <file_name | * | *.extension>
```
or
```
python3 scripts/wc.py <file_name | * | *.extension>
```

To test how the implemented Array class work, try to experiment with it.
For instance, you can create 2-dimensional Array with 3 columns at each row like this:
```python
arr = Array((2,3), 1,2,3, 4,5,6 )
```
You can do elementwise operations on the array like adding two arrays, get nice formatted view of the array by printing
it and do many other operations. For more info refer to the pdf inside assignment directory.
Example:
```python
a = Array((2,3), 1,2,3, 4,5,6 )
b = Array((2,3), 1,2,3, 4,5,6 )
c = a + b
```
Result:
```
>>> print(c)
[[2, 4, 6], [8, 10, 12]]
```



