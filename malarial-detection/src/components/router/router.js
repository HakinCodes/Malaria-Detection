import React from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom";

const Router = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/about.js" component={
  About} />
      <Route path="/users.js " component={Users} />
      <Route path="/Homepage.js" component={
  Home} />
    </Switch>
  </BrowserRouter>
);

const Home = () => <h2>Home</h2>;

const About = () => <h2>About</h2>;

const Users = () => <h2>Users</h2>;

export default Router;
