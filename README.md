mysite01 directory = Django Project

mytodolist01 directory = Django Application

# 12/28/2024 UPDATE:

    1 - MySQL server connected as DataBase server.
    
    2 - Login/LogOut Browser-view and authentication added.
    
    3 - Users access level is now managed and each user can only view and manipulate their own data.
    
    4 - JWT token is now added at end point "/api/token/" via POST method.
    

# Project structure
```
.
├── db.sqlite3                       # Database File (SQLite, for development)
├── manage.py                         # Django Project Management Script
├── requirments.txt                           # Dependencies/Requirements File (pip)
├── mysite01                          # Project Directory (settings for the entire project)
│   ├── settings.py                    # Project Settings (database, installed apps, etc.)
│   └── urls.py                        # Project URL Configuration (top-level URL routing)
├── mytodolist01                       # Application Directory (a component of the project)
│   ├── admin.py                       # Admin Interface Customizations
│   ├── apps.py                        # Application Configuration (optional, for app-specific settings)
│   ├── models.py                      # Data Models (database schema definitions)
│   ├── serializer.py                  # Data Serialization (for APIs, converting data types)
│   ├── tests.py                       # Unit Tests and Integration Tests
│   ├── urls.py                        # Application URL Configuration (URL routing for this app)
│   └── views.py                       # Business Logic (functions handling HTTP requests/responses)
```

# TodoList API (DRF Python)

This repository contains a Django REST Framework (DRF) implementation of a simple TodoList API.

## Features

* **Create:** Create new todo items with titles and optional descriptions.
* **Read:** Retrieve a list of all todo items or a single todo item by ID.
* **Update:** Update existing todo items, including title and description.
* **Delete:** Delete individual todo items.
* **Authentication:** Basic authentication is implemented for basic user authorization.

## Technologies

* **Python:** The primary programming language.
* **Django:** A high-level web framework for Python.
* **Django REST Framework (DRF):** A powerful toolkit for building Web APIs.

## Installation
1.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r req.txt
    ```

3.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Start the development server:**

    ```bash
    python manage.py runserver 
    ```



## API Endpoints

This section describes the API endpoints available in this application.

**Tasks**

* **`/tasks/` (GET)**
    * Lists all tasks in the system.
* **`/tasks/<int:pk>/` (GET)**
    * Retrieves a single task with the specified primary key (pk).

**Authentication**

* **`/register/` (POST)**
    * Allows users to register for the application.
* **`/login/` (POST)**
    * Allows users to log in to the application.
* **`/user/` (GET)**
    * Retrieves information about the currently logged-in user.

* This API follows a RESTful design pattern, using HTTP methods (GET, POST, etc.) to perform actions on resources (tasks, users).

**Authentication**

These endpoints require user authentication to access. You'll need to implement a mechanism to obtain and provide authentication credentials (e.g., tokens) when making requests to these endpoints.

This documentation provides a starting point for understanding the API endpoints offered by this application. Refer to the source code in the `views.py` file for more details about the implementation and any additional functionalities.


**Note:** This is a basic example. You can extend this API further by adding features like:

  * **Authorization:** Control access to resources based on user roles or permissions.
  * **Search:** Add search functionality to filter todo items by title or description.
  * **Pagination:** Implement pagination for better performance with large datasets.
  * **Testing:** Write unit and integration tests to ensure code quality.
  * **Deployment:** Explore deployment options like Heroku, AWS, or Docker.
