import "./App.css";
import React from "react";
import HeaderNavbar from "./components/Navbar/Navbar";
import logo from "./logo.svg";
import Router from "./components/router/router"

function App() {
  return (
    <div className="App">
      <HeaderNavbar />
      <header className="App-header">
        <Router/>
      </header>
    </div>
  );
}

export default App;
