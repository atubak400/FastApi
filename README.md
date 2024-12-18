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
   { "message": "Hello World" }
   ```

> Screenshot: [API Response](./img/4.png)

---

## 5. **Add a /todos Route**

### Step 5.1: Update the Code for a `/todos` Endpoint

In `main.py`, add the following code to create a `GET` endpoint at `/todos`. This endpoint will return an empty list of todos for now.

```python
todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}
```

This code:

- Initializes an empty list named `todos`.
- Defines a new route `/todos` that returns the current list of todos in JSON format.

> Screenshot: [Updated main.py](./img/5.png)

---

### Step 5.2: Test the `/todos` Route

Run the FastAPI server again if it's not already running:

```bash
uvicorn main:app --reload
```

Visit the following URL:

```
http://127.0.0.1:8000/todos
```

**Output:**

```json
{ "todos": [] }
```

This confirms that the `/todos` route is working correctly and returning an empty list.

> Screenshot: [Response for /todos](./img/6.png)

---

## 6. **Add a Pydantic Model for Todo Items**

### Step 6.1: Create the Pydantic Model
Create a new file `models.py` and define a `Todo` model using Pydantic.

```python
from pydantic import BaseModel

# Pydantic model for a Todo item
class Todo(BaseModel):
    id: int
    item: str
```

This model ensures validation and type enforcement for incoming `Todo` objects.

> Screenshot: [Pydantic Model](/img/7.png)

---

### Step 6.2: Update `main.py` to Accept POST Requests
In `main.py`, import the `Todo` model and add a `POST` endpoint for creating todos.

```python
from models import Todo

# Create a todos
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}
```

This code:
1. Adds a new `Todo` item to the `todos` list.
2. Returns a confirmation message.

> Screenshot: [Updated main.py with POST Endpoint](/img/8.png)

---

### Step 6.3: Test the POST `/todos` Route
Using a tool like Postman or cURL, send a `POST` request with a JSON body:

**Request:**
```json
{
  "id": 1,
  "item": "Edit a blog post"
}
```

**Response:**
```json
{
  "message": "Todo has been added"
}
```

> Screenshot: [POST Request in Postman](/img/9.png)

---

### Step 6.4: Verify the New Todo Item
Visit the `/todos` endpoint again to confirm the item was added.

**Output:**
```json
{
  "todos": [
    {
      "id": 1,
      "item": "Edit a blog post"
    }
  ]
}
```

> Screenshot: [Updated /Postman todos Response](./img/10.png) and [Updated /Browser todos Response](./img/11.png)
