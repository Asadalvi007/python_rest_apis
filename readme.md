# Django API Project

This project is a Django-based API designed to manage departments and employees. It allows CRUD (Create, Read, Update, Delete) operations for both entities through HTTP requests.

## Table of Contents
- [Django API Project](#django-api-project)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)

---

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- A virtual environment manager (optional but recommended)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone 
   cd DJANGOAPI
2. **Set up a virtual environment**:
   ```
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install dependencies**:
   ```bash
    pip install -r requirements.txt
    If you don’t have a requirements.txt file, make sure to install Django:
    ```
    pip install django
4. **Migrate the database**: Before running the server, ensure the database is migrated:

    ```bash
    python manage.py migrate

5. **Create a superuser** (optional): If you want to access the Django admin panel, create a superuser:
    ```bash
    python manage.py createsuperuser

# Running the Project
1. Start the development server:

    ```bash
    python manage.py runserver
2. The API will be available at http://127.0.0.1:8000/.
