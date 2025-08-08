# Employee Management System

A Django-based Employee Management System with REST APIs, JWT authentication, and data visualization.  
Manage departments, employees, attendance, and performance efficiently through a clean web interface.

---

## Features

- Full CRUD APIs for Departments, Employees, Attendance, and Performance  
- Secure JWT-based authentication for API access  
- Responsive login page styled with Tailwind CSS and widget tweaks  
- Interactive charts showing employee distribution per department using Chart.js  
- Swagger & ReDoc auto-generated API documentation for easy exploration  
- Easily extendable for future enhancements

---

## Prerequisites

- Python 3.10 or higher  
- pip (Python package installer)  
- Virtual environment tool (`venv` or `virtualenv`)  
- PostgreSQL (optional, for production use; SQLite is used by default)

---

## Getting Started: Local Development Setup

Follow these steps to set up and run the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/aluleam/employee-project-internship.git
cd employee-project-internship

2. Create and activate a virtual environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate    
3. Install required Python packages
bash
Copy code
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root and add the following adjust values as needed:

ini
Copy code
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

5. Apply database migrations
bash
Copy code
python manage.py migrate
6. Create an admin/superuser account
bash
Copy code
python manage.py createsuperuser
7. Run the development server
bash
Copy code
python manage.py runserver
8. Access the app
Login page: http://127.0.0.1:8000/accounts/login/

API endpoints: http://127.0.0.1:8000/api/

Swagger API docs: http://127.0.0.1:8000/swagger/

Charts page: http://127.0.0.1:8000/charts/

Using the API
Authentication
Obtain JWT token by sending a POST request with your username and password to:

bash
Copy code
POST /api/token/
Example JSON payload:

json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
Use the returned access token in the header of subsequent requests:

makefile
Copy code
Authorization: Bearer access_token
Refresh tokens via:

swift
Copy code
POST /api/token/refresh/
Example endpoints
List all departments: GET /api/departments/

List employees: GET /api/employees/

View attendance records: GET /api/attendance/

Check performance metrics: GET /api/performance/

All endpoints require JWT authentication except for Swagger docs and login page.

Frontend Overview
Login page uses Tailwind CSS for styling and widget_tweaks for Django form enhancements

Password toggle and loading spinner included for better UX

Chart.js visualizes employee count per department dynamically using API data

.........continue later!!!