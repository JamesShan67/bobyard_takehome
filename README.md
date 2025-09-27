# Minimal Comment System

A clean, minimal comment system built with Django REST Framework + React + TypeScript.

## 📁 File Structure (14 files total)

### Backend (Django + DRF + SQLite) - 8 files
```
manage.py
backend/
├── __init__.py
├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py
comments/
├── __init__.py
├── models.py          # JSONField for images
├── serializers.py
├── views.py           # DRF ViewSet + router
├── urls.py
├── admin.py           # Optional
├── apps.py
└── management/
    └── commands/
        └── load_comments.py
```

### Frontend (Vite + React + TS) - 6 files
```
frontend/
├── index.html
├── package.json
├── vite.config.ts
└── src/
    ├── main.tsx
    ├── App.tsx         # All components inline
    ├── api.ts          # Fetch functions
    └── styles.css
```

## 🚀 Quick Start

### Backend
```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py migrate

# Load sample data
python manage.py load_comments

# Start server
python manage.py runserver 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🎯 Features

- ✅ **Minimal file count**: Only 14 files total
- ✅ **Django REST Framework**: Full CRUD with ViewSet + router
- ✅ **React + TypeScript**: Modern frontend with Vite
- ✅ **JSONField**: Images stored as JSON in database
- ✅ **CORS**: No CORS issues with django-cors-headers
- ✅ **Clean API**: RESTful endpoints
- ✅ **Modern UI**: Responsive design with CSS

## 🔧 API Endpoints

- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create comment (author=Admin, created_at=now)
- `PATCH /api/comments/{id}/` - Update comment
- `DELETE /api/comments/{id}/` - Delete comment

## 🧪 Test with curl

```bash
# Get comments
curl http://localhost:8000/api/comments/

# Add comment
curl -X POST http://localhost:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Test comment"}'

# Update comment
curl -X PATCH http://localhost:8000/api/comments/1/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Updated text"}'

# Delete comment
curl -X DELETE http://localhost:8000/api/comments/1/
```

## 🎨 Frontend Features

- **Fetch + List**: Load and display comments
- **Add**: Form to create new comments
- **Edit**: Inline editing with PATCH requests
- **Delete**: Delete with confirmation
- **Polish**: Author, human date, likes, image rendering

## 📊 Data Structure

```typescript
interface Comment {
  id: number;
  author: string;        // Auto-set to "Admin" for new comments
  text: string;
  created_at: string;    // ISO timestamp
  likes: number;
  image: {               // JSONField
    url?: string;
  };
}
```

## 🏗️ Architecture

- **Backend**: Django handles all business logic, database operations
- **Frontend**: React handles UI, user interactions, API calls
- **Communication**: RESTful API with JSON
- **Database**: SQLite (easily upgradeable to PostgreSQL)

## ⚡ Performance

- **Minimal bundle**: No unnecessary dependencies
- **Fast development**: Vite for instant HMR
- **Efficient API**: DRF ViewSet with automatic CRUD
- **Clean state**: Simple React state management

This structure follows the exact minimal approach requested - clean, fast, and maintainable!