# 🚀 Django Tech Journal

A modern, minimal blog application built using Django featuring a clean UI, admin panel integration, and dynamic blog rendering.

---

## ✨ Features

- 📝 Blog system powered by Django ORM
- 👨‍💻 Admin panel for managing posts
- 🎨 Minimal dark luxury UI
- 📱 Fully responsive layout
- 🗂 Organized app structure
- 🔎 QuerySet-based filtering
- ⚡ Dynamic template rendering

---

## 🛠 Tech Stack

- **Backend:** Django 4.x
- **Frontend:** HTML, CSS
- **Database:** SQLite3
- **Styling:** Custom CSS
- **Admin:** Django Admin Panel

---

## 📂 Project Structure


TechBlog/
│
├── blog/ # Blog app
│ ├── models.py # BlogPost model
│ ├── views.py # QuerySet logic
│ ├── admin.py # Admin configuration
│ ├── urls.py # App routing
│ ├── templates/blog/ # HTML templates
│ └── static/blog/css/ # Custom CSS styling
│
├── techblog/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── db.sqlite3


---

## ⚙️ Installation

1. Clone the repository:


git clone https://github.com/yourusername/django-tech-blog.git


2. Navigate into project folder:


cd django-tech-blog


3. Create virtual environment:


python -m venv venv


4. Activate virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


5. Install dependencies:


pip install -r requirements.txt


6. Run migrations:


python manage.py migrate


7. Start development server:


python manage.py runserver


---

## 🌐 Access the Application

- Home: http://127.0.0.1:8000/
- Blog: http://127.0.0.1:8000/blog/
- Admin: http://127.0.0.1:8000/admin/

---

## 🔐 Admin Login

Create superuser:


python manage.py createsuperuser


Then login via `/admin`.

---

## 📸 Screenshots

_Add screenshots here for better presentation._

---

## 📌 Future Improvements

- Blog detail page
- Slug-based URLs
- Search functionality
- Pagination
- Deployment on Render / Railway

---

## 👤 Author

**Sujal Kava**  
Aspiring Backend Developer 🚀
