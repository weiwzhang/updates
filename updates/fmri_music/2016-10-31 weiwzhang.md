# Past Week
- continue to work on debuging sphinx documentation
- finish implementing all documentation docstrings for music-feats/features files (see my Github https://github.com/weiwzhang/music-features/tree/master/music_feats/features for more info)
- testing sphinx documentaion via the cesium repo

# Next Week
- (after Tuesday)finish fixing Sphinx documentation bugs
- peer code review: look into Travis-CI team's code 
- continue reading music-features/tutorials to understand more about the methodology of this research

# Issues
- compiling error (syntax error on "utilities.py")
-  fixed thanks to Stefan! Apparently there's a syntax error on utilities.py in pretty midi package. Will stop using that package for now.
- docstrings aren't read in by APIDocWriter
-  attempts: have tried editing __init__.py (added __all__ array with all documentated function signatures), tried using setup.py, tried to use the cesium repo to generate documentation
-  result: still can't read in the docstrings (Pearl also tested similarly)
-  reflections: I do think that we've imported all functions and also added them at the top of init.py files in respective directories. So I'm genuinely confused about what else we might have missed..
