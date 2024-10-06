# Job Recommendation Platform

## Overview
This project implements a backend service for an AI-powered talent acquisition platform that recommends relevant job postings to users based on their profiles and preferences. Built using **FastAPI** and **MySQL**.

### Features
- RESTful API with job recommendation functionality.
- MySQL database for storing job postings and user data.
- Matching algorithm that considers skills, experience level, job type, and location.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/kannan-2002/job-recommendation-platform.git
   cd job-recommendation-platform
2. Install dependencies:
   pip install -r requirements.txt
3. Set up the MySQL database:

Create a MySQL database and run the provided schema to set up the users and jobs tables.
Insert job data into the jobs table.
4. Run the FastAPI application:
   uvicorn main:app --reload

