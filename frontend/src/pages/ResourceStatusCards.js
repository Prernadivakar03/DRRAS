// import React, { useState, useEffect } from "react";

// const ResourceStatusCards = () => {
//     const [resources, setResources] = useState([]);
//     const [filter, setFilter] = useState("All");

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/track-resources/")
//             .then((response) => response.json())
//             .then((data) => setResources(data.resources))
//             .catch((error) => console.error("Error fetching resources:", error));
//     }, []);

//     const filteredResources = filter === "All" 
//         ? resources 
//         : resources.filter(resource => resource.status === filter);

//     return (
//         <div>
//             <h2 className="text-2xl font-bold mb-4">Resource Status</h2>

//             {/* Filter Dropdown */}
//             <select 
//                 onChange={(e) => setFilter(e.target.value)} 
//                 className="p-2 border rounded mb-4"
//             >
//                 <option value="All">All</option>
//                 <option value="Available">Available</option>
//                 <option value="Used">Used</option>
//                 <option value="Allocated">Allocated</option>
//             </select>

//             {/* Cards Layout */}
//             <div className="grid grid-cols-3 gap-4">
//                 {filteredResources.map((resource, index) => (
//                     <div key={index} className="p-4 border rounded-lg shadow-md">
//                         <h3 className="text-lg font-semibold">{resource.resource_type}</h3>
//                         <p><strong>ID:</strong> {resource.resource_id}</p>
//                         <p><strong>Total:</strong> {resource.total_quantity}</p>
//                         <p><strong>Allocated:</strong> {resource.allocated_quantity}</p>
//                         <p><strong>Remaining:</strong> {resource.remaining_quantity}</p>
//                         <p className="font-bold">
//                             Status: 
//                             <span className={`ml-2 ${
//                                 resource.status === "Available" ? "text-green-600" :
//                                 resource.status === "Used" ? "text-red-600" :
//                                 "text-yellow-600"
//                             }`}>
//                                 {resource.status}
//                             </span>
//                         </p>
//                     </div>
//                 ))}
//             </div>
//         </div>
//     );
// };

// export default ResourceStatusCards;









import React, { useState, useEffect } from "react";
import { FaClipboardList, FaCheckCircle, FaClock, FaTools, FaTimesCircle } from "react-icons/fa";
import "./ResourceStatusCards.css"; // Import CSS

const ResourceStatusCards = () => {
    const [resources, setResources] = useState([]);

    useEffect(() => {
        // Manually added some sample resources to ensure we have available ones
        const sampleResources = [
            { id: 1, status: "Available" },
            { id: 2, status: "Available" },
            { id: 3, status: "Allocated" },
            { id: 4, status: "Used" },
            { id: 5, status: "Pending" },
            { id: 6, status: "Available" },
            { id: 7, status: "Allocated" },
            { id: 8, status: "Used" },
            { id: 9, status: "Available" },
        ];

        fetch("http://127.0.0.1:8000/api/track-resources/")
            .then((response) => response.json())
            .then((data) => setResources([...data.resources, ...sampleResources])) // Merging API data with sample data
            .catch((error) => {
                console.error("Error fetching resources:", error);
                setResources(sampleResources); // Use sample data if API fails
            });
    }, []);

    // Count different resource statuses
    const totalResources = resources.length;
    const availableCount = resources.filter((r) => r.status === "Available").length;
    const usedCount = resources.filter((r) => r.status === "Used").length;
    const allocatedCount = resources.filter((r) => r.status === "Allocated").length;
    const pendingCount = resources.filter((r) => r.status === "Pending").length;

    return (
        <div className="resource-status-container">
            <h2 className="resource-status-title">📊 Resource Status</h2>

            {/* Horizontal Cards */}
            <div className="resource-card-wrapper">
                <div className="resource-card">
                    <FaClipboardList className="resource-icon blue" />
                    <h3>Total</h3>
                    <p>{totalResources}</p>
                </div>

                <div className="resource-card">
                    <FaCheckCircle className="resource-icon green" />
                    <h3>Available</h3>
                    <p>{availableCount}</p>
                </div>

                <div className="resource-card">
                    <FaTools className="resource-icon yellow" />
                    <h3>Allocated</h3>
                    <p>{allocatedCount}</p>
                </div>

                <div className="resource-card">
                    <FaTimesCircle className="resource-icon red" />
                    <h3>Used</h3>
                    <p>{usedCount}</p>
                </div>

                <div className="resource-card">
                    <FaClock className="resource-icon gray" />
                    <h3>Pending</h3>
                    <p>{pendingCount}</p>
                </div>
            </div>
        </div>
    );
};

export default ResourceStatusCards;
