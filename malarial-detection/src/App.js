import "./App.css";

import React from "react";

import HeaderNavbar from "./components/Navbar/Navbar";

import logo from "./logo.svg";

function App() {
  return (
    <div className="App">
      <HeaderNavbar />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          {" "}
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
