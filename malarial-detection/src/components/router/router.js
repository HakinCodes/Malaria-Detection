import React from "react";
import {
  BrowserRouter,
  Switch,
  Route,
  Link
} from "react-router-dom";

const Router = () => (
    <BrowserRouter>
      <Switch>
        <Route path="/about" component={About}/>
        <Route path="/users" component={Users}/>
        <Route path="/" component={Home}/>
      </Switch>
    </BrowserRouter>
);

const Home = () => (
  <h2>Home</h2>
);

const About = () => (
  <h2>About</h2>
);

const Users = () => (
  <h2>Users</h2>
);

export default Router;