# GRADEFLOW

# GradeFlow – Automated academic performance analytics portal


## Project Overview

**GradeFlow** is a web-based Student Marks Management and Analytics System developed using Python, Django, HTML, CSS, and MongoDB. The application helps manage student records, upload marks data through CSV files, analyze academic performance, and generate student reports.

The system provides a dashboard for accessing student information, viewing academic analytics, and generating reports. It uses Django for application logic and request handling, while MongoDB is used for student data management. CSV upload functionality helps simplify the process of importing student marks.


## Objectives

- To maintain student records in a centralized system.
- To simplify student marks management.
- To upload student marks using CSV files.
- To analyze academic performance and calculate relevant statistics.
- To generate student performance reports.
- To provide a dashboard for viewing student data and analytics.
- To improve the efficiency of academic record management.

  

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- MongoDB
- SQLite
- CSV
- Python Threading


  
## Features

-  Student record management
-  Add student details
-  Edit student information
-  View student records
-  User login page
-  CSV file upload module
-  Student marks management
-  Academic analytics dashboard
-  Student performance reports
-  Data validation
-  Report generation module



## Project Structure

gradeflow/
├── gradeflow/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── student/
│   ├── admin.py
│   ├── analytics.py
│   ├── exceptions.py
│   ├── forms.py
│   ├── models.py
│   ├── mongodb.py
│   ├── reports.py
│   ├── serializers.py
│   ├── upload_csv.py
│   ├── urls.py
│   ├── utils.py
│   ├── validators.py
│   └── views.py
├── templates/
│   ├── add_student.html
│   ├── analytics.html
│   ├── dashboard.html
│   ├── edit_student.html
│   ├── login.html
│   ├── report.html
│   ├── student_list.html
│   └── upload.html
├── sample_data/
│   └── student_mark.csv
├── manage.py
├── db.sqlite3
├── .gitignore
└── requirements.txt



## Main Modules

### Student Management

The student management module allows users to add, view, and update student information. Student records are processed through Django views and forms.

### CSV Upload

The CSV upload module imports student marks from a CSV file. The uploaded data can be validated and processed before being stored in the configured database.

### Analytics Dashboard

The analytics module processes student marks and presents academic performance information through a dashboard.

### Report Generation

The report module generates student performance reports using available student records and marks data.

### MongoDB Integration

The  mongodb.py module manages MongoDB connectivity and database operations where configured.

### Data Validation

The validation modules check incoming student data and uploaded CSV files to reduce invalid or incomplete records.


## Installation and Setup

### 1. Clone the Repository

bash
git clone <your-repository-url>
cd gradeflow

### 2. Create a Virtual Environment

bash
python -m venv .venv

### 3. Activate the Virtual Environment

Windows:

bash
.venv\Scripts\activate

### 4. Install Dependencies

bash
pip install django pymongo

If your project has a requirements.txt file, use:

bash
pip install -r requirements.txt


### 5. Configure the Database

Configure the database settings in gradeflow/settings.py and the MongoDB connection in student/mongodb.py, as required by your project.

### 6. Run Database Migrations

bash
python manage.py migrate

### 7. Start the Development Server

bash
python manage.py runserver


### 8. Open the Application

Open your browser and visit:

http://127.0.0.1:8000/



##  Sample CSV Format

The sample_data/student_mark.csv file can contain student information and marks.

Example:

csv
student_id,name,subject,marks
101,Rahul Sharma,Mathematics,85
102,Priya Patil,Science,92
103,Amit Kumar,English,78


The column names must match the format expected by the application's CSV upload code.

##  Expected Outcome

GradeFlow provides a centralized interface for managing student information, importing marks, reviewing academic analytics, and generating performance reports. It helps reduce manual data entry and makes student academic information easier to organize and analyze.


##  Future Enhancements

- Student attendance management
- Grade and percentage calculation
- Subject-wise performance comparisons
- Export reports to PDF or Excel
- Interactive performance charts
- Role-based access for administrators and teachers
- Improved CSV error handling
- Automated report generation

