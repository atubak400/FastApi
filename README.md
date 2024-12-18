# FastAPI Project Documentation

This document outlines the step-by-step process for setting up and running a basic **FastAPI** project. It serves as a reference for others who wish to replicate this setup.

---

## 1. **Setup the Project Environment**

### Step 1.1: Create a Virtual Environment
To ensure dependencies are managed cleanly, create a virtual environment.

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

> Screenshot: [Terminal with environment setup](./img/1.png)

---

### Step 1.2: Install FastAPI and Uvicorn
FastAPI is the framework, and **Uvicorn** serves as the ASGI server.

Run the following commands:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

This installs the required dependencies:
- `fastapi` for API development
- `uvicorn` for running the API server

> Screenshot: [Dependencies Installation](./img/1.png)

---

## 2. **Create the FastAPI App**

### Step 2.1: Project Structure
The project structure is simple for this example:
```
FastAPI
│-- main.py          # The main FastAPI app file
│-- venv/            # Virtual environment folder
│-- __pycache__/     # Auto-generated cache files
│-- img/             # Images or assets (optional)
│-- README.md        # Documentation
```

### Step 2.2: Write the Code
In the `main.py` file, write a simple FastAPI app that returns a JSON response:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This code:
1. Creates a FastAPI app instance.
2. Defines a route at `/` that returns a JSON response `{"message": "Hello World"}`.

> Screenshot: [main.py Code](./img/2.png)

---

## 3. **Run the FastAPI Server**

Use **Uvicorn** to start the FastAPI server. Run the following command:

```bash
uvicorn main:app --reload
```

- `main` refers to the file name (`main.py`).
- `app` is the FastAPI instance.
- `--reload` enables live reloading for development.

**Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

> Screenshot: [Server Running](./img/3.png)

---

## 4. **Test the FastAPI App**

1. Open a browser and visit:
   ```
   http://127.0.0.1:8000
   ```
2. You should see the JSON response:
   ```json
   {"message": "Hello World"}
   ```

> Screenshot: [API Response](./img/4.png)

---

## 5. **Next Steps**
To further develop this project:
1. Add more routes (e.g., POST, PUT, DELETE).
2. Integrate a database (SQLite, PostgreSQL, etc.).
3. Add input validation using Pydantic models.
4. Use Swagger UI (`/docs`) for API testing.

---

## Conclusion
You have successfully set up and run a basic FastAPI application. This process covered:
- Creating a virtual environment.
- Installing FastAPI and Uvicorn.
- Writing and running a basic API endpoint.

For further learning, refer to the official [FastAPI documentation](https://fastapi.tiangolo.com).
