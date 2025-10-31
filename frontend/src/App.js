

// import React, { useEffect, useState } from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar"; // Import Navbar
// import Footer from "./components/Footer"; // Import Footer
// import Home from "./pages/Home"; // Import Home Page
// import About from "./pages/About"; // Import About Page
// import ResourceAllocationForm from "./pages/resource-allocation"; // Import Resource Allocation Form
// import axios from "axios"; // ✅ Import axios for API calls
// import "bootstrap/dist/css/bootstrap.min.css";


// function App() {
//   const [backendStatus, setBackendStatus] = useState("");

//   // ✅ Test Backend Connection
//   useEffect(() => {
//     axios
//       .get("http://127.0.0.1:8000/api/test/") // Replace with a test API endpoint
//       .then((response) => {
//         setBackendStatus(response.data.message); // ✅ Display backend response
//       })
//       .catch((error) => {
//         console.error("Backend connection error:", error);
//         setBackendStatus("Error connecting to backend!");
//       });
//   }, []);

//   return (
//     <Router>
//       <Navbar /> {/* Navbar will always be visible */}
//       <Routes>
//         <Route path="/" element={<Home />} /> {/* Home Page */}
//         <Route path="/about" element={<About />} /> {/* About Page */}
//         <Route path="/resource-allocation" element={<ResourceAllocationForm />} /> {/* Resource Allocation Form */}
//       </Routes>
//       <Footer /> {/* Footer will always be visible */}

//       {/* ✅ Show Backend Connection Status */}
//       <div style={{ textAlign: "center", padding: "10px", color: "gray" }}>
//         <small>🔗 Backend Status: {backendStatus}</small>
//       </div>
//     </Router>
//   );
// }

// export default App;
//imp code 










































import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar"; // ✅ Navbar Component
import Footer from "./components/Footer"; // ✅ Footer Component
import Home from "./pages/Home"; // ✅ Home Page
import About from "./pages/About"; // ✅ About Page
import ResourceAllocationForm from "./pages/resource-allocation"; // ✅ Resource Allocation Page
import Analytics from "./pages/analytics"; // ✅ Added Analytics Page
import axios from "axios"; // ✅ For API Calls
import "bootstrap/dist/css/bootstrap.min.css"; // ✅ Bootstrap for Styling



function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");

  // ✅ Test Backend Connection on Load
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/test/") 
      .then((response) => {
        setBackendStatus(response.data.message); // ✅ Show backend response
      })
      .catch((error) => {
        console.error("Backend connection error:", error);
        setBackendStatus("❌ Error connecting to backend!");
      });
  }, []);

  return (
    <Router>
      {/* ✅ Navbar is Always Visible */}
      <Navbar />

      {/* ✅ Define All Routes */}
      <Routes>
        <Route path="/" element={<Home />} /> {/* Home Page */}
        <Route path="/about" element={<About />} /> {/* About Page */}
        <Route path="/resource-allocation" element={<ResourceAllocationForm />} /> {/* Resource Allocation */}
        <Route path="/analytics" element={<Analytics />} /> {/* ✅ Added Analytics Page */}
     
      </Routes>

      {/* ✅ Footer is Always Visible */}
      <Footer />

      {/* ✅ Display Backend Status */}
      <div style={{ textAlign: "center", padding: "10px", color: "#555", fontSize: "14px" }}>
        <small>🔗 Backend Status: {backendStatus}</small>
      </div>
    </Router>
  );
}

export default App;
