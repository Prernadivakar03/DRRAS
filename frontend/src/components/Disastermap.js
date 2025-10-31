// import React, { useEffect, useState } from "react";
// import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
// import L from "leaflet";

// const DisasterMap = () => {
//     const [disasterData, setDisasterData] = useState([]);

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/disasters/")
//             .then(res => res.json())
//             .then(data => setDisasterData(data))
//             .catch(err => console.error("Error fetching disasters:", err));
//     }, []);

//     // Custom marker icon
//     const disasterIcon = new L.Icon({
//         iconUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
//         iconSize: [25, 41],
//         iconAnchor: [12, 41],
//         popupAnchor: [1, -34]
//     });

//     return (
//         <div className="h-96 w-full border rounded-lg shadow-lg overflow-hidden">
//             <MapContainer center={[19.7515, 75.7139]} zoom={6} className="h-full w-full">
//                 <TileLayer
//                     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//                     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//                 />
//                 {disasterData.map((disaster, index) => (
//                     <Marker 
//                         key={index} 
//                         position={[disaster.latitude, disaster.longitude]} 
//                         icon={disasterIcon}
//                     >
//                         <Popup>
//                             <strong>{disaster.disaster_type}</strong><br />
//                             Location: {disaster.location}<br />
//                             People Affected: {disaster.people_affected}
//                         </Popup>
//                     </Marker>
//                 ))}
//             </MapContainer>
//         </div>
//     );
// };

// export default DisasterMap;








// import React, { useEffect, useState, useRef } from "react";
// import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
// import L from "leaflet";

// // Custom marker icon
// const customIcon = new L.Icon({
//     iconUrl: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
//     iconSize: [32, 32],
//     iconAnchor: [16, 32],
//     popupAnchor: [0, -32],
// });

// const DisasterMap = () => {
//     const [disasters, setDisasters] = useState([]);
//     const [locationCoords, setLocationCoords] = useState({});
//     const locationCoordsRef = useRef({}); // ✅ Prevents unnecessary re-fetching

//     // Fetch disasters from API
//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/disasters/")
//             .then((res) => res.json())
//             .then((data) => setDisasters(data))
//             .catch((err) => console.error("Error fetching disaster data:", err));
//     }, []);

//     // Fetch coordinates for disaster locations
//     useEffect(() => {
//         const fetchCoordinates = async (location) => {
//             try {
//                 const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${location}, Maharashtra`);
//                 const data = await response.json();
//                 if (data.length > 0) {
//                     return { lat: parseFloat(data[0].lat), lon: parseFloat(data[0].lon) };
//                 }
//             } catch (error) {
//                 console.error("Error fetching coordinates for", location, error);
//             }
//             return null;
//         };

//         const getAllCoordinates = async () => {
//             const newCoords = {};
//             for (const disaster of disasters) {
//                 if (disaster.location && !locationCoordsRef.current[disaster.location]) {
//                     const coords = await fetchCoordinates(disaster.location);
//                     if (coords) {
//                         newCoords[disaster.location] = coords;
//                     }
//                 }
//             }
//             if (Object.keys(newCoords).length > 0) {
//                 setLocationCoords((prev) => {
//                     const updatedCoords = { ...prev, ...newCoords };
//                     locationCoordsRef.current = updatedCoords; // ✅ Updates ref
//                     return updatedCoords;
//                 });
//             }
//         };

//         if (disasters.length > 0) {
//             getAllCoordinates();
//         }
//     }, [disasters]); // ✅ Now correctly tracks `disasters` changes without warnings

//     return (
//         <div className="h-96 w-full">
//             <MapContainer center={[19.7515, 75.7139]} zoom={6} className="h-full w-full">
//                 <TileLayer
//                     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//                     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//                 />

//                 {/* Add markers for disasters */}
//                 {disasters.map((disaster) => {
//                     const coords = locationCoords[disaster.location];
//                     if (!coords) return null;
//                     return (
//                         <Marker key={disaster.id} position={[coords.lat, coords.lon]} icon={customIcon}>
//                             <Popup>
//                                 <strong>{disaster.disaster_type}</strong>
//                                 <br />
//                                 Location: {disaster.location}
//                                 <br />
//                                 People Affected: {disaster.people_affected}
//                             </Popup>
//                         </Marker>
//                     );
//                 })}
//             </MapContainer>
//         </div>
//     );
// };

// export default DisasterMap;
























// import React, { useEffect, useState, useRef } from "react";
// import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
// import L from "leaflet";

// // Custom marker icon
// const customIcon = new L.Icon({
//     iconUrl: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
//     iconSize: [32, 32],
//     iconAnchor: [16, 32],
//     popupAnchor: [0, -32],
// });

// const DisasterMap = () => {
//     const [disasters, setDisasters] = useState([]);
//     const [locationCoords, setLocationCoords] = useState({});
//     const locationCoordsRef = useRef({});

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/disasters/")
//             .then((res) => res.json())
//             .then((data) => {
//                 console.log("Disaster Data:", data);  // ✅ DEBUG HERE
//                 setDisasters(data);
//             })
//             .catch((err) => console.error("Error fetching disaster data:", err));
//     }, []);
    

//     // Fetch coordinates for disaster locations
//     useEffect(() => {
//         const fetchCoordinates = async (location) => {
//             try {
//                 const response = await fetch(
//                     `https://nominatim.openstreetmap.org/search?format=json&q=${location}, Maharashtra`
//                 );
//                 const data = await response.json();
//                 if (data.length > 0) {
//                     return { lat: parseFloat(data[0].lat), lon: parseFloat(data[0].lon) };
//                 }
//             } catch (error) {
//                 console.error("Error fetching coordinates for", location, error);
//             }
//             return null;
//         };

//         const getAllCoordinates = async () => {
//             const newCoords = {};
//             for (const disaster of disasters) {
//                 if (disaster.location && !locationCoordsRef.current[disaster.location]) {
//                     const coords = await fetchCoordinates(disaster.location);
//                     if (coords) {
//                         newCoords[disaster.location] = coords;
//                     }
//                 }
//             }
//             if (Object.keys(newCoords).length > 0) {
//                 setLocationCoords((prev) => {
//                     const updatedCoords = { ...prev, ...newCoords };
//                     locationCoordsRef.current = updatedCoords;
//                     return updatedCoords;
//                 });
//             }
//         };

//         if (disasters.length > 0) {
//             getAllCoordinates();
//         }
//     }, [disasters]);

//     return (
//         <div style={{ height: "400px", width: "100%" }}> {/* ✅ INLINE CSS APPLIED */}
//             <MapContainer
//                 center={[19.7515, 75.7139]}
//                 zoom={6}
//                 style={{ height: "100%", width: "100%", zIndex: "0" }} // ✅ INLINE CSS
//             >
//                 <TileLayer
//                     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//                     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//                 />
//                 {disasters.map((disaster) => {
//                     const coords = locationCoords[disaster.location];
//                     if (!coords) return null;
//                     return (
//                         <Marker key={disaster.id} position={[coords.lat, coords.lon]} icon={customIcon}>
//                             <Popup>
//                                 <strong>{disaster.disaster_type}</strong>
//                                 <br />
//                                 Location: {disaster.location}
//                                 <br />
//                                 People Affected: {disaster.people_affected}
//                             </Popup>
//                         </Marker>
//                     );
//                 })}
//             </MapContainer>
//         </div>
//     );
// };

// export default DisasterMap;





















































































// import React, { useEffect, useState, useRef } from "react";
// import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
// import L from "leaflet";

// // Custom marker icon
// const customIcon = new L.Icon({
//     iconUrl: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
//     iconSize: [32, 32],
//     iconAnchor: [16, 32],
//     popupAnchor: [0, -32],
// });

// const DisasterMap = () => {
//     const [disasters, setDisasters] = useState([]);
//     const [locationCoords, setLocationCoords] = useState({});
//     const locationCoordsRef = useRef({});

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/disasters/")
//             .then((res) => res.json())
//             .then((data) => {
//                 console.log("Disaster Data:", data);  // ✅ DEBUG HERE
//                 setDisasters(data);
//             })
//             .catch((err) => console.error("Error fetching disaster data:", err));
//     }, []);

//     // Fetch coordinates for disaster locations
//     useEffect(() => {
//         const fetchCoordinates = async (location) => {
//             try {
//                 const response = await fetch(
//                     `https://nominatim.openstreetmap.org/search?format=json&q=${location}, Maharashtra`
//                 );
//                 const data = await response.json();
//                 if (data.length > 0) {
//                     return { lat: parseFloat(data[0].lat), lon: parseFloat(data[0].lon) };
//                 }
//             } catch (error) {
//                 console.error("Error fetching coordinates for", location, error);
//             }
//             return null;
//         };

//         const getAllCoordinates = async () => {
//             const newCoords = {};
//             for (const disaster of disasters) {
//                 if (disaster.location && !locationCoordsRef.current[disaster.location]) {
//                     const coords = await fetchCoordinates(disaster.location);
//                     if (coords) {
//                         newCoords[disaster.location] = coords;
//                     }
//                 }
//             }
//             if (Object.keys(newCoords).length > 0) {
//                 setLocationCoords((prev) => {
//                     const updatedCoords = { ...prev, ...newCoords };
//                     locationCoordsRef.current = updatedCoords;
//                     return updatedCoords;
//                 });
//             }
//         };

//         if (disasters.length > 0) {
//             getAllCoordinates();
//         }
//     }, [disasters]);

//     return (
//         <div style={{ height: "400px", width: "100%" }}> {/* ✅ INLINE CSS APPLIED */}
//             <MapContainer
//                 center={[19.7515, 75.7139]}
//                 zoom={6}
//                 style={{ height: "100%", width: "100%", zIndex: "0" }} // ✅ INLINE CSS
//             >
//                 <TileLayer
//                     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//                     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//                 />

//                 {/* Default Marker for Maharashtra */}
//                 <Marker position={[19.7515, 75.7139]} icon={customIcon}>
//                     <Popup><strong>Maharashtra (Default)</strong></Popup>
//                 </Marker>

//                 {/* Markers for disasters */}
//                 {disasters.map((disaster) => {
//                     const coords = locationCoords[disaster.location];
//                     if (!coords) return null;
//                     return (
//                         <Marker key={disaster.id} position={[coords.lat, coords.lon]} icon={customIcon}>
//                             <Popup>
//                                 <strong>{disaster.disaster_type}</strong>
//                                 <br />
//                                 Location: {disaster.location}
//                                 <br />
//                                 People Affected: {disaster.people_affected}
//                             </Popup>
//                         </Marker>
//                     );
//                 })}
//             </MapContainer>
//         </div>
//     );
// };

// export default DisasterMap;



















































import React, { useEffect, useState, useRef } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// 📍 Custom marker icon
const customIcon = new L.Icon({
    iconUrl: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32],
});

// ✅ Manually mapped coordinates for Maharashtra locations
const knownLocations = {
    "Ahmednagar": { lat: 19.0948, lon: 74.7480 },
    "Amravati": { lat: 20.9374, lon: 77.7796 },
    "Aurangabad": { lat: 19.8762, lon: 75.3433 },
    "Kolhapur": { lat: 16.7049, lon: 74.2433 },
    "Latur": { lat: 18.4088, lon: 76.5604 },
    "Mumbai": { lat: 19.0760, lon: 72.8777 },
    "Nagpur": { lat: 21.1458, lon: 79.0882 },
    "Nanded": { lat: 19.1383, lon: 77.3209 },
    "Nashik": { lat: 19.9975, lon: 73.7898 },
    "Pune": { lat: 18.5204, lon: 73.8567 },
    "Ratnagiri": { lat: 16.9944, lon: 73.3000 },
    "Satara": { lat: 17.6805, lon: 74.0183 },
    "Solapur": { lat: 17.6599, lon: 75.9064 },
    "Thane": { lat: 19.2183, lon: 72.9781 },
};

const DisasterMap = () => {
    const [disasters, setDisasters] = useState([]);
    const [locationCoords, setLocationCoords] = useState(knownLocations);
    const locationCoordsRef = useRef(knownLocations);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/disasters/")
            .then((res) => res.json())
            .then((data) => {
                console.log("Disaster Data:", data);  // ✅ DEBUG LOG
                setDisasters(data);
            })
            .catch((err) => console.error("Error fetching disaster data:", err));
    }, []);

    // Fetch coordinates for unknown locations
    useEffect(() => {
        const fetchCoordinates = async (location) => {
            try {
                const response = await fetch(
                    `https://nominatim.openstreetmap.org/search?format=json&q=${location}, Maharashtra`
                );
                const data = await response.json();
                if (data.length > 0) {
                    return { lat: parseFloat(data[0].lat), lon: parseFloat(data[0].lon) };
                }
            } catch (error) {
                console.error("Error fetching coordinates for", location, error);
            }
            return null;
        };

        const getAllCoordinates = async () => {
            const newCoords = {};
            for (const disaster of disasters) {
                if (disaster.location && !locationCoordsRef.current[disaster.location]) {
                    const coords = await fetchCoordinates(disaster.location);
                    if (coords) {
                        newCoords[disaster.location] = coords;
                    }
                }
            }
            if (Object.keys(newCoords).length > 0) {
                setLocationCoords((prev) => {
                    const updatedCoords = { ...prev, ...newCoords };
                    locationCoordsRef.current = updatedCoords;
                    return updatedCoords;
                });
            }
        };

        if (disasters.length > 0) {
            getAllCoordinates();
        }
    }, [disasters]);

    return (
        <div style={{ height: "400px", width: "100%" }}> {/* ✅ INLINE CSS APPLIED */}
            <MapContainer
                center={[19.7515, 75.7139]}
                zoom={6}
                style={{ height: "100%", width: "100%", zIndex: "0" }} // ✅ INLINE CSS
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />

                {/* 📍 Default Marker for Maharashtra */}
                <Marker position={[19.7515, 75.7139]} icon={customIcon}>
                    <Popup><strong>Maharashtra (Default)</strong></Popup>
                </Marker>

                {/* 📌 Markers for disasters */}
                {disasters.map((disaster) => {
                    const coords = locationCoords[disaster.location];
                    if (!coords) return null;
                    return (
                        <Marker key={disaster.id} position={[coords.lat, coords.lon]} icon={customIcon}>
                            <Popup>
                                <strong>{disaster.disaster_type}</strong>
                                <br />
                                Location: {disaster.location}
                                <br />
                                People Affected: {disaster.people_affected}
                            </Popup>
                        </Marker>
                    );
                })}
            </MapContainer>
        </div>
    );
};

export default DisasterMap;
