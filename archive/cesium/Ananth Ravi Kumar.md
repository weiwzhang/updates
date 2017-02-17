# Report for Ananth Ravi Kumar

*This report combines 9 individual submissions.*

Past week:
> Attempted to set up prerequisite packages.

Next week:
> Start fixing bugs/closing pull requests.

Issues:
> Discovered a number of issues in using PostgreSQL with Ubuntu on
Windows. Turns out that it's not natively supported, and using it
requires downloading PostgreSQL for windows and then remotely
connecting to your own machine from within the Ubuntu subsystem.

<hr/>

Past Week:
    > No progress made due to interviews and midterms.

Next week:
    > set up Cesium Web on Ubuntu for Windows
    > Improve test coverage of cesium as per issue #93

Issues:
    > None

<hr/>

Past Week:
    > Submitted pull request to integrate coverage with travis.ci
    > added in tests to boost coverage of test_cadence_features and test_transform

Next week:
    > Continue improving test coverage, bump up at least one file to 100% coverage.
    > Read through the Cesium code in depth, figure out how the math behind it works.
    > Work with Alejandro to work on issue #138 (Model selection changes in sklearn)

Issues:
    > Code coverage can be misleading; some of the util files in particular have only ~70% coverage, but do not
    actually need more tests, since the methods not explicitly tested are often used in other test cases, which leads to coverage actually underestimating how much is being tested.

<hr/>

Past Week:
    > added in more tests to test_cadence_features and test_transform. Cadence features is now at 92% coverage, and transform is at 83%.

Next Week:
    > Talk to Stefan about further tasks to be done for Cesium.
    > Read through and understand codebase, pitch possible areas that could be expanded or improved upon. 

Challenges:
    > Code base is already very-well covered by tests, and for the most part, untested lines seem to be declarations or constructors. Rather unclear on how to progress.


<hr/>

Past week:
    - No significant progress made due to Midterms and job interviews. Recruitment season and midterm season are both over now, so this shouldn't impact progress anymore moving forward.

Next week: 
    - Finishing up addressing comments on currently open pull requests (should be done in the next hour or so). 

    - Additionally, I wanted to start working on issue #154 (Distance-based classification methods), but was wondering if this was a priority. 

Challenges:
    - None.

<hr/>

Past Week:
    - Read and understood background behind dynamic time warping.
    - Read through the FastDTW implementation and paper, also read through the R dtw repo's companion paper and repository.

Next Week:
    - Discuss FastDTW and R repository's functionality with Stefan, and see where to go from there.

Challenges:
    -  Having trouble with the codecoverage pull request; coverage docs aren't very clear, and I'm not sure if coverage needs to be pip installed inside the travis_script.sh bash script. Overall, not sure how travis, nosetests and coverage all fit together.

<hr/>

Past week:
    - Prototyped DAG-based partial as per this paper: http://knight.cis.temple.edu/~vasilis/Courses/CIS664/Papers/PKDD05.pdf

Current Week:
    - Find a time series to test cesium time-series clustering on.
    - Finish up implementation of DAG-based partial matching by:
        - writing test cases.
        - reading literature and seeing if there are any other partial matching methods
        that don't require computation of the entire cost matrix.

Challenges:
    - Nothing insurmountable.

<hr/>

Past Week:
    - almost finished implementation of DTW - DAG method 
    - finished implementing test cases for 4/6 methods.

Next week:
    - finish up DTW-DAG implementation.
    - time series clustering with Cesium
    - think of ways to make the DTW alg faster.

Challenges:
    - Having difficulty figuring out a way to systematically label nodes in networkx formulation. Using the value of a cell as the name of a node is not doable since networkx doesn't allow for multiple nodes with the same label.

<hr/>

Work left to do:
    1) Finish the DTW implementation
    2) Add in the code coverage functionality, in particular the PR comment feature.
    3) Keep contributing to cesium! I'll add in both of the aforementioned after finals.

Links to pull requests:
    1) Improving test coverage: https://github.com/cesium-ml/cesium/pull/215
    2) Integrating coverage with Travis: https://github.com/cesium-ml/cesium/pull/211
    3) Updating the readme: https://github.com/cesium-ml/cesium/pull/207
    4) Updating model_selection: https://github.com/cesium-ml/cesium/pull/212
    5) [Work in Progress] DTW implementation: https://github.com/cesium-ml/cesium/pull/233

All in all I spent about 8-9 hours a week on average working on Cesium-related activities. Most of that time was spent reading documentation (for Travis CI, codecov and DTW implementations) and the existing code-base (for the readme), and the second largest chunk of time was spent writing actual code. The third significant chunk of time was spent reading through papers on Time series analysis and on dynamic time warping as a whole, to try to reconcile speed with cost in the DTW implementation. 
