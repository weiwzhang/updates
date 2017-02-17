# Report for Weiwei Zhang

*This report combines 10 individual submissions.*

# Past Week

# Next Week
-Self-study Sphinx documentation
-implement documentation for music-features/music/features (part)
    -collaborating with Pearl

# Issues
-confirm the documentation file structure, file names



<hr/>

# Past Week
implement Sphinx documentation for music-features/music/features codes

# Next Week
-Continue working on Sphinx documentation for music-feats module with Pearl
- learn to use APIDocWriter and numpy to write documentations
- Record functions with unclear descriptions

# Issues
-revise documentation file structure


<hr/>

# Past Week
learn and use numpy doc to autogenerate Sphinx documentations
- having some problem setting up numpy doc to work properly
- implemented docstrings in source files (music_feats/features)

# Next Week
-troublseshooting for numpydoc & sphinx

# Issues
- docstrings not read by numpydoc (tried to refer to cesium repo but cesium doesn't seem to work right locally either)
- missing packages; reporting syntactic errors on source files in music_feats


<hr/>

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


<hr/>

# Past Week
- finished debugging API doc writer and successsfully generated all sphinx documentation for files in music_feats/feaures, utils folders.(see my Github https://github.com/weiwzhang/music-features/tree/master/ for more info)

# Next Week
- start working on Travis-CI testing files
- peer code review: look into Travis-CI team's code 
- continue reading music-features/tutorials to understand more about the methodology of this research

# Issues
- IMPORTANT NOTE: midi package is having syntax errors, so it's commented out and abstained from usage for now (features/pitchextractor.py)
- local configuration problem: my Mac is missing certain Mac library that's stopping me from installing cortex (for now have commented out import cortex in files: utils/model_func.py, resposne_utils_fi.py). 
- need to double check for documentation clarity? any improvement needed? 


<hr/>

# Past Week
- upgrade pretty_midi to fix incompatibility problem 
- fix minor errors in sphinx docstrings 

# Next Week
- keep working on minor Sphinx documentation bugs
- add sphinx doc build to Travis CI

# Issues
- need to determine py version
- have local issue with installing cortex package
- have no music files for test file


<hr/>

# Past Week
- manually upgrade pretty_midi 
- add missing sphinx docstrings for one file 
- fix spacing issues in docstrings for several files in features folder
- fix import statement in features/features.py for sphinx doc format
- experiment with Travis CI

# Next Week
- make LICENSE file for music-features repo
- add sphinx doc build to Travis CI
- survey doc tools
- prepare for end-of-semester team presentation

# Issues
- how to set up script commands in .travis.yml for sphinx?
- how does testing work?


<hr/>

# Past Week
- have committed a license file (MIT License format, follow cesium repo)
- have modified .travis.yml and requirements.txt for travis CI testing for sphinx doc build files
- compile brief list of other documentation tools
- have prepared short presentation on sphinx documentation

# Next Week
- keep working on sphinx documentation bugs
- keep working on fixing Travis CI errors

# Issues
- get more specific criteria on recording doc tools
- current Travis CI problems:
    - nibabel missing (utils/generateTestPrep.py)
    - tables missing (utils/response_utils_fi.py)
- features/pitchextractor.py documentation not generated??


<hr/>

#Past
- Implement travis-CI
 - Add nosetests with coverage module
 - Add tests for feature extractors
 - Remove tests where we test our results against another library's results using large music files.
 - Create test signals - ones, sinusoid, sawtooth, and strictly alternating.
 - Add tests for RMS, ZCR, and spectral centroid based on these test signals. Test both framewise and single-window.
- Clean up extractor and utils files
 - Clean up documentation for RMS, ZCR, and spectral centroid.
 - Change pad/padAmt variable to pad consistently.
 - Add assertions for y, win_length, hop_length, and pad.
 - Change framewise to not use librosa functions, use list comprehension, and dynamically pad both sides by reflection.
 - Add spectrogram utility to utils.py, now using np.fft.rfft and creating a threshold at 1% of the maximum frequency's amiplitude.
#Future
- Continue writing tests
 - Spectral spread, spectral flatness, fluctuation entropy, fluctuation centroid, key clarity, and pulse clarity are the next features to review the algorithms and rewrite the tests for.


<hr/>

# Work Summary
- task: build autogenerated documentation for the whole project using Sphinx and numpydoc
    - worked with Pearl to built documentations for all files in music-feats/features, utils folders
    - learn new tools (sphinx, numpydoc, Travis-CI)
    - set up testing for documentations (in progress)
- logistics: 
    - have participated in discussions on slack and github
    - have attended all meetings (except one week because of school exams)

# PR (not merged yet due to Travis-CI testing errors)
- https://github.com/machine-shop/music-features/pull/23 
- https://github.com/machine-shop/music-features/pull/18

# Code Review
- have worked with Pearl to modify conf.py and init files for documentation 

