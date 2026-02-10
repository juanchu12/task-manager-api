# ✅ Task Manager API

Simple REST API built with FastAPI to manage tasks.
Supports full CRUD operations using SQLite as storage.

## 🚀 Features

- Create, read, update, delete tasks
- SQLite database (no configuration needed)
- Automatic API documentation (Swagger / OpenAPI)
- Clean and simple project structure

## 📁 Project Structure

task-manager-api/
├── app/
├── database/
├── tests/
├── requirements.txt
└── README.md

## 🔧 Installation

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
```

## ▶️ Run the API
```bash
uvicorn app.main:app --reload
API will be available at:
http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
OpenAPI JSON: http://127.0.0.1:8000/openapi.json
```

## 📌 Example API Requests
Create a task
``` bash
curl -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d '{
  "title": "Learn FastAPI",
  "description": "Build a REST API project"
}'
```

Get all tasks
```bash
curl http://127.0.0.1:8000/tasks
```

Get a task by ID
```bash
curl http://127.0.0.1:8000/tasks/1
```

Update a task
```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
-H "Content-Type: application/json" \
-d '{
  "title": "Learn FastAPI",
  "description": "Updated description",
  "completed": true
}'
```

Delete a task
```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

## 📝 License
Open-source project for learning and portfolio purposes.