# FastAPI Authentication with JWT

This project demonstrates a basic authentication setup using FastAPI and JWT (JSON Web Tokens). It includes token generation, password hashing, and protected routes requiring authentication.

## Features

- **Token-based Authentication:** Uses JWT for secure authentication.
- **Password Hashing:** Utilizes `passlib` for password hashing.
- **Dependency Injection:** Demonstrates the use of FastAPI's dependency injection for getting the current user from the token.
- **Protected Routes:** Includes an example of a protected route that requires authentication.

## Getting Started

1. **Install Dependencies:**
   ```bash
   pip install fastapi[all] passlib python-jose uvicorn
   ```
# FastAPI Authentication with JWT

## Run the Application

```bash
uvicorn main:app --reload
```
# FastAPI Authentication with JWT

The application will be running at [http://127.0.0.1:8001](http://127.0.0.1:8001).

## Obtain an Access Token

Use the `/token` endpoint to obtain an access token by providing valid credentials.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8001/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=testuser&password=testpassword'
  ```
  Replace testuser and testpassword with your desired credentials.
  Access Protected Route:
Use the obtained access token to access the protected route.
```bash
curl -X 'GET' \
  'http://127.0.0.1:8001/todos/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
  ```
Replace YOUR_ACCESS_TOKEN with the actual access token obtained in step 3.

**Project Structure**

- main.py: Contains the main FastAPI application code.
- requirements.txt: Lists the project dependencies.

**Dependencies**

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [passlib](https://pypi.org/project/passlib/): A password hashing library for Python, which provides cross-platform implementations of over 30 password hashing schemes.
- [python-jose](https://pypi.org/project/python-jose/): A JOSE implementation in Python.

**Contributors**

------------
Kedar
