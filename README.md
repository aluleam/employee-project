Employee Management System - Django Internship Project
Welcome to the Employee Management System — a Django web app to manage employees, departments, attendance, and performance with easy-to-use APIs and interactive charts.

🔥 What This Website Does
Manage employees, departments, attendance records, and performance reviews.

Secure access with token-based login (JWT).

Explore and test APIs via built-in Swagger UI.

Visualize employee data with charts (e.g., employees per department).

Seed your database with fake data to get started quickly.

Fully tested APIs with unit tests covering employees, departments, attendance, and performance.

⚙️ How to Run It Locally
Clone & Setup:
bash
Copy code
git clone <your-repo-url>
cd employee-project-internship
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Heads up:
If you get warnings about pkg_resources or package install errors, run:

bash
Copy code
pip install --upgrade setuptools
Configure environment variables:
Copy .env.example to .env and fill in your database and secret keys.

Run migrations & seed data:
bash
Copy code
python manage.py migrate
python manage.py seed_data
Start the server:
bash
Copy code
python manage.py runserver
🌐 Accessing the Website & APIs
Visit homepage or frontend at:
http://127.0.0.1:8000/

API Root (JSON responses):
http://127.0.0.1:8000/api/

Swagger UI for API docs & testing:
http://127.0.0.1:8000/swagger/

Charts page (if enabled):
http://127.0.0.1:8000/charts/

🔐 Authentication Notes
The API requires JWT token authentication.

Tokens expire; if you get “Authentication credentials were not provided” errors, log in again for a new token.

Use Swagger UI’s Authorize button to enter your token for easy API testing.

📋 How to Test Everything
Use Swagger UI for interactive API testing.

Use curl or Postman with your Bearer token to test endpoints:

bash
Copy code
curl -H "Authorization: Bearer <your-token>" http://127.0.0.1:8000/api/employees/
Supported APIs include CRUD operations for:

Employees

Departments

Attendance

Performance

Filtering and pagination are supported via query parameters.

🧪 Unit Testing
Unit tests cover models and APIs for Employees, Departments, Attendance, and Performance.

Run tests locally with:

bash
Copy code
python manage.py test employees
python manage.py test attendance
Tests check authentication, list/retrieve, create, update, partial update, and delete endpoints.

⚠️ Common Gotchas & Troubleshooting
Token expired? Re-authenticate to get a new JWT token.

Package warnings/errors? Upgrade setuptools:

bash
Copy code
pip install --upgrade setuptools
Database issues? Ensure PostgreSQL is running and .env config is correct.

Docker: Docker setup was not finalized — please run locally.

🧰 Handy Management Commands
python manage.py seed_data — populate the database with dummy data for testing.

This web app delivers a fully functional Employee Management System with secure APIs and clear visualizations. Though Docker and deployment are pending, it’s simple to run and test locally. Dive in, explore the APIs, and check out the charts!