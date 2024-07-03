# Task Management RestAPI

This is a Task Management Application that allows users to create, read, update, and delete tasks. The application also includes user authentication features such as registration, login, and logout.

## Features

- User Registration
- User Login
- User Logout
- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks

## Technology Stack

- Backend: Django REST framework
- Frontend: HTML, CSS, JavaScript (jQuery)
- Authentication: JWT (JSON Web Tokens)

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Node.js (for frontend development)

### Backend Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-repo/task-management-app.git
    cd task-management-app
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Server**:
    ```sh
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the Frontend Directory**:
    ```sh
    cd frontend
    ```

2. **Open `index.html`** in a browser to access the application.

## API Endpoints

### Authentication Endpoints

- **Register User**: `POST /api/accounts/register/`
    - Request Body:
      ```json
      {
          "username": "testuser",
          "password": "testpassword"
      }
      ```

- **Login User**: `POST /api/accounts/login/`
    - Request Body:
      ```json
      {
          "username": "testuser",
          "password": "testpassword"
      }
      ```
    - Response:
      ```json
      {
          "refresh": "refresh_token",
          "access": "access_token"
      }
      ```

- **Logout User**: `POST /api/accounts/logout/`
    - Request Body:
      ```json
      {
          "refresh_token": "refresh_token"
      }
      ```

### Task Endpoints

- **Retrieve All Tasks**: `GET /api/tasks/`
    - Headers:
      ```json
      {
          "Authorization": "Bearer access_token"
      }
      ```

- **Create a New Task**: `POST /api/tasks/`
    - Headers:
      ```json
      {
          "Authorization": "Bearer access_token",
          "Content-Type": "application/json"
      }
      ```
    - Request Body:
      ```json
      {
          "title": "Test Task",
          "description": "This is a test task",
          "due_date": "2024-07-01"
      }
      ```

- **Retrieve a Single Task**: `GET /api/tasks/{id}/`
    - Headers:
      ```json
      {
          "Authorization": "Bearer access_token"
      }
      ```

- **Update an Existing Task**: `PUT /api/tasks/{id}/`
    - Headers:
      ```json
      {
          "Authorization": "Bearer access_token",
          "Content-Type": "application/json"
      }
      ```
    - Request Body:
      ```json
      {
          "title": "Updated Task",
          "description": "This is an updated test task",
          "due_date": "2024-07-01"
      }
      ```

- **Delete a Task**: `DELETE /api/tasks/{id}/`
    - Headers:
      ```json
      {
          "Authorization": "Bearer access_token"
      }
      ```

## Frontend Pages

- **Landing Page**: `index.html`
    - Displays a list of tasks.
    - Form to add new tasks.
    - Buttons to edit and delete tasks.

- **Login Page**: `login.html`
    - Form to log in users.

- **Register Page**: `register.html`
    - Form to register new users.

## Authentication Flow

1. **User Registration**:
    - User navigates to the registration page and fills out the registration form.
    - On successful registration, the user is redirected to the login page.

2. **User Login**:
    - User navigates to the login page and fills out the login form.
    - On successful login, JWT tokens (access and refresh) are stored in local storage.
    - User is redirected to the landing page.

3. **User Logout**:
    - User clicks the logout button.
    - JWT tokens are removed from local storage.
    - User is redirected to the login page.

## Notes

- Ensure that the backend server is running before accessing the frontend pages.
- Use tools like Postman to test API endpoints during development.




