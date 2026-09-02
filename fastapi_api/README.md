FastAPI + SQLite example

Quick start

1. Open a PowerShell in this folder.
2. Create a venv (if not already created):
   python -m venv venv
3. Activate (optional) and install dependencies:
   .\venv\Scripts\python.exe -m pip install --upgrade pip
   .\venv\Scripts\python.exe -m pip install -r requirements.txt
4. Run the app:
   .\run.ps1

Endpoints
- POST /items/        create item (JSON: {"name":"...","description":"..."})
- GET  /items/        list items
- GET  /items/{id}    get item
- PUT  /items/{id}    update item (send full Item JSON)
- DELETE /items/{id}  delete item

Database: SQLite file app.db created in the project directory.
