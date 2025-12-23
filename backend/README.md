# FastAPI Backend

## Setup

1.  Create a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Setup Database:
    - Ensure MySQL is running.
    - Create a database named `app_db`.
    - Update `.env` with your credentials.

4.  Run Migrations:
    ```bash
    alembic upgrade head
    ```

5.  Run App:
    ```bash
    uvicorn app.main:app --reload
    ```

## API Documentation

Go to `http://localhost:8000/docs` for Swagger UI.
