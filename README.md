![FastApi](./img/0.avif)
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

---

## 7. **Retrieve a Single Todo**

### Step 7.1: Add a GET Endpoint for a Single Todo
Update `main.py` to include a route for retrieving a single todo by its ID:

```python
# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}
```

This code:
1. Loops through the `todos` list to find the todo with the specified `id`.
2. Returns the todo if found, or a message if not found.

> Screenshot: [Updated main.py for Single Todo](./img/12.png)

---

### Step 7.2: Test the Single Todo Endpoint
Using a tool like Postman or cURL, send a `GET` request to `/todos/{id}`:

**Request:**
```
GET http://127.0.0.1:8000/todos/1
```

**Response:**
```json
{
  "todo": {
    "id": 1,
    "item": "Edit a blog post"
  }
}
```

> Screenshot: [GET Single Todo in Postman](./img/13.png)


---


## 8. **Delete a Todo**

### Step 8.1: Add a DELETE Endpoint
Update `main.py` to include a route for deleting a todo by its ID:

```python
# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been DELETED!"}
    return {"message": "No todos found"}
```

This code:
1. Loops through the `todos` list to find the todo with the specified `id`.
2. Deletes the todo if found, or returns a message if not found.

> Screenshot: [Updated main.py for Delete Todo](./img/14.png)

---

### Step 8.2: Test the DELETE Endpoint
Using a tool like Postman or cURL, send a `DELETE` request to `/todos/{id}`:

**Request:**
```
DELETE http://127.0.0.1:8000/todos/1
```

**Response:**
```json
{
  "message": "Todo has been DELETED!"
}
```

> Screenshot: [DELETE Todo in Postman](./img/15.png)

---

### Step 8.3: Verify the Todo Has Been Deleted
Visit the `/todos/{id}` endpoint again to confirm the item has been removed.

**Request:**
```
GET http://127.0.0.1:8000/todos/1
```

**Response:**
```json
{
  "message": "No todos found"
}
```

> Screenshot: [GET after Delete](./img/16.png)

---

## 9. **Update a Todo**

### Step 9.1: Add a PUT Endpoint for Updating a Todo
Update `main.py` to include a route for updating a todo by its ID:

```python
# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todos found to update"}
```

This code:
1. Loops through the `todos` list to find the todo with the specified `id`.
2. Updates the `item` field of the todo object.
3. Returns the updated todo, or a message if not found.

> Screenshot: [Updated main.py for Update Todo](./img/17.png)

---

### Step 9.2: Test the PUT Endpoint
Using a tool like Postman or cURL, send a `PUT` request to `/todos/{id}` with the updated details:

**Request:**
```json
{
  "id": 1,
  "item": "Updated a blog post"
}
```

**Response:**
```json
{
  "todo": {
    "id": 1,
    "item": "Updated a blog post"
  }
}
```

> Screenshot: [PUT Request in Postman](./img/18.png)

---

### Step 9.3: Verify the Updated Todo
Visit the `/todos/{id}` endpoint again to confirm the item has been updated.

**Request:**
```
GET http://127.0.0.1:8000/todos/1
```

**Response:**
```json
{
  "todo": {
    "id": 1,
    "item": "Updated a blog post"
  }
}
```

> Screenshot: [GET after Update](./img/19.png)

---

## Conclusion

In this project, we:
- Set up a FastAPI environment using a virtual environment and installed the necessary dependencies.
- Created a basic FastAPI application that returns JSON responses.
- Added multiple endpoints (`GET`, `POST`, `PUT`, `DELETE`) to handle a todo list.
- Validated input data using Pydantic models.
- Tested all endpoints using Postman, ensuring proper functionality.

### Future Improvements
1. **Database Integration**: Persist todos in a database (e.g., SQLite, PostgreSQL) instead of using an in-memory list.
2. **Authentication**: Add user authentication and authorization to secure endpoints.
3. **Error Handling**: Implement custom error handling for more descriptive responses.
4. **Frontend Integration**: Build a frontend (e.g., React or Vue.js) to interact with the FastAPI backend.
5. **Deployment**: Deploy the API to a cloud provider (e.g., AWS, Heroku) for public access.

This project serves as a foundation for building more complex applications with FastAPI.