# Report for Jun Tan

*This report combines 7 individual submissions.*

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


<hr/>

### What I did:

1. Fix the bug causing `python tests.py` has failures.
2. Haven been doing Bug in AxesStack.add. Still in progress


<hr/>

Find the AxesStack remove issue and make the test for it in test_figure.py


<hr/>

1. Document the changes in the AxesStack

2. Add a helper function to verify the input is matrix


<hr/>

1. refactor :func:_parse_args in quiver.py



<hr/>

In the past week:

1. Debate about whether should change the stack.remove() in the AxesStack

2. Fixed the typo mentioned in this ticket: https://github.com/matplotlib/matplotlib/issues/7198

Coming up:

1. Make a clearer error message mentioned in this ticket: https://github.com/matplotlib/matplotlib/issues/7314

2. Get start with https://github.com/matplotlib/matplotlib/issues/7199


<hr/>

## Pull Request I made

https://github.com/matplotlib/matplotlib/pull/7461

https://github.com/matplotlib/matplotlib/pull/7335

https://github.com/matplotlib/matplotlib/pull/7249

https://github.com/matplotlib/matplotlib/pull/7384


