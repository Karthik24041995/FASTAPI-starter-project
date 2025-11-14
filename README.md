# FASTAPI-starter-project

# FastAPI Intermediate Project

This project demonstrates a moderately complex FastAPI structure with:
- Modular routers (users, items)
- In-memory DB with CRUD (poised for upgrade)
- Dependency injection examples
- Pydantic schemas & validation
- Environment-based settings management

## Run Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for API docs.

## Run tests
```bash
pytest
```
