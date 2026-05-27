# Disaster Relief Resource Allocation System (DRRAS)

## Overview

The **Disaster Relief Resource Allocation System (DRRAS)** is an AI-powered disaster management platform designed to improve disaster response and resource allocation during emergencies. The system focuses on disaster-prone regions in Maharashtra and helps authorities, relief workers, and volunteers manage resources efficiently using Machine Learning, clustering, and optimization techniques.

The project combines:

* Real-time disaster reporting
* Disaster clustering and analysis
* Resource allocation optimization
* Volunteer management
* Beneficiary tracking
* Interactive dashboard visualization
* Multi-language accessibility support

---

## Features

### Disaster Management

* Add and manage disaster reports
* Store disaster location and severity details
* Historical disaster data analysis
* Real-time disaster monitoring

### AI & Machine Learning

* Disaster clustering using unsupervised learning
* Predictive analysis for disaster-prone regions
* Resource allocation optimization using Linear Programming
* Data-driven disaster management insights

### Resource Allocation

* Smart allocation of resources based on disaster severity
* Allocation by resource type
* Optimization for efficient relief distribution
* Resource tracking and monitoring


### Dashboard & Visualization

* Interactive analytics dashboard
* Cluster visualization
* Disaster impact analysis
* Resource monitoring interface

### Additional Functionalities

* Role-based access (Admin & Relief Worker)
* Beneficiary feedback system
* Multi-language support
* Disaster heatmap visualization

---

## Tech Stack

### Frontend

* React.js
* Bootstrap
* Axios
* CSS

### Backend

* Django
* Django REST Framework
* SQLite

### Machine Learning & Optimization

* Scikit-learn
* Pandas
* NumPy
* SciPy
* Linear Programming

---

## Project Structure

```bash
DRRAS/
│
├── backend/
│   ├── api/
│   │   ├── clustering.py
│   │   ├── optimization.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── serializers.py
│   │
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
│
└── venv/
```

---

## Database Models

### DisasterData

Stores disaster-related information.

### BeneficiaryData

Stores beneficiary details and aid information.

### ResourceData

Stores available disaster relief resources.

### DisasterCluster

Stores disaster clustering results.

### UserInput

Stores manually submitted disaster reports.

### OptimizedAllocation

Stores optimized resource allocation results.

## Installation & Setup

### Prerequisites

Make sure the following are installed:

* Python 3.x
* Node.js
* npm
* pip
* Git

---

## Backend Setup (Django)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DRRAS.git
cd DRRAS
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 6. Start Backend Server

```bash
python manage.py runserver
```

Backend will run at:

```bash
http://127.0.0.1:8000/
```

---

## Frontend Setup (React)

### 1. Navigate to Frontend Folder

```bash
cd frontend
```

### 2. Install Packages

```bash
npm install
```

### 3. Start React Application

```bash
npm start
```

Frontend will run at:

```bash
http://localhost:3000/
```

---

## Machine Learning Modules

### Clustering

The project uses unsupervised machine learning techniques to group disasters based on:

* Severity
* Location
* Resource requirements
* Disaster type

### Optimization

Linear Programming is used to:

* Optimize resource distribution
* Reduce response delays
* Improve resource utilization

---

## API Endpoints

| Endpoint              | Description                      |
| --------------------- | -------------------------------- |
| `/api/disasters/`     | Get disaster data                |
| `/api/resources/`     | Manage resources                 |
| `/api/beneficiaries/` | Beneficiary data                 |
| `/api/cluster/`       | Disaster clustering results      |
| `/api/optimize/`      | Resource allocation optimization |


---

## Future Enhancements

* Real-time weather API integration
* SMS and Email alerts
* Mobile application support
* GIS-based live disaster mapping
* AI-powered disaster prediction
* Emergency communication system

---

## Use Case

DRRAS can be used by:

* Government disaster management authorities
* NGOs and relief organizations
* Emergency response teams
* Volunteers
* Researchers and analysts

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Full Stack Web Development
* Machine Learning
* Data Analysis
* Optimization Techniques
* Disaster Management Systems
* REST API Development
* Dashboard Visualization

---

## Contributing

Contributions are welcome.

### Steps to Contribute

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit changes
5. Push to your branch
6. Create a Pull Request

---

## License

This project is created for educational and research purposes.

---

## Author

**Prerna Divakar**

M.Sc Data Science Student

---

## Contact

For suggestions or collaboration:

* GitHub: https://github.com/Prernadivakar03
* LinkedIn: www.linkedin.com/in/prerna-d-130045283
* Email: prernadivakar0328@gmail.com
