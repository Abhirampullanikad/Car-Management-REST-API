🚗 Car Management System

A Car Management Web Application built with Django and Django REST Framework (DRF).
It provides both a REST API for CRUD operations on cars and a web interface for managing cars (list, create, update, delete).

🔗 Live Demo: Car Management System

📌 Features

🔑 API Endpoints with Django REST Framework

📋 Car list & details view

➕ Add a new car

✏️ Update existing cars

❌ Delete cars

🎨 Simple UI with Django templates & forms

✅ Success/error message handling with Django messages

⚙️ Tech Stack

Backend: Django, Django REST Framework

Frontend: Django Templates, Bootstrap (if used)

Database: SQLite (default) / PostgreSQL (for production)

Deployment: AWS EC2 + Docker


car-management/
│── car/                # Car app (models, views, forms, serializers)
│── templates/          # HTML templates
│── static/             # Static files (CSS, JS, images)
│── car_management/     # Main Django project settings
│── Dockerfile          # Docker config
│── requirements.txt    # Dependencies
│── manage.py


🐳 Docker Setup
Build & Run with Docker
docker build -t car-management .
docker run -d -p 8000:8000 car-management

👨‍💻 Author

Abhiram P
📍 Kerala, India
📧 abhiramppullanikad23@gmail.com
