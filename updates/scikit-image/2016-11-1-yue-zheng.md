# Past week

- Looked into issue #2053. Claudia made a PR so I won't be making one.
- Continued to investigate issue #2225. Figured out why we got the images in the two examples.

# Next week

- Work on fixing the bug of issue #2225
- Look for new issues to work on.

# Issues
- For issue #2225, non-negative labels are handled correctly, but nonconsecutive labels are not handled. Background color is always at index 0 of color cycle, but background label may not be smallest label, so the background color may not be displayed correctly.
- Not sure exactly how to fix bug yet, will work on it this week.