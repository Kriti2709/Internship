Mini Leave Management System 

■ Overview
This project is a console-based Mini Leave Management System for a startup with 50 employees.
It allows HR to add employees, apply/approve/reject leaves, and track leave balances.
It handles multiple edge cases and can be extended into a web-based or API-driven system.

■■ Setup Instructions
1. Install Python 3.x
2. Save the script as `leave_mgmt.py`
3. Run using:
```bash
python leave_mgmt.py
```

■ Features
- Add Employees (Name, Email, Department, Joining Date)
- Apply for Leave
- Approve/Reject Leave
- View Leave Balance
- List Employees
- 
■ Edge Cases Handled
- Applying for leave before joining date
- Applying for more days than available balance
- Overlapping approved leave requests
- Invalid dates (end date before start date)
- Employee not found
- Invalid leave request index
- 
■ System Design
The system follows a simple layered design:
Frontend (Console Menu / Future Web UI)
↓
Backend (Python Business Logic / APIs)
↓
Database (In-Memory Dictionary → can scale to SQL DB)
Scaling:
- Move from in-memory dict to SQL (Postgres, MySQL)
- Add REST APIs (Flask/Django)
- Use caching for faster access
- Deploy on cloud (AWS/Heroku/Render)
- 
■ Future Improvements
- Database integration (SQLite/Postgres)
- Web frontend (React/Flask)
- Email notifications to employees
- Role-based access (HR vs Employee)
- Cloud deployment with authentication
- 
■ Architecture Diagram
<img width="362" height="416" alt="image" src="https://github.com/user-attachments/assets/cc0898ba-1e4b-49ec-ba5d-b582d9651698" />
