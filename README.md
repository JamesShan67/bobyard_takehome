# 

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python load_data.py
python manage.py runserver 3002
```

### Frontend
```bash
cd frontend
python3 -m http.server 3000
```

Open http://localhost:3000

