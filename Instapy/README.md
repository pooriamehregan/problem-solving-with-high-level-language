# Project summary
This project consist of many subtasks. What it basically does is to take an image and apply filters to it. For doing 
these tasks, the program uses different strategies like using pure python, numpy and numba to do the same tasks.Then it 
times each strategy and produces report files and writes timing and comparison to other strategies into the file.

Skills that was demonstrated in this project:
- code documentation
- code structuring 
- command line documentation
- python packaging
- installing/uninstalling packages
- working in virtual environment
- logging and debugging
- writing tests using *pytest*
- writing markdown README, like this file
- working with 3rd party scientific libraries like:
    - numpy
    - opencv
    - numba
- Peer-reviewing another students solutions to this assignment. You can see the peer-reviewing instruction inside 
the assignment folder, called *"Peer_Review.pdf"*.
   
Check out the *"assignment.pdf"* inside assignment folder for more details on the project.


# General info
.txt files inside numba_files, numpy_files and python_files (located inside instapy/bin) contain results from last test
run. To produce new results, simply run main.py from commandline. Then, a pop up will show up asking you to choose a 
file. 

This README should be enough to understand what this package does and how to use it, but if you need additional help
run the following command at the command line: 
```
$ instapy -h
```

# Environment requirements
only python versions *>=3.6,<3.9* are supported.
I would recommend setting up virtual environment like *venv* and install the package there.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a 
script with the directory path:
```
$ python3 -m venv tutorial-env
```
Once you’ve created a virtual environment, you may activate it.
```
$ source tutorial-env/bin/activate
```

# Packaging
### Creating the instapy package (*just for showing course instructor how I did it*)
You can skip installing wheel, if you already have it installed:
```
pip install wheel
python3 setup.py sdist bdist_wheel
```
### Installing the instapy package:
From inside instapy directory:
```
python3 setup.py install
```
From outside instapy folder: 
```
pip install -e <path_to_instapy>
```

# Dependencies
You can skip this part, this is just for info for better understanding the package dependencies. These dependencies 
will automatically be installed by installing instapy package (look further down).

Dependencies:
- Numpy
- Numba
- Open CV
- Pytest

# Execution instruction
### Simple run (*with user-interface*)
For a simple run, which also produces report files, and produces gray-scale and sepia filtered version of your chosen 
image, use below command (*filtered image will be saved into the assignment folder*):
```
$ instapy
```
### Advanced run
*Note: if output name is not given (with -o | --out), the image file will be saved to the current directory.*

Run with more options:
- grayscale filter:
```
 $ instapy -f <image_file_path> [-g|--gray] [(-i|--implement) <python|numba|numpy>] [(-o|--out) <output_file>]]
```
- sepia filter:
```
 $ instapy -f <image_file_path> [-se|--sepia] [(-st|--step) <filter strength>] [(-i|--implement) <python|numba|numpy>] [(-o|--out) <output_file>]]
```
- rescale image:
```
 $ instapy -f <image_file_path> [(-sc|--scale) <x> <y> (-o|--out) <output_file>]
```

Examples (*Note that second line creates the image in instapy folder, not in the same directory as chosen image*):
```
 $ instapy -f assignment/rain.jpg --gray
 $ instapy -f assignment/rain.jpg --sepia -i python -st 0 -o rain.jpg
 $ instapy -f assignment/rain.jpg -sc 0.5 0.5 -o assignment/rescaled.jpg
```
Running tests (with pytest):
```bash
pytest tests/test_instapy.py
```


