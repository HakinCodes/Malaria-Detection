import React from "react";
import {
  BrowserRouter,
  Switch,
  Route
} from "react-router-dom";
import Homepage from '../pages/Homepage';

const Router = () => (
    <BrowserRouter>
      <Switch>
        <Route path="/about" component={About}/>
        <Route path="/demo" component={Demo}/>
        <Route path="/" component={Homepage}/>
      </Switch>
    </BrowserRouter>
);

const About = () => (
  <h2>About Page</h2>
);

const Demo = () => (
  <h2>Demo Page</h2>
);

export default Router;