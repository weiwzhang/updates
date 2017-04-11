# Nathan Pham weekly updates

## 02-24-2017

- **Past week:** Met the team, got the web app up and running both locally and with Docker, read the codebase and study React. 
- **Got stuck on:** Got trouble while setting up the app locally because of missing dependencies, wrong Python version and forgot to kill running server.
- **Coming week:** Learn more about React to help Michael and Wei with troubleshooting the click-through tutorial ticket. 

## 03-03-2017

- **Past week:** Investigate on React [JoyRide](https://github.com/gilbarbara/react-joyride), a better tool to create walkthroughs and guided tours for ReactJS apps. Brainstorming and design session with Michael and Wei about the walkthrough in details. Run a [Joyride's demo](https://github.com/gilbarbara/react-joyride/tree/master/demo) locally and noting on how it functions.
- **Got stuck on:** How to design a React component using JoyRide and how to render this new component into our existing app.
- **Coming week:** Attempt to design a simple JoyRide component. 

## 03-10-2017

- **Past week:** Built a [walkthrough prototype] (https://github.com/trpham/react-walk-prototype) with React Joyride and React tabs.
- **Got stuck on:** The walk dismissed after switching tabs. 
- **Coming week:** Fix switching tab problem and improve the prototype.

## 03-31-2017

- **Past week:** Making progress on integrate Walkthough component into Cesium app: including adding a ‘start a tour’ button, declare props and callback functions. The app run sucessfully and be able jump to to different 'visible' elements (steps) in the main page. https://github.com/trpham/cesium_web/blob/master/public/scripts/main.jsx
- **Got stuck on:** The tabs only get opened after uploading some feed data, need to figure out how to mimic uploading data. 
- **Coming week:** Improve transition from tabs to tabs, pack the walkthorugh code into a seperate component instead of putting it all in the main.js

## 04-07-2017

- **Past week:** Because the web interface requires clicking event to expand differnt tabs, I try to simulate the action by manually trigger click event on DOM elements within Walkthorugh callback function: https://github.com/trpham/cesium_web/blob/master/public/scripts/main.jsx
- **Got stuck on:** Try different approaches but was unsucessful on how to call jQuery .click() event inside walkthrough callback function.
- **Coming week:** Continue on fixing the click event to work. 
