# 🏢 Employee Management System - Django Internship Project


Welcome to the Employee Management System — a simple yet powerful Django app that helps you keep track of your team, their departments, attendance, and performance. It comes with easy-to-use APIs and handy charts to give you quick insights, all built to make HR tasks less of a headache.

## ✨ Key Features
- **Employee & Department Management**  
- **Attendance & Performance Tracking**  
- **JWT Token Authentication**  
- **Interactive Data Visualization**  
- **Fully Tested APIs** (Employees, Departments, Attendance, Performance)
- **Database Seeding** for quick setup
- **Built-in Swagger UI** for API documentation

---

## Installation & Setup

### 1. Clone & Setup Environment
```bash
git clone <https://github.com/aluleam/employee-project-internship>
cd employee-project-internship

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Heads up:
If you get warnings about pkg_resources or package install errors, please run:

```
pip install --upgrade setuptools
```

Configure environment variables:
Copy .env.example to .env and fill in your database and secret keys.

Run migrations & seed data:
```
python manage.py migrate
python manage.py seed_data
```
Start the server:
```
python manage.py runserver
```

Accessing the Website & APIs
Visit homepage or frontend at:
```
http://127.0.0.1:8000/
```

API Root (JSON responses):
```
http://127.0.0.1:8000/api/
```

Swagger UI for API docs & testing:
```
http://127.0.0.1:8000/swagger/
```

Charts page (if enabled):
```
http://127.0.0.1:8000/charts/
```

## Authentication

### JWT Token Authentication
The API uses JWT (JSON Web Token) authentication for secure access. 

**Key Notes:**
- Tokens have expiration time for security
- If you see _"Authentication credentials were not provided"_:
  1. Your token has expired
  2. You need to re-authenticate
- 🔄 Get new tokens at: `http://localhost:8000/api/token/`

### Using Swagger UI
1. Visit `/swagger/`
2. Click **"Authorize"** button
3. Enter your token:  
   `Bearer <your_token>`
4. All API requests will now include your token automatically

## Swagger Authentication

## Testing the System

### 1. Using Swagger UI
- Interactive API documentation at `/swagger/`
- Test endpoints directly in browser
- Automatic token inclusion after authorization
- See request/response formats

### 2. Using cURL
```bash
# Get token
curl -X POST -H "Content-Type: application/json" \
-d '{"username":"youruser", "password":"yourpass"}' \
http://localhost:8000/api/token/

# List employees
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
http://localhost:8000/api/employees/

# Filter by department
curl -H "Authorization: Bearer your_token" \
"http://localhost:8000/api/employees/?department=HR"

# Create new employee
curl -X POST -H "Authorization: Bearer your_token" \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "department": 1, "position": "Developer"}' \
http://localhost:8000/api/employees/

```

This web app delivers a fully functional Employee Management System with secure APIs and clear visualizations.
Though Docker and deployment are pending, it’s simple to run and test locally.
Dive in, explore the APIs, and check out the charts!

Thank you!
