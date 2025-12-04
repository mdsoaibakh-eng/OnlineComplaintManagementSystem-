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

<img width="1366" height="768" alt="Screenshot (414)" src="https://github.com/user-attachments/assets/24260a11-ece6-4d6c-b26c-b1eda9a8d8a3" />

<img width="1366" height="768" alt="Screenshot (415)" src="https://github.com/user-attachments/assets/2599d46b-606e-417f-b457-888a584598eb" />
<img width="1366" height="768" alt="Screenshot (416)" src="https://github.com/user-attachments/assets/4a24745c-d5ce-4129-bb03-2cb6b31932d6" />
<img width="1366" height="768" alt="Screenshot (417)" src="https://github.com/user-attachments/assets/700eadbc-7a89-4c02-a179-061d41a1fa72" />
<img width="1366" height="768" alt="Screenshot (418)" src="https://github.com/user-attachments/assets/bb7c9bb1-3f23-4483-a14b-9b051a42f121" />
<img width="1366" height="768" alt="Screenshot (419)" src="https://github.com/user-attachments/assets/c2e3b050-6a07-40a0-baf7-9b4ad306cbaa" />
<img width="1366" height="768" alt="Screenshot (420)" src="https://github.com/user-attachments/assets/8f6f0733-e84d-450f-a178-579e7c3edbbc" />
<img width="1366" height="768" alt="Screenshot (421)" src="https://github.com/user-attachment<img width="1366" height="768" alt="Screenshot (422)" src="https://github.com/user-attachments/assets/a0c81af6-be5c-4677-a491-2fe874998b30" />
s/assets/539aec17-1da9-4d96-84be-3b69d818c146" />
<img width="1366" height="768" alt="Screenshot (423)" src="https://github.com/user-attachments/assets/02822eae-d33f-41b0-b8b4-fd8d86d08e2a" />
<img width="1366" height="768" alt="Screenshot (424)" src="https://github.com/user-attachments/assets/4adc29fc-062c-4a77-9e2b-fa3586899c12" />
<img width="1366" height="768" alt="Screenshot (425)" src="https://github.com/user-attachments/assets/dfca6818-1484-44a6-a576-97f863ab960f" />
