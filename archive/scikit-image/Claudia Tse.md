# Report for Claudia Tse

*This report combines 9 individual submissions.*

#Past Week
1) Cloned the scikit-image repository on github
2) Installed the project for local development
3) Ran the unit test suite

#Next Week

#Issues

<hr/>

##Past Week
- Worked on Issue #2214, #2214, #1961

##Next week
- Continue working on Issue #2225

##Issues
- Didn't understand what the expected output for negative labels should be.
- Had trouble locating the location of the bug for Issue #2214.
- There was already another pull request on Issue #2214

<hr/>

##Past Week
- Finished Issue #1961.
- Continued working on Issue #2225.

##Next week
- Will work on Issue #548 or #2053.
- Continue trying to locate the bug for Issue #2225.

##Issues
- Had trouble locating the location of the bug for Issue #2214.
- The RGB background produced by passing in negative labels to label2rgb seems 
  to remain blue even when bg_label and bc_color are 0 and (0, 0, 0) respectively.
- Had limited time to work on issues for scikit-image due to having 
  projects and midterm due this week.

<hr/>

##Past Week
- Finished Issue #2053.

##Next week
- Work with Yue Zheng on fixing the bug she located for Issue #2225.
- Work on a new Issue.

##Issues

<hr/>

#Past Week
- Looked through pull requests and issues and tried to understand them.
- Attempted to find the indentation error in PR #2366 that was causing the Travis CI check to fail.
- Attempted to understand the logic of the code in Issue #2367 and figure out whether the problem is caused by a bug.
- Attempted Issue #2346.

##Next week
- Continue working on Issue #2346 or another issue.
- Might look through other PRs or issues.

##Issues
- Had trouble understanding the code involved in the issues and pull requests I looked through due to limited knowledge in the math behind it.
- Unsure of how to solve Issue #2346 since many of the functions feature.structure_tensor uses requires or outputs 2D arrays or points.

<hr/>

# Past week
- Made the requested changes in my PR #2364.
- Lookd over PRs. Made comment in PR #2376. I think my comment was wrong though...
- I noticed that some checks from previous PRs I've made were failing and tried to understand why.
- Looked at Issue #2346.

# Next week
- Will continue looking through other PRs and Issues.
- Continue looking at Issue #2346.

# Issues
- Didn't understand why some checks in my previous PRs were failing.
- I'm pretty sure I know how to change feature.structure_tensor so that it will compute the tensor of a 3-D array, but I don't know how to make it compute the tenor of an array of any dimension.

<hr/>

#Past Week
- Worked on Issue #2346.

##Next week
- Continue working on Issue #2346.

##Issues
- Checks on previous PRs I've made are failing even though the tests pass. Don't know what the problems are or how to fix them though.


<hr/>

#Past Week
- Worked on Issue #2346.
- Made suggested changes in PR #2364.

##Next week
- Continue working on Issue #2346.
- Try to figure out why the checks in PR #2351 are failing.
- Perhaps make more thorough tests for feature.structure_tensor and feature.corner_harris.

##Issues
- The Travis CI check for my PR #2351 is failing due to an indention error. I can't find where the indention error is though.
- Two tests for Issue #2346 are failing: test_normal_mode and test_uniform_mode even though all other tests pass.

<hr/>

#Merged PRs
- https://github.com/scikit-image/scikit-image/pull/2364
- https://github.com/scikit-image/scikit-image/pull/2351 [in progres]

#Code Review
- https://github.com/scikit-image/scikit-image/pull/2376/files/e179496ed01c719de6b0fbde33e9d8f11af8674a
