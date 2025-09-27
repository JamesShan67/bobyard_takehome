# Comment System

Minimal Django REST API + HTML/JavaScript frontend.

## Setup

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python load_data.py
python manage.py runserver
```

### Frontend
```bash
cd frontend
python3 -m http.server 3000
```

Open http://localhost:3000

## Features
- List all comments
- Add new comment (author auto-set to "Admin")
- Edit comment text
- Delete comment
- Display author, date, likes, images