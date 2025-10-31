
import React from "react";
import { Link } from "react-router-dom";
import { ReactTyped } from "react-typed"; // Ensure ReactTyped is installed
import "./Navbar.css"; // Import CSS file
import logo from "../assets/logo.png";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark fixed-top">
      <div className="container-fluid">
        {/* Logo & Brand */}
        <Link className="navbar-brand d-flex align-items-center" to="/">
          <img src={logo} alt="DRRAS Logo" width="50" height="50" className="me-2" />
          <span className="fw-bold fs-4">DRRAS</span>
        </Link>

        {/* Animated Text */}
        <div className="navbar-text ms-3 typing-text">
          <ReactTyped
            strings={["Welcome to Disaster Relief Resource Allocation System"]}
            typeSpeed={50}
            backSpeed={30}
            loop
            className="typing-text"
            style={{ color: "white" }} // Ensures white color
          />
        </div>

        {/* Mobile Toggle Button */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Navbar Links */}
        <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/about">About</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/resource-allocation">Resource Allocation</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/analytics">Analytics</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
