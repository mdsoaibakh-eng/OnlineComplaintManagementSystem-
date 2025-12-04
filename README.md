Online Complaint Registration System

A web-based platform built using Flask, Jinja2, Bootstrap, and SQLAlchemy that allows students or users to submit complaints and enables admins to manage and update their status efficiently.

Features

User Registration and Login

Admin Registration and Login

User Dashboard with complaint history

File new complaints with categories

Admin Dashboard to view and filter complaints

Update complaint status with logs

Status timeline for each complaint

Secure password hashing

Session-based authentication

SQLite database (default)

Tech Stack

Frontend

HTML + Jinja2

Bootstrap 5

Custom CSS

Backend

Python Flask

SQLAlchemy ORM

SQLite (default)

Project Structure
project/
│── app.py
│── models.py
│── .env
│── site.db
│── requirements.txt
│── /templates
│      ├── base.html
│      ├── index.html
│      ├── admin_login.html
│      ├── admin_register.html
│      ├── admin_dashboard.html
│      ├── admin_complaint_detail.html
│      ├── user_login.html
│      ├── user_register.html
│      ├── user_dashboard.html
│      ├── file_complaint.html
│      ├── complaint_detail.html
│      └── 404.html
│── /static
       └── css/style.css

Environment Variables

Create a .env file:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=123456
DATABASE_URL=sqlite:///site.db

How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run the application
python app.py  / flask run

3. Access in browser
http://127.0.0.1:5000

Default Categories Added Automatically

Academic

Infrastructure

Hostel

Canteen

Other

Admin Features

Login and Register

View all complaints

Filter by status

Update status

Add comments

Status log history

User Features

Register and login

File complaints

Track complaint progress

See full details

License

This project is created and managed by Soaib Sheikh. You may modify it for learning or personal use.

