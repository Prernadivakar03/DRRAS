import React from "react";
import "../pages/Home.css"; // Ensure the path is correct
import disasterImage from "../assets/diaster.png"; // Ensure the path is correct
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      {/* Image Section */}
      <div className="image-wrapper">
        <img src={disasterImage} alt="Disaster" className="home-image" />
      </div>

      {/* Quote Section */}
      <div className="quote-container">
        <p className="quote">
          "We cannot stop natural disasters, but we can arm ourselves with knowledge: 
          so many lives wouldn't have to be lost if there was enough disaster preparedness."
        </p>
         
      <button className="cta-button" onClick={() => navigate("/resource-allocation")}>
        Get Started
      </button>
      </div>
    </div>
  );
}

export default Home;
