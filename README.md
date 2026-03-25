# Django Blog Management System

A web-based Blog Management System built with Django that allows users to register, log in, create blog posts, view blog details, update existing posts, and delete blogs. This project demonstrates core Django concepts such as authentication, models, forms, CRUD operations, template rendering, and user-based access control.

---

##  Project Overview

This project is a **Django-based Blog Website** developed as a practical assignment to understand backend web development and user authentication.

The application allows authenticated users to manage blog posts efficiently through a clean and structured workflow. Each blog contains important fields such as title, slug, content, status, author, and timestamps.

This project is useful for learning how a complete Django web application works from **database to frontend templates**.

---

##  Key Features

- **User Signup**
- **User Login / Logout**
- **Create New Blog Post**
- **Display All Blogs**
- **View Individual Blog Details**
- **Edit Existing Blog**
- **Delete Blog**
- **User Profile Page**
- **Author-based Blog Management**
- **Draft / Published Blog Status**
- **Automatic Created & Updated Date Tracking**

---

##  Technologies Used

- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite**
- **Django Authentication System**

---

##  Concepts Implemented

This project includes practical implementation of:

- Django Models
- Django Views
- URL Routing
- Django Forms
- CRUD Operations
- Authentication & Authorization
- Template Rendering
- Database Integration
- User-based Access Control

---

##  Project Structure

```bash
blog_project/
│── blog/
│   │── migrations/
│   │── templates/
│   │   ├── blog_list.html
│   │   ├── blog_detail.html
│   │   ├── create_blog.html
│   │   ├── edit_blog.html
│   │   └── profile.html
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── urls.py
│   │── views.py
│
│── blog_project/
│   │── settings.py
│   │── urls.py
│   │── asgi.py
│   │── wsgi.py
│
│── templates/
│   └── registration/
│       ├── login.html
│       └── signup.html
│
│── db.sqlite3
│── manage.py
│── README.md
Database Model
Blog Model

The Blog model contains the following fields:

title → Blog title
slug → Unique slug for each blog
content → Main blog content
created_date → Automatically stores creation date
updated_at → Automatically stores updated date
author → Linked authenticated user
status → Draft or Published
🔐 Authentication System

This project uses Django’s built-in authentication system for:

User Registration
User Login
User Logout

Only logged-in users can:

Create blogs
Edit their own blogs
Delete their own blogs
Access profile page

This ensures basic authorization and secure user-specific blog management.

* How to Run This Project

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/Arooj-Fatima/django-blog-app.git
2️⃣ Move to Project Folder
cd django-blog-app
3️⃣ Go Inside the Django Project Directory
cd Blog_project/blog_project
3️⃣ Install Django
pip install django
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Run the Development Server
python manage.py runserver
6️⃣ Open in Browser
http://127.0.0.1:8000/
 **Login or Create an Account

After opening the project in your browser:

Visit the Login Page at /
Or create a new account at /signup/
📄 Available Pages / Routes

The project includes the following main pages:

Login Page
Signup Page
Blog List Page
Blog Detail Page
Create Blog Page
Edit Blog Page
Profile Page
* Learning Objectives

The main goal of this project was to practice:

Building a complete Django application
Working with models and forms
Managing user authentication
Performing CRUD operations
Handling dynamic content in templates
Structuring a Django project professionally
* Future Improvements

This project can be improved further by adding:

Search functionality
Blog categories / tags
Blog comments section
Rich text editor
Pagination
Image upload support
Better UI/UX styling
Admin dashboard enhancements
* Author

Arooj Fatima
Student | Learning Python, Django, Web Development & Backend Systems
