# Django Authorization Module with Docker

This project is a Django-based authorization module that includes a signup page, login page, and an about page with email verification. The setup uses local database but any other RDBMS can also be substituted as per requirement.

## Features

- User signup with fields: First Name, Last Name, Mobile, Email ID
- Email verification before allowing login
- Login and logout functionality
- Protected about page accessible only after login

## Prerequisites

- Python

## Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/atharva26k/Django-Authentication-with-Email-Verification.git
cd authorization_module
```

### Step 2: Run the server

python manage.py runserver


### Step 3: Open Url in browser.

http://127.0.0.1:8000/login/
http://localhost:8000/login/

