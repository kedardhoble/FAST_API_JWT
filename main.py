from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import List

app = FastAPI()

SECRET_KEY = "61302344d2ac138cde4d3c9234c96c54ae6d992946fe4d69a7dc386a06fd631a"  # Replace with your own secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# User model for authentication
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


# Example user data
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "password": "$2b$12$E22vUvFK2UjsiAQY6BY0J.x6vZr6Hm9X8/Jfz/uhH2I8noX86.3aG",  # hashed password
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return User(username=username, password=None)


# Function to create access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# OAuth2PasswordBearer for handling token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Route to get token
@app.post("/token")
async def login_for_access_token(form_data: dict):
    user = fake_users_db.get(form_data["username"])
    if user and form_data["password"] == user["password"]:
        token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user["username"]}, expires_delta=token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# Protected route requiring authentication
@app.get("/todos/", response_model=List[str])
async def read_items(current_user: User = Depends(get_current_user)):
    try:
        # Replace this with your actual logic to fetch todos
        todos_data = ["Buy groceries", "Read a book", "Learn FastAPI"]
        return todos_data
    except Exception as e:
        print(f"Exception in read_items: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
