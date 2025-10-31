import React from "react";
import {  FaTwitter, FaLinkedin, FaGithub } from "react-icons/fa";
import "./Footer.css"; // ✅ Since Footer.css is in components

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        
        {/* Left Section - About */}
        <div className="footer-section">
          <h3>About Us</h3>
          <p>We strive to optimize disaster relief resource allocation using data-driven solutions.</p>
        </div>

        {/* Middle Section - Contact Info */}
        <div className="footer-section">
          <h3>Contact Us</h3>
          <p> prernadivakar0328@gmail.com</p>
          <p>Mumbai | India</p>
        </div>

        {/* Right Section - Social Media */}
        <div className="footer-section">
          <h3>Follow Us</h3>
          <div className="social-icons">
            <FaGithub />
            <FaTwitter />
            <FaLinkedin />
          </div>
        </div>

      </div>

      {/* Bottom Section */}
      <div className="footer-bottom">
        <p>© 2025 DRRAS. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
