# Run the API using the project's virtualenv
$proj = Split-Path -Parent $MyInvocation.MyCommand.Definition
& "$proj\venv\Scripts\python.exe" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
