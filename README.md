# Student Planner

## Overview
Student Planner is a web-based application designed to help students organize their tasks, notes, and reminders effectively. Built with Django and Tailwind, the platform ensures a seamless and user-friendly experience.

## Features
- **User Authentication**: Register, login, logout, and manage user profiles.
- **Task Management**: Create, update, and track tasks with priority levels and due dates.
- **Notes**: Add personal or task-linked notes for easy reference.
- **Reminders**: Set reminders for tasks to stay on schedule.
- **Responsive UI**: Modern design using Tailwind CSS.
- **Admin Dashboard**: Manage users, tasks, and notes efficiently.
- **Secure Data Handling**: Uses Django’s built-in authentication and security features.

## Project Structure
```
student_planner/  
│── config/           # Main Django project settings  
│── accounts/         # Authentication & User Management  
│── planner/          # Core Student Planner App (Tasks, Schedule, etc.)  
│── notes/            # Notes App  
│── reminders/        # Reminders App  
│── home/             # Landing page and static content  
│── utils/            # Reusable Helper Functions  
│── frontend/         # Templates and Tailwind Setup  
│── manage.py         # Django management script  
│── requirements.txt  # Dependencies  
│── .env              # Environment variables  
│── db.sqlite3        # SQLite database (or PostgreSQL)  
```

## Prerequisites
Ensure you have the following installed before setting up the project:
- Python (3.8+)
- pip (Python package manager)
- virtualenv (optional but recommended)
- Git
- PostgreSQL (if using a production database)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Webwithkhan/student_planner.git
   cd student-planner
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   - Update `.env` with appropriate values.

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
7. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment (Render)
1. Push your code to GitHub.
2. Create a new Render project and connect your repository.
3. Set the following environment variables in Render:
   ```
   SECRET_KEY=<your-secret-key>
   DEBUG=False
   DATABASE_URL=<your-database-url>
   ALLOWED_HOSTS=student-planner.onrender.com
   ```
4. Deploy and test your application.

## Future Implementations
- **Calendar Integration**: Sync tasks and reminders with Google Calendar.
- **Collaboration**: Allow students to share tasks and notes with peers.
- **Mobile Optimization**: Improve UI for mobile responsiveness.
- **Progress Tracking**: Add analytics for task completion and performance insights.
- **Dark Mode**: Implement theme switching for better user experience.
- **AI-based Suggestions**: Recommend study schedules and task prioritization.
- **Offline Mode**: Enable task access without an internet connection.
- **Email & Push Notifications**: Send alerts for upcoming tasks and reminders.
- **Gamification**: Reward users for completing tasks to enhance motivation.

## License
This project is licensed under the MIT License.

## Contributors
- **Khan** - Developer

## Conclusion
Student Planner aims to streamline task and time management for students, ensuring better productivity and organization. With a robust set of features and future improvements planned, the project will continue to evolve to meet student needs. Contributions and feedback are welcome to enhance the platform further.

