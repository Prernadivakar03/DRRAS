// imp 

// import DisasterMap from "C:\\prerna\\DRRAS\\frontend\\src\\components\\Disastermap.js"; // ✅ Fixed import path
// import React, { useEffect, useState } from "react";
// import {
//     BarChart, Bar, XAxis, YAxis, Tooltip, PieChart, Pie, Cell, Legend, ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis
// } from "recharts";
// import "bootstrap/dist/css/bootstrap.min.css"; // ✅ Bootstrap Added


// const Card = ({ title, value, children }) => (
//     <div className="card shadow-lg border-0 rounded-lg p-4 text-center transition transform hover:scale-105 bg-white">
//         <h2 className="card-title text-xl font-bold text-primary">{title}</h2>
//         {value !== undefined ? <p className="text-3xl font-semibold text-danger">{value}</p> : children}
//     </div>
// );

// const Dashboard = () => {
//     const [disasterData, setDisasterData] = useState([]);
//     const [resourceData, setResourceData] = useState([]);
//     const [allocations, setAllocations] = useState([]);
//     const [optimizedAllocations, setOptimizedAllocations] = useState([]);
//     const [beneficiaryData, setBeneficiaryData] = useState([]);
 
//     useEffect(() => {
//         // ✅ Fetch Disasters
//         const fetchDisasters = async () => {
//             try {
//                 const res = await fetch("http://127.0.0.1:8000/api/disasters/");
//                 const data = await res.json();
//                 setDisasterData(data || []);
//             } catch (error) {
//                 console.error("Error fetching disasters:", error);
//             }
//         };

//         // ✅ Fetch Resources
//         const fetchResources = async () => {
//             try {
//                 const res = await fetch("http://127.0.0.1:8000/api/resources/");
//                 const data = await res.json();
//                 setResourceData(data || []);
//             } catch (error) {
//                 console.error("Error fetching resources:", error);
//             }
//         };

//         // ✅ Fetch Allocations
//         const fetchAllocations = async () => {
//             try {
//                 const res = await fetch("http://127.0.0.1:8000/api/allocate-resources/");
//                 const data = await res.json();
//                 setAllocations(data.allocations || []);
//             } catch (error) {
//                 console.error("Error fetching allocations:", error);
//             }
//         };

//         // ✅ Fetch Optimized Allocations
//         const fetchOptimizedAllocations = async () => {
//             try {
//                 const res = await fetch("http://127.0.0.1:8000/api/run-optimization/");
//                 const data = await res.json();
//                 setOptimizedAllocations(data.allocations || []);
//             } catch (error) {
//                 console.error("Error fetching optimized allocations:", error);
//             }
//         };

        
//     // ✅ Fetch Beneficiaries
//     const fetchBeneficiaries = async () => {
//         try {
//           const res = await fetch("http://127.0.0.1:8000/api/beneficiaries/");
//           const data = await res.json();
  
//           // Group by location and count aid types
//           const groupedData = data.reduce((acc, item) => {
//             if (!acc[item.location]) acc[item.location] = {};
//             acc[item.location][item.aid_received] = (acc[item.location][item.aid_received] || 0) + 1;
//             return acc;
//           }, {});
  
//           const chartData = Object.keys(groupedData).map((location) => ({
//             location,
//             ...groupedData[location],
//           }));
  
//           setBeneficiaryData(chartData);
//         } catch (error) {
//           console.error("Error fetching beneficiaries:", error);
//         }
//       };
  

//         fetchDisasters();
//         fetchResources();
//         fetchAllocations();
//         fetchOptimizedAllocations();
//         fetchBeneficiaries();
//     }, []);



//     // ✅ Disaster Impact Data for Bar Chart
//     const disasterImpactData = disasterData.reduce((acc, disaster) => {
//         if (disaster.disaster_type && disaster.people_affected) {
//             acc[disaster.disaster_type] = (acc[disaster.disaster_type] || 0) + disaster.people_affected;
//         }
//         return acc;
//     }, {});

//     const disasterChartData = Object.keys(disasterImpactData).map(type => ({
//         name: type.length > 12 ? type.slice(0, 12) + "..." : type,
//         affected: disasterImpactData[type],
//     }));

//     // ✅ Resource Type Data for Pie Chart
//     const resourceTypeCounts = resourceData.reduce((acc, resource) => {
//         if (resource.resource_type && resource.quantity) {
//             acc[resource.resource_type] = (acc[resource.resource_type] || 0) + resource.quantity;
//         }
//         return acc;
//     }, {});

//     const resourceChartData = Object.keys(resourceTypeCounts).map(type => ({
//         name: type.length > 12 ? type.slice(0, 12) + "..." : type,
//         value: resourceTypeCounts[type],
//     }));

//     const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#FF6384", "#36A2EB"];

//     return (
//         <div className="container mt-5">
//             <div className="row g-4">
//                 {/* ✅ Total Disasters & Resources Cards */}
//                 <div className="col-md-6">
//                     <Card title="Total Disasters" value={disasterData.length} />
//                 </div>
//                 <div className="col-md-6">
//                     <Card title="Available Resources" value={resourceData.length} />
//                 </div>

//                 {/* ✅ Disaster Impact Bar Chart */}
//                 <div className="col-md-6">
//                     <Card title="People Affected by Disaster Type">
//                         <ResponsiveContainer width="100%" height={300}>
//                             <BarChart data={disasterChartData} margin={{ bottom: 50 }}>
//                                 <XAxis dataKey="name" angle={-30} textAnchor="end" tick={{ fontSize: 12 }} />
//                                 <YAxis />
//                                 <Tooltip />
//                                 <Bar dataKey="affected" fill="#FF5733" />
//                             </BarChart>
//                         </ResponsiveContainer>
//                     </Card>
//                 </div>

//                 {/* ✅ Resource Allocation Pie Chart */}
//                 <div className="col-md-6">
//                     <Card title="Resource Allocation">
//                         <ResponsiveContainer width="100%" height={350}>
//                             <PieChart>
//                                 <Pie
//                                     data={resourceChartData}
//                                     dataKey="value"
//                                     nameKey="name"
//                                     cx="50%"
//                                     cy="50%"
//                                     outerRadius={90}
//                                     label
//                                 >
//                                     {resourceChartData.map((_, index) => (
//                                         <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
//                                     ))}
//                                 </Pie>
//                                 <Tooltip />
//                                 <Legend layout="vertical" align="right" verticalAlign="middle" />
//                             </PieChart>
//                         </ResponsiveContainer>
//                     </Card>
//                 </div>

//                 {/* ✅ Disaster Map */}
//                 <div className="col-md-12">
//                     <Card title="Disaster Locations in Maharashtra">
//                         <DisasterMap />
//                     </Card>
//                 </div>

                
//       {/* ✅ Beneficiary Chart */}
//       <div className="mt-4">
//         <h2>Beneficiary Aid Types by Location</h2>
//         <RadarChart cx={300} cy={250} outerRadius={150} width={600} height={500} data={beneficiaryData}>
//           <PolarGrid />
//           <PolarAngleAxis dataKey="location" />
//           <PolarRadiusAxis />
//           <Tooltip />
//           {Object.keys(beneficiaryData[0] || {}).filter((key) => key !== "location").map((key, index) => (
//             <Radar
//               key={index}
//               name={key}
//               dataKey={key}
//               stroke="#8884d8"
//               fill="#8884d8"
//               fillOpacity={0.6}
//             />
//           ))}
//         </RadarChart>
//       </div>

//                 {/* ✅ Allocations Table + Optimized Allocations Table */}
//                 <div className="col-md-6">
//                     <Card title="Resource Allocation Details">
//                         <div className="table-responsive" style={{ maxHeight: "300px", overflowY: "auto" }}>
//                             <table className="table table-striped table-bordered">
//                                 <thead className="table-dark">
//                                     <tr>
//                                         <th>ID</th>
//                                          <th>Location</th>
//                                          <th>Disaster Type</th>
//                                          <th>Impact Level</th>
//                                          <th>Resource Type</th>
//                                          <th>Allocated Resources</th>
//                                     </tr>
//                                 </thead>
//                                 <tbody>
//                                     {allocations.map((allocation, index) => (
//                                         <tr key={index}>
//                                             <td>{allocation.disaster_id}</td>
//                                             <td>{allocation.location}</td>
//                                             <td>{allocation.disaster_type}</td>
//                                             <td>{allocation.impact_level}</td>
//                                             <td>{allocation.resource_type}</td>
//                                             <td>{allocation.allocated_resources}</td>
//                                         </tr>
//                                     ))}
//                                 </tbody>
//                             </table>
//                         </div>
//                     </Card>
//                 </div>

//                 <div className="col-md-6">
//                     <Card title="Optimized Allocation Details">
//                         <div className="table-responsive" style={{ maxHeight: "300px", overflowY: "auto" }}>
//                             <table className="table table-striped table-bordered">
//                                 <thead className="table-dark">
//                                     <tr>
//                                         <th>Location</th>
//                                         <th>Cluster Impact</th>
//                                         <th>Resource</th>
//                                         <th>Quantity</th>
//                                     </tr>
//                                 </thead>
//                                 <tbody>
//                                     {optimizedAllocations.map((allocation, index) => (
//                                         <tr key={index}>
//                                             <td>{allocation.location}</td>
//                                             <td>{allocation.cluster_impact}</td>
//                                             <td>{allocation.resource_name}</td>
//                                             <td>{allocation.quantity}</td>
//                                         </tr>
//                                     ))}
//                                 </tbody>
//                             </table>
//                         </div>
//                     </Card>
//                 </div>

//             </div>
//         </div>
//     );
// };

// export default Dashboard;

//imp 
















































































































































































































































import "./analytics.css"
import DisasterMap from "C:\\prerna\\DRRAS\\frontend\\src\\components\\Disastermap.js"; // ✅ Fixed import path
import React, { useEffect, useState } from "react";
import {
    BarChart, Bar, XAxis, YAxis, Tooltip,ComposedChart, PieChart, Pie,Cell, Legend, ResponsiveContainer,CartesianGrid,Line, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis
} from "recharts";
import "bootstrap/dist/css/bootstrap.min.css"; // ✅ Bootstrap Added
import ResourceStatusCards from "./ResourceStatusCards";



const Card = ({ title, value, children }) => (
    <div className="card shadow-lg border-0 rounded-lg p-4 text-center transition transform hover:scale-105 bg-white">
        <h2 className="card-title text-xl font-bold text-primary">{title}</h2>
        {value !== undefined ? <p className="text-3xl font-semibold text-danger">{value}</p> : children}
    </div>
);

const Dashboard = () => {
    const [disasterData, setDisasterData] = useState([]);
    const [resourceData, setResourceData] = useState([]);
    const [allocations, setAllocations] = useState([]);
    const [optimizedAllocations, setOptimizedAllocations] = useState([]);
    const [beneficiaryData, setBeneficiaryData] = useState([]);
    const [userInputData, setUserInputData] = useState([]);
 
    useEffect(() => {
        // ✅ Fetch Disasters
        const fetchDisasters = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/api/disasters/");
                const data = await res.json();
                setDisasterData(data || []);
            } catch (error) {
                console.error("Error fetching disasters:", error);
            }
        };

        // ✅ Fetch Resources
        const fetchResources = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/api/resources/");
                const data = await res.json();
                setResourceData(data || []);
            } catch (error) {
                console.error("Error fetching resources:", error);
            }
        };

        // ✅ Fetch Allocations
        const fetchAllocations = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/api/allocate-resources/");
                const data = await res.json();
                setAllocations(data.allocations || []);
            } catch (error) {
                console.error("Error fetching allocations:", error);
            }
        };

        // ✅ Fetch Optimized Allocations
        const fetchOptimizedAllocations = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/api/run-optimization/");
                const data = await res.json();
                setOptimizedAllocations(data.allocations || []);
            } catch (error) {
                console.error("Error fetching optimized allocations:", error);
            }
        };

        
    // ✅ Fetch Beneficiaries
    const fetchBeneficiaries = async () => {
        try {
          const res = await fetch("http://127.0.0.1:8000/api/beneficiaries/");
          const data = await res.json();
  
          // Group by location and count aid types
          const groupedData = data.reduce((acc, item) => {
            if (!acc[item.location]) acc[item.location] = {};
            acc[item.location][item.aid_received] = (acc[item.location][item.aid_received] || 0) + 1;
            return acc;
          }, {});
  
          const chartData = Object.keys(groupedData).map((location) => ({
            location,
            ...groupedData[location],
          }));
  
          setBeneficiaryData(chartData);
        } catch (error) {
          console.error("Error fetching beneficiaries:", error);
        }
      };


      const fetchUserInput = async () => {
        try {
            const res = await fetch("http://127.0.0.1:8000/api/userinput/");
            const data = await res.json();
            setUserInputData(data || []);
        } catch (error) {
            console.error("Error fetching user input data:", error);
        }
    };

  

        fetchDisasters();
        fetchResources();
        fetchAllocations();
        fetchOptimizedAllocations();
        fetchBeneficiaries();
        fetchUserInput();
    }, []);



    // ✅ Disaster Impact Data for Bar Chart
    const disasterImpactData = disasterData.reduce((acc, disaster) => {
        if (disaster.disaster_type && disaster.people_affected) {
            acc[disaster.disaster_type] = (acc[disaster.disaster_type] || 0) + disaster.people_affected;
        }
        return acc;
    }, {});

    const disasterChartData = Object.keys(disasterImpactData).map(type => ({
        name: type.length > 12 ? type.slice(0, 12) + "..." : type,
        affected: disasterImpactData[type],
    }));

    // ✅ Resource Type Data for Pie Chart
    const resourceTypeCounts = resourceData.reduce((acc, resource) => {
        if (resource.resource_type && resource.quantity) {
            acc[resource.resource_type] = (acc[resource.resource_type] || 0) + resource.quantity;
        }
        return acc;
    }, {});

    const resourceChartData = Object.keys(resourceTypeCounts).map(type => ({
        name: type.length > 12 ? type.slice(0, 12) + "..." : type,
        value: resourceTypeCounts[type],
    }));

    const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#FF6384", "#36A2EB"];

    return (

        <div className="container mt-5">
      <h1 className="mb-4 text-center text-3xl font-bold text-dark" style={{padding:"0px" , fontFamily:"fort" , fontWeight:"bold"}}>📊 Disaster Relief Resource Allocation Dashboard</h1>
    
        <div className="container mt-5">
            <div className="row g-4">
                {/* ✅ Total Disasters & Resources Cards */}
                <div className="col-md-4">
                    <Card title="Total Disasters" value={disasterData.length} />
                </div>
                <div className="col-md-4">
                    <Card title="Available Resources" value={resourceData.length} />
                </div>
                <div className="col-md-4">
                    <Card title="User Inputs" value={userInputData.length}/>
                </div>


                 {/* ✅ Resource Status Cards */}
            <div className="mt-5">
                <ResourceStatusCards />
            </div>
            

                {/* ✅ Disaster Impact Bar Chart */}
                <div className="col-md-6">
                    <Card title="People Affected by Disaster Type">
                        <ResponsiveContainer width="100%" height={300}>
                            <BarChart data={disasterChartData} margin={{ bottom: 50 }}>
                                <XAxis dataKey="name" angle={-30} textAnchor="end" tick={{ fontSize: 12 }} />
                                <YAxis />
                                <Tooltip />
                                <Bar dataKey="affected" fill="#FF5733" />
                            </BarChart>
                        </ResponsiveContainer>
                    </Card>
                </div>

                {/* ✅ Resource Allocation Pie Chart */}
                <div className="col-md-6">
                    <Card title="Resource Allocation">
                        <ResponsiveContainer width="100%" height={350}>
                            <PieChart>
                                <Pie
                                    data={resourceChartData}
                                    dataKey="value"
                                    nameKey="name"
                                    cx="50%"
                                    cy="50%"
                                    outerRadius={90}
                                    label
                                >
                                    {resourceChartData.map((_, index) => (
                                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                    ))}
                                </Pie>
                                <Tooltip />
                                <Legend layout="vertical" align="right" verticalAlign="middle" />
                            </PieChart>
                        </ResponsiveContainer>
                    </Card>
                </div>

                {/* ✅ Disaster Map */}
                <div className="col-md-12">
                    <Card title="Disaster Locations in Maharashtra">
                        <DisasterMap />
                    </Card>
                </div> 
                <div className="col-md-6">
  {/* ✅ Beneficiary Chart in a Card */}
  <Card title="Beneficiary Aid Types by Location" className="chart">
    <ResponsiveContainer width="100%" height={320}>
      <RadarChart cx={200} cy={150} outerRadius={100} data={beneficiaryData}>
        <PolarGrid />
        <PolarAngleAxis dataKey="location" />
        <PolarRadiusAxis />
        <Tooltip />
        {Object.keys(beneficiaryData[0] || {}).filter(key => key !== "location").map((key, index) => (
          <Radar key={index} name={key} dataKey={key} stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
        ))}
      </RadarChart>
    </ResponsiveContainer>
  </Card>
</div>

  {/* ✅ Disaster Data Chart in a Card */}
<div className="col-md-6">
  <Card title="Disaster Data by Location" className="chart">
    {userInputData.length > 0 && (
      <ResponsiveContainer width="100%" height={320}>
        <ComposedChart data={userInputData}>
          <CartesianGrid stroke="#f0f0f0" />
          <XAxis dataKey="location" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="infrastructure_damage" barSize={20} fill="#4f46e5" radius={[4, 4, 0, 0]} />
          <Line type="monotone" dataKey="people_affected" stroke="#ff6347" strokeWidth={1.5} />
          <Line type="monotone" dataKey="casualties" stroke="#00c49f" strokeWidth={1.5} />
        </ComposedChart>
      </ResponsiveContainer>
    )}
  </Card>
</div>



                {/* ✅ Allocations Table + Optimized Allocations Table */}
                <div className="col-md-6">
                    <Card title="Resource Allocation Details">
                        <div className="table-responsive" style={{ maxHeight: "300px", overflowY: "auto" }}>
                            <table className="table table-striped table-bordered">
                                <thead className="table-dark">
                                    <tr>
                                        <th>ID</th>
                                         <th>Location</th>
                                         <th>Disaster Type</th>
                                         <th>Impact Level</th>
                                         <th>Resource Type</th>
                                         <th>Allocated Resources</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {allocations.map((allocation, index) => (
                                        <tr key={index}>
                                            <td>{allocation.disaster_id}</td>
                                            <td>{allocation.location}</td>
                                            <td>{allocation.disaster_type}</td>
                                            <td>{allocation.impact_level}</td>
                                            <td>{allocation.resource_type}</td>
                                            <td>{allocation.allocated_resources}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </Card>
                </div>

                <div className="col-md-6">
                    <Card title="Optimized Allocation Details">
                        <div className="table-responsive" style={{ maxHeight: "300px", overflowY: "auto" }}>
                            <table className="table table-striped table-bordered">
                                <thead className="table-dark">
                                    <tr>
                                        <th>Location</th>
                                        <th>Cluster Impact</th>
                                        <th>Resource</th>
                                        <th>Quantity</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {optimizedAllocations.map((allocation, index) => (
                                        <tr key={index}>
                                            <td>{allocation.location}</td>
                                            <td>{allocation.cluster_impact}</td>
                                            <td>{allocation.resource_name}</td>
                                            <td>{allocation.quantity}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </Card>
                </div>
            </div>
            <div className="url-link" style={{ marginTop: "20px" }}>
    <p style={{ fontWeight: "bold" }}>API Endpoints:</p>
    {[
        "http://127.0.0.1:8000/api/",
        "http://127.0.0.1:8000/api/disasters/",
        "http://127.0.0.1:8000/api/beneficiaries/",
        "http://127.0.0.1:8000/api/resources/",
        "http://127.0.0.1:8000/api/userinput/",
        "http://127.0.0.1:8000/api/cluster/",
        "http://127.0.0.1:8000/api/run-optimization/",
        "http://127.0.0.1:8000/api/allocate-resources/"
    ].map((url, index) => (
        <a
            key={index}
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="url-link"
            style={{
                display: "block",
                color: "#4f46e5",
                textDecoration: "none",
                marginBottom: "5px",
                transition: "color 0.3s ease"
            }}
            onMouseEnter={(e) => e.target.style.color = "#ff6347"}
            onMouseLeave={(e) => e.target.style.color = "#4f46e5"}
        >
            {url}
        </a>
    ))}
    </div>
        </div>
        
        </div>

    );
};

export default Dashboard;

