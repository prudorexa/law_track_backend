# Law Firm Web Application

## Overview
The Law Firm Web Application is designed to streamline interactions between clients, lawyers, and admins. This full-stack web application uses Django for the backend and React for the frontend, ensuring a robust, scalable, and user-friendly experience.

## Key Features

### User Authentication and Authorization
- **User Roles:**
  - Admin
  - Lawyer
  - Client
- **Functionalities:**
  - User registration and login
  - Password reset
  - Email verification

### User Dashboard
- **Admin Dashboard:**
  - Manage users
  - View reports
  - Monitor system activities
- **Lawyer Dashboard:**
  - View assigned cases
  - Manage schedules
  - Communicate with clients
- **Client Dashboard:**
  - View case status
  - Communicate with assigned lawyers
  - Receive notifications

### Case Management
- Create, update, and delete case details
- Assign lawyers to cases
- Track case progress and status

### Communication
- Messaging system for clients and lawyers
- Notifications for important updates

## Technologies Used
- **Backend:**
  - Django
  - Django REST framework
- **Frontend:**
  - React
  - Tailwind CSS
  - Axios (for making API requests)
- **Database:**
  - SQLite (development)
  - PostgreSQL (production)
- **Authentication:**
  - JSON Web Tokens (JWT)

## Installation

### Backend Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/law-firm-web-app.git
    cd law-firm-web-app/backend
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```

2. **Install the required dependencies:**
    ```bash
    npm install
    ```

3. **Start the React development server:**
    ```bash
    npm start
    ```

## Usage

### Admin Dashboard
- Access the admin dashboard to manage users, view reports, and monitor activities.

### Lawyer Dashboard
- View assigned cases, manage schedules, and communicate with clients.

### Client Dashboard
- View case status, communicate with assigned lawyers, and receive notifications.

## API Endpoints

### Authentication
- `POST /api/auth/login/`
- `POST /api/auth/register/`
- `POST /api/auth/password-reset/`
- `POST /api/auth/verify-email/`

### Cases
- `GET /api/cases/`
- `POST /api/cases/`
- `GET /api/cases/:id/`
- `PUT /api/cases/:id/`
- `DELETE /api/cases/:id/`

### Messages
- `GET /api/messages/`
- `POST /api/messages/`
- `GET /api/messages/:id/`
- `PUT /api/messages/:id/`
- `DELETE /api/messages/:id/`

### Notifications
- `GET /api/notifications/`
- `POST /api/notifications/`
- `GET /api/notifications/:id/`
- `PUT /api/notifications/:id/`
- `DELETE /api/notifications/:id/`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License.

---

For any questions or suggestions, feel free to contact the project maintainer.

