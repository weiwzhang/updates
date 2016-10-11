# What I have done
1. config github with my username and email
2. setup the working environment
4. getting familiar with matplotlib
3. adding docstring to demo_floating_axes.py

# Question:
1. output of tests.py: FAILED (KNOWNFAIL=31, SKIP=1234, failures=903). Is this result reasonable? without making any modification
2. returning 2 variables seems to be unnecessary in demo_floating_axes.py's setup_axes* functions.

# Note:
Steps to set up the thorough developer working environment are flying here and there. Here is what I did. It works in my OS Sierra.

1. git clone https://github.com/matplotlib/matplotlib (this is the /matplotlib will be used later)

2. download MacPorts

3. In terminal: `sudo port install libpng freetype pkgconfig`

4. In terminal: `cd /matplotlib`, `python setup.py install` (now you can run `python tests.py` inside /matplotlib) 

5. conda install python.app (now you can run all *.py inside /example using `pythonw`) 
