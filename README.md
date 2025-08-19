#!/usr/bin/env bash
set -euo pipefail

### ====== CONFIG: EDIT THESE ====== ###
# Your live demo URL
LIVE_URL="http://54.242.252.179:8000"

# Your GitHub repo URL (SSH or HTTPS). Example:
# GITHUB_REPO_SSH="git@github.com:your-username/car-management.git"
# or
# GITHUB_REPO_SSH="https://github.com/your-username/car-management.git"
GITHUB_REPO_SSH="git@github.com:your-username/car-management.git"

# Your display name and links
AUTHOR_NAME="Abhiram P"
AUTHOR_LOCATION="Kerala, India"
AUTHOR_EMAIL="abhiramppullanikad23@gmail.com"
AUTHOR_LINKEDIN="https://www.linkedin.com"
AUTHOR_GITHUB="https://github.com/your-username"
### ================================= ###

echo "➡️  Writing README.md ..."
cat > README.md <<EOF
# 🚗 Car Management System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![DRF](https://img.shields.io/badge/DRF-REST--Framework-red?logo=django)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?logo=google-chrome)](${LIVE_URL})

A **Car Management Web Application** built with **Django** and **Django REST Framework (DRF)**.  
It provides both a **REST API** for CRUD operations on cars and a **web interface** for managing cars (list, create, update, delete).  

🔗 **Live Demo:** [Car Management System](${LIVE_URL})

---

## 📌 Features
- 🔑 API Endpoints with Django REST Framework  
- 📋 Car list & details view  
- ➕ Add a new car  
- ✏️ Update existing cars  
- ❌ Delete cars  
- 🎨 Simple UI with Django templates & forms  
- ✅ Success/error message handling with Django messages  

---

## ⚙️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Frontend:** Django Templates
- **Database:** SQLite (default)  
- **Deployment:** AWS EC2 + Docker  

---


## 🚀 Getting Started

### 1️⃣ Clone the Repository
\`\`\`bash
git clone https://github.com/your-username/car-management.git
cd car-management
\`\`\`

### 2️⃣ Create Virtual Environment & Install Dependencies
\`\`\`bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
\`\`\`

### 3️⃣ Run Migrations
\`\`\`bash
python manage.py migrate
\`\`\`

### 4️⃣ Run Development Server
\`\`\`bash
python manage.py runserver
\`\`\`
Visit **http://127.0.0.1:8000/**

---

## 📡 API Endpoints

| Method | Endpoint        | Description       |
|--------|-----------------|-------------------|
| GET    | \`/cars/\`        | List all cars      |
| POST   | \`/cars/\`        | Create a new car   |
| GET    | \`/cars/<id>/\`   | Retrieve a car     |
| PUT    | \`/cars/<id>/\`   | Update a car       |
| DELETE | \`/cars/<id>/\`   | Delete a car       |



## 🐳 Docker Setup

### Build & Run with Docker
\`\`\`bash
docker build -t car-management .
docker run -d -p 8000:8000 car-management
\`\`\`

---


## 👨‍💻 Author
**${Abhiram}**  
📍 ${kerala,palakkad}  
📧 ${abhiramppullanikad23@gmail.com}  


# Ensure git repo exists
if [ ! -d .git ]; then
  echo "➡️  Initializing new git repository ..."
  git init
fi

# Set default branch to main if not already
current_branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"
if [ "\$current_branch" != "main" ]; then
  echo "➡️  Setting default branch to 'main' ..."
  git checkout -B main
fi

# Add remote origin if missing or update it
if git remote get-url origin >/dev/null 2>&1; then
  echo "ℹ️  Remote 'origin' already set."
else
  echo "➡️  Adding remote 'origin' -> \$GITHUB_REPO_SSH"
  git remote add origin "\$GITHUB_REPO_SSH"
fi

echo "➡️  Staging and committing README.md ..."
git add README.md
git commit -m "docs: add polished README with badges and live demo"

echo "➡️  Pushing to GitHub ..."
git push -u origin main

