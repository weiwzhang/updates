# Report for Yue Zheng

*This report combines 8 individual submissions.*

# Past week

- Set up environment, install dependencies, run tests.
- Set up Sublime Text to indent with 4 spaces
- Browse issues to get an idea of what issues look like

# Next week

- Familiar myself with Scipy and Matplotlib
- Start working on an issue

# Issues

- Some tests are failing:

    skimage.io.tests.test_mpl_imshow.test_uint8 ... ERROR
    skimage.io.tests.test_mpl_imshow.test_uint16 ... ERROR
    skimage.io.tests.test_mpl_imshow.test_float ... ERROR
    skimage.io.tests.test_mpl_imshow.test_low_dynamic_range ... ERROR
    skimage.io.tests.test_mpl_imshow.test_outside_standard_range ... ERROR
    skimage.io.tests.test_mpl_imshow.test_nonstandard_type ... ERROR
    skimage.io.tests.test_mpl_imshow.test_signed_image ... ERROR

    skimage.io.tests.test_plugin.test_load_preferred_plugins_all ... /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable
    ERROR
    skimage.io.tests.test_plugin.test_load_preferred_plugins_imread ... /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable
    ERROR
    /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable
    /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable
    /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable
    /Users/yuezheng/machine-shop/scikit-image/skimage/io/_plugins/matplotlib_plugin.py:4: ImportWarning: Not importing directory '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/mpl_toolkits': missing __init__.py
      from mpl_toolkits.axes_grid1 import make_axes_locatable

    skimage.restoration.tests.test_inpaint.test_inpaint_biharmonic_2d ... /Users/yuezheng/Library/Python/2.7/lib/python/site-packages/numpy/core/fromnumeric.py:2699: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
      VisibleDeprecationWarning)
    ERROR
    skimage.restoration.tests.test_inpaint.test_inpaint_biharmonic_3d ... ERROR

    Default package level setup routine for skimage tests. ... ok
    Default package level teardown routine for skimage tests. ... ok
    Failure: ValueError (invalid literal for int() with base 10: '0b1') ... ERROR

<hr/>

# Past week

- Investigated issue #2225, reproduced bug examples
- Worked on issue #2214. Already being addressed in PR #2220, so will not push changes

# Next week

- Work on issue #2225

<hr/>

# Past week

- Made PR #2354 addressing issue #2183
- Decided problem of issue #2225 is probably in _match_label_with_color

# Next week

- Look into issue #2053
- Continue looking into issue #2225 if have time.


<hr/>

# Past week

- Looked into issue #2053. Claudia made a PR so I won't be making one.
- Continued to investigate issue #2225. Figured out why we got the images in the two examples.

# Next week

- Work on fixing the bug of issue #2225
- Look for new issues to work on.

# Issues
- For issue #2225, non-negative labels are handled correctly, but nonconsecutive labels are not handled. Background color is always at index 0 of color cycle, but background label may not be smallest label, so the background color may not be displayed correctly.
- Not sure exactly how to fix bug yet, will work on it this week.

<hr/>

# Past week

- Worked on #2225, fixed issue and wrote some tests. Made PR.

# Next week

- Work on improving PR for #2225 if there are any comments on it
- Learn to do code reviewing
- Look for new issue to work on

<hr/>

#Past Week
- Researched meaning for beta parameters of frangi filter algorithm and made a PR for issue 2166.
- Looked at example of deprecation and made a PR for issue 2245.

##Next week
- Work on new issues

##Issues
- Some checks failed for the PR for issue 2245. Mostly test coverage decreased. Don't know if a test to check deprecation warning works is needed or not.


<hr/>

#Past Week
- Added tests for deprecation for issue 2245.
- Started working on issue 2189.

##Next week
- Finish working on issue 2189 and make a PR for it.

##Issues
- The continuous integration check failed for PR 2384 (addressing issue 2245), not sure why.
- Not sure what the default value for the proposed 'image_range' argument should be.


<hr/>

# Merged PRS
- https://github.com/scikit-image/scikit-image/pull/2354
- https://github.com/scikit-image/scikit-image/pull/2370
- https://github.com/scikit-image/scikit-image/pull/2382

# Code reviews
- https://github.com/scikit-image/scikit-image/pull/2351
