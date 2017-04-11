## 02-27-2017
- **Past week:** setting up cesium_web locally. Learning JavaScript.
- **Got stuck on:** had trouble setting up psql correctly (NOTE: psql wasn't started automatically in the background. Fixed); 
              can't parse webpack.config.json's info corectly (NOTE: the extension list had emptry string entry --> delete it)
- **Coming week:** finish setting up cesium_web. Also start looking at past semester's pull requests.

## 02-27-2017
- **Past week:** Finished debugging cesium_web app on local computer. Learning React.
                Compiling list of bugs and fixes for deploying Cesium web locally.
- **Got stuck on:** can't pass some of the Travis-CI tests (NOTE: Travis using an older version of webpack); get timeout errors (NOTE: probably because machine too slow)
- **Coming week:** Learning React. Start implementing the walkthrough tutorial.

## 03-13-2017
- **Past week:** meet with walk-tour team to discuss design of the walkthrough tutorial. Learn React and experiment with demos.   
- **Got stuck on:** making multiple tours for each tab or making one tour? Set up separate beacons (doable)? 
- **Coming week:** implement a prototype walkthrough. Explore merging walkthrough into existing project structure.
- **NOTES:** tentative design ideas for the walkthrough:
    - separate tool for each tab (5 in total) / one tool for all tabs, click on a tab it activates the walkthrough
    - each tool = dialogue boxes activating one after another, automatically, beside the respective functioning section
    - each box has back, next, “x” buttons
    - “x” cancels the tour for this tab for good
    - if we goes into a new tab, cancel old tour
    - color: blue
    - 1st welcome page: a starting button (that activate all tours)
    - a drop down shot menu: that asks for consent to start the tutorial

## 03-20-2017
- **Past week:** making a prototype for walkthrough tutorial (with Michael's help, have pushed to github) [single continuous tour with all steps, enable clickthrough to different tabs, can skip can restart]
- **Got stuck on:** reset tour button doesn't start the whole tour from the beginning (only repeat the first step and then stop); decide on what kind of popup welcome window we want
- **Coming week:** Will do more after midterms. Would explore options to fix reset tour button. Also try to meet with Stefan and team to discuss how to merge tour into the existing project structure.
- **NOTES:** tentative design ideas for the walkthrough (revised):
    - single tour (separate beacons unnecessary)
    - each tool = dialogue boxes activating one after another, automatically, beside the respective functioning section
    - get rid of "x" button on boxes? (use skip instead)
    - can reset tour
    - color: blue
    - 1st welcome page: a dropdown menu asking for consent to start the tour?
 
## 04-03-2017
- **Past week:** Learn React. Keep improving walkthrough demo. Fork and merge code into Nathan's cesium web version
- **Got stuck on:** need to decide on styling for user permission box, connecting one tab to the other, etc.
- **Coming week:** Focus on implementing a user permission box that asks user's consent to start/disable the walkthrough tutorial. 

## 04-10-2017
- **Past week:** Learn React. Implemented a prototype for user permission box using React-Modal. 
- **Got stuck on:** how to disable beacon? what exactly to implement for "never again (for walkthorugh)" option? is the styling of Modal ok? 
- **Coming week:** Improve Modal's styling (esp. make it footer and overlay-less). Figure out disabling beacons. 

    
