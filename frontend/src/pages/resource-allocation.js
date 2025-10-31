import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import { Container, Form, Button, Row, Col, Alert, Spinner } from "react-bootstrap";
import { FaCloudUploadAlt } from "react-icons/fa";
import "bootstrap/dist/css/bootstrap.min.css";
import "./resource.css"; 

const ResourceForm = () => {
  const [formData, setFormData] = useState({
    disaster_type: "",
    location: "",
    date: "",
    people_affected: "",
    infrastructure_damage: "",
    funds_allocated: "",
    casualties: "",
    impact_level: "",
    cluster_label: "",
    resource_name: "",
    allocated_resources: "",
  });

  const [csvFile, setCsvFile] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [fileName, setFileName] = useState("No file chosen");
  const navigate = useNavigate();


  // Handles input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Handles CSV File Upload
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setCsvFile(file || null);
    setFileName(file ? file.name : "No file chosen");
  };

  // Handles Form Submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const formDataToSend = new FormData();

      // Append form fields
      Object.entries(formData).forEach(([key, value]) => {
        formDataToSend.append(key, value);
      });

      // Append CSV file if selected
      if (csvFile) {
        formDataToSend.append("csv_File", csvFile);
      }

      const response = await fetch("http://127.0.0.1:8000/api/userinput/", {
        method: "POST",
        body: formDataToSend,
      });

      // if (!response.ok) {
      //   const errorData = await response.json();
      //   throw new Error(`Server Error: ${errorData.detail || response.statusText}`);
      // }

      const result = await response.json();
      console.log("✅ Form Submitted:", result);
      setSubmitted(true);
      navigate('/analytics'); 
      setTimeout(() => setSubmitted(false), 3000);
    } catch (err) {
      console.error("❌ Submission Error:", err);
      setError(err.message || "Error submitting form. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="form-container">
      <Row className="justify-content-center">
        <Col md={8}>
          <h2 className="text-center mb-4">🌍 Disaster Resource Allocation</h2>

          {submitted && <Alert variant="success">✅ Form submitted successfully!</Alert>}
          {error && <Alert variant="danger">{error}</Alert>}

          <Form onSubmit={handleSubmit} className="p-4 shadow-lg rounded bg-light">
            <Row>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Disaster Type *</Form.Label>
                  <Form.Control type="text" name="disaster_type" placeholder="e.g., Flood, Earthquake" onChange={handleChange} />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Location *</Form.Label>
                  <Form.Control type="text" name="location" placeholder="Enter location" onChange={handleChange} />
                </Form.Group>
              </Col>
            </Row>

            <Row>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Date *</Form.Label>
                  <Form.Control type="date" name="date" onChange={handleChange} />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Resource Name *</Form.Label>
                  <Form.Control type="text" name="resource_name" placeholder="e.g., Food, Medical Kits" onChange={handleChange} />
                </Form.Group>
              </Col>
            </Row>

            <Row>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>People Affected *</Form.Label>
                  <Form.Control type="number" name="people_affected" placeholder="Enter number" onChange={handleChange} />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Casualties *</Form.Label>
                  <Form.Control type="number" name="casualties" placeholder="Enter number" onChange={handleChange} />
                </Form.Group>
              </Col>
            </Row>

            <Row>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Infrastructure Damage (USD) *</Form.Label>
                  <Form.Control type="number" name="infrastructure_damage" placeholder="Enter amount" onChange={handleChange} />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group className="mb-3">
                  <Form.Label>Funds Allocated (USD) *</Form.Label>
                  <Form.Control type="number" name="funds_allocated" placeholder="Enter amount" onChange={handleChange} />
                </Form.Group>
              </Col>
            </Row>

            <Form.Group className="mb-3">
              <Form.Label>Allocated Resources *</Form.Label>
              <Form.Control type="number" name="allocated_resources" placeholder="Enter amount" onChange={handleChange} />
            </Form.Group>

            {/* Optional CSV Upload */}
            <Form.Group className="mb-4">
              <Form.Label>Upload CSV File (Optional)</Form.Label>
              <div className="custom-file-upload">
                <input type="file" id="fileUpload" hidden onChange={handleFileChange} />
                <label htmlFor="fileUpload" className="upload-btn">
                  <FaCloudUploadAlt size={20} /> Choose File
                </label>
                <span className="file-name">{fileName}</span>
              </div>
            </Form.Group>

            <Button type="submit" variant="primary" className="w-100 fw-bold" disabled={loading}>
              {loading ? <Spinner animation="border" size="sm" /> : "🚀 Submit"}
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default ResourceForm;
