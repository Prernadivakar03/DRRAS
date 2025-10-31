
import React, { useEffect } from "react";
import "./About.css"; 
import logo from "../assets/logo.png"; 
import floodImg from "../assets/flood.jpg";
import earthquakeImg from "../assets/earthquake.jpg";
import wildfireImg from "../assets/wildfire.jpg";
import cycloneImg from "../assets/cyclone.jpg";
import landslide from "../assets/landslide.jpg";
import drought from "../assets/drought.jpg";
const About = () => {
  useEffect(() => {
    const cards = document.querySelectorAll(".disaster-card");

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("show");
          }
        });
      },
      { threshold: 0.2 }
    );

    cards.forEach((card) => observer.observe(card));

    return () => {
      cards.forEach((card) => observer.unobserve(card));
    };
  }, []);

  return (
    <div className="about-container">
      {/* Text & Image Section */}
      <div className="about-content">
        <div className="about-text">
          <h2>About DRRAS</h2>
          <p>
            The Disaster Relief Resource Allocation System (DRRAS) is designed to efficiently allocate
            resources using data-driven algorithms in Maharashtra. Our goal is to optimize relief distribution and
            improve disaster preparedness. where users can input the disaster data ,system itself cluster them in high , low or moderate serverity 
            and then allocate the resources.
          </p>
        </div>
        <div className="about-image">
          <img src={logo} alt="DRRAS Logo" className="logo-img"/>
        </div>
      </div>

      {/* Flashcards Section */}
      <div className="flashcards-container">
        {flashcards.map((card, index) => (
          <div key={index} className="flashcard">
            <div className="flashcard-inner">
              <div className="flashcard-front">{card.front}</div>
              <div className="flashcard-back">{card.back}</div>
            </div>
          </div>
        ))}
      </div>

      {/* Divider */}
      <hr className="section-divider" />

      {/* Disaster Types Section */}
      <div className="disaster-section">
        <h2>Listed below are some recent Disasters that have occurred in maharashtra! </h2>
        <p style={{textAlign:"center"}}>A natural disaster is the highly harmful impact on a society or community following a natural hazard event. The term "disaster" itself is defined as follows: "Disasters are serious disruptions to the functioning of a community that exceed its capacity to cope using its own resources.
           Disasters can be caused by natural, man-made and technological hazards, as well as various factors that influence the exposure and vulnerability of a community.
           Here are some of the NATURAL DISASTERS....!!!!!</p>
        <div className="disaster-grid">
          {disasters.map((disaster, index) => (
            <div key={index} className="disaster-card">
              <img src={disaster.image} alt={disaster.name} className="disaster-img"/>
              <h3>{disaster.name}</h3>
              <p>{disaster.description}</p>
            </div>
          ))}
        </div>
      </div>
      <div>
        <p style={{ textAlign:"center"}}> As you can see, the above-mentioned disasters are the most recent ones in Maharashtra, highlighting the increasing frequency and severity of natural events. 
          This underscores the urgent need for effective disaster preparedness and resource management.</p>
      </div>
      <div>
  <div className="help-hover">
    Need Help?
  </div>
  <div className="help-popup">
    📞 **Emergency Contacts:**  
    🚑 Ambulance: 102 
    🚒 Fire Brigade: 101  
    🚓 Police: 100  or 112 
    🌊 Disaster Helpline: 108   
  </div>
</div>

    </div>
  );
};

// Flashcard Data
const flashcards = [
  { front: "📌 Optimized Resource Allocation", back: "Smart AI-driven disaster response system." },
  { front: "📊 Data-Driven Decisions", back: "Using analytics to predict & distribute relief." },
  { front: "⚡ Real-Time Disaster Response", back: "Live monitoring & allocation for emergencies." },
  { front: "💻 Technology Stack", back: "React.js ⚛️ | Django 🐍 | PostgreSQL 🗄️ | AI-powered predictions 🤖" },
];

// Disaster Data
const disasters = [
  { name: "Flood", image: floodImg, description: "Floods occur due to excessive rainfall, overflowing rivers, or storm surges. Recently, A series of floods took place across the Indian State of Maharashtra in 2021. As of 28 July 2021, around 251 people have died and over 100 are still missing due to floods and landslides. 13 districts have been affected in western Maharashtra.Damage was calculated to be Rs4,000 crore (US$539 million)." },
  { name: "Earthquake", image: earthquakeImg, description: "Sudden shaking of the ground caused by tectonic movements.There have been several earthquakes in Maharashtra in recent years, including a 3.7 magnitude earthquake in Palghar in January 2025 and a 4.5 magnitude earthquake in Hingoli in July 2024. " },
  { name: "Wildfire", image: wildfireImg, description: "Uncontrolled fires that spread rapidly, destroying forests and homes.PUNE: Maharashtra has registered 97 large forest fires since Jan this year, up from 33 during the corresponding period in 2024, the Forest Survey of India (FSI)'s latest satellite mapping-based data showed." },
  { name: "Cyclone", image: cycloneImg, description: "Intense storm systems with strong winds and heavy rainfall.Cyclone Nisarga hit Maharashtra in June 2020, causing severe damage. It was the most powerful tropical cyclone to hit Maharashtra since 1891. " },
  { name: "Droughts", image: drought, description: "A prolonged period of dry weather that results in a water shortage.Maharashtra has been experiencing a severe drought since 2023, affecting more than 66% of the state. The drought has led to a drastic drop in water levels in reservoirs and wells, and has caused water shortages for drinking and irrigation. " },
  { name: "Landslides", image: landslide, description: "A mass movement of material, such as rock, earth or debris, down a slope.On July 19, 2023, the entire Irshalwadi village in the Raigad district of Maharashtra, India, was obliterated due to a single catastrophic landslide." },
];

export default About;
