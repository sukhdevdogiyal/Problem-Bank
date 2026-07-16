# Problem Bank

> A Django-based platform that connects **students** with **companies** by enabling organizations to post real-world problems and allowing students to submit innovative solutions.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-purple?logo=bootstrap)
![Status](https://img.shields.io/badge/Status-Phase%201%20Completed-success)
![License](https://img.shields.io/badge/License-MIT-orange)

</p>

---

# Overview

Problem Bank is a web application that bridges the gap between **students** and **companies**.

Companies can publish real-world challenges, while students can solve them by submitting their ideas, documents, or code. Companies can review submissions, provide feedback, and select the best solutions.

The platform is designed to encourage practical learning, innovation, and industry collaboration.

---

# Features

## Student

- Student Registration & Login
- Student Profile Management
- Browse Available Problems
- Search & Filter Problems
- Submit Solutions
- Track Submission Status
- View Company Feedback

## Company

- Company Registration & Profile
- Post New Problems
- Edit/Delete Problems
- Review Student Submissions
- Accept / Reject Solutions
- Provide Feedback

## Admin

- Manage Users
- Verify Companies
- Manage Problems
- Moderate Content
- Manage Categories
- Monitor Platform Activities

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Django, Python |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Version Control | Git & GitHub |

---

# Database Models

The project currently contains the following models:

- ✅ CustomUser
- ✅ StudentProfile
- ✅ CompanyProfile
- ✅ Problem
- ✅ Solution

Relationships are implemented using the Django ORM.

---

# Project Structure

```text
Problem-Bank/
│
├── accounts/
├── problems/
├── submissions/
├── problembank/
├── templates/
├── static/
├── media/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

### Clone Repository

```bash
git clone https://github.com/sukhdevdogiyal/Problem-Bank.git
```

### Go to Project

```bash
cd Problem-Bank
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Virtual Environment

Windows

```bash
myenv\Scripts\activate
```

Linux / Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# Development Progress

| Phase | Status |
|--------|--------|
| Phase 1 — Database Design | ✅ Completed |
| Phase 2 — Authentication | 🚧 In Progress |
| Phase 3 — Company Module | ⏳ Pending |
| Phase 4 — Student Module | ⏳ Pending |
| Phase 5 — Admin Module | ⏳ Pending |
| Phase 6 — Advanced Features | ⏳ Pending |

---

# Current Progress

## ✅ Completed

- Django Project Setup
- GitHub Repository Setup
- Database Design
- Custom User Model
- Student Profile Model
- Company Profile Model
- Problem Model
- Solution Model

## 🚧 Currently Working

- Authentication System

---

# Future Enhancements

- REST API Integration
- Email Notifications
- AI-based Solution Recommendations
- Payment Gateway Integration
- Real-time Notifications
- Company Verification
- Student Dashboard
- Analytics Dashboard
- Certificates
- Leaderboard
- Discussion Forum

---

# Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

**Sukhdev Dogiyal**

🎓 B.Tech CSE Student

💻 Passionate about Backend Development, Django, and Problem Solving

GitHub: https://github.com/sukhdevdogiyal