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

<img width="1366" height="768" alt="Screenshot (413)" src="https://github.com/user-attachments/assets/483cfcbe-0c3b-4113-b9ef-65bb9d943a69" />

<img width="1366" height="768" alt="Screenshot (403)" src="https://github.com/user-attachments/assets/da09f27f-ff07-4483-9e8a-273be885aa9b" />


<img width="1366" height="768" alt="Screenshot (404)" src="https://github.com/user-attachments/assets/2cbebd7d-59af-4cf5-80af-3c4d451af9f6" />

<img width="1366" height="768" alt="Screenshot (405)" src="https://github.com/user-attachments/assets/fa167594-4abf-4522-85cf-5c81947d5802" />

<img width="1366" height="768" alt="Screenshot (406)" src="https://github.com/user-attachments/assets/afc7b655-758b-4bcc-ac28-d00b700dbb77" />
<img width="1366" height="768" alt="Screenshot (407)" src="https://github.com/user-attachments/assets/815d39d8-2b8d-4058-9e9b-c87109a5b6e6" />
<img width="1366" height="768" alt="Screenshot (408)" src="https://github.com/user-attachments/assets/4a91a61b-f32f-4e18-9070-5127ce401ed2" />
<img width="1366" height="768" alt="Screenshot (409)" src="https://github.com/user-attachments/assets/0839c149-2a5d-4f15-9e93-b3f4110ccda4" />
<img width="1366" height="768" alt="Screenshot (410)" src="https://github.com/user-attachments/assets/68ec5ae7-8890-4fa0-91d4-f92a6455016d" />
<img width="1366" height="768" alt="Screenshot (411)" src="https://github.com/user-attachments/assets/5b9660e5-2c6a-43a4-9998-f8cac58037cd" />
<img width="1366" height="768" alt="Screenshot (412)" src="https://github.com/user-attachments/assets/47327001-9aef-43aa-890e-68957d1b4e6d" />
