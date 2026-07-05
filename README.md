# 🚀 Problem Bank

A Django-based platform where companies can post real-world problems and students can submit innovative solutions.

## 📌 Features

### 👨‍🎓 Student
- Register & Login
- View available problems
- Search & Filter problems
- Submit solutions
- Track submission status

### 🏢 Company
- Company Registration
- Post new problems
- Manage submissions
- Accept/Reject solutions
- Provide feedback

### 🛡️ Admin
- Manage users
- Moderate content
- Manage categories
- Control platform activities

## 🛠️ Tech Stack

- Python
- Django
- SQLite (Development)
- HTML
- CSS
- JavaScript
- Bootstrap

## 📂 Project Structure

```text
Problem-Bank/
│── accounts/
│── problems/
│── submissions/
│── problembank/
│── manage.py
│── requirements.txt
│── README.md
│── .gitignore
```

## ⚙️ Installation

```bash
git clone https://github.com/sukhdevdogiyal/Problem-Bank.git
cd Problem-Bank

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## 📅 Development Roadmap

- [x] Project Setup
- [x] GitHub Setup
- [ ] Authentication
- [ ] Custom User Model
- [ ] Problem Management
- [ ] Solution Submission
- [ ] Dashboard
- [ ] Search & Filter
- [ ] Email Notifications
- [ ] Payment Integration

## 👨‍💻 Author

**Sukhdev Dogiyal**

GitHub: https://github.com/sukhdevdogiyal