from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {
        "name": "Charles",
        "linkedin": "https://www.linkedin.com/charles-osoti",
        "age": 78,
        "role": "AI Systems Engineer"
    }
}

# Base Pydantic Models
class User(BaseModel):
    name: str
    linkedin:str
    age: int
    role:str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    linkedin: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Crash Course"}

@app.get("/users/{user_id}")
def get_user(user_id:int =  Path(..., description="The ID of a user", gt=0)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not Found")
    return users[user_id]

# Create User
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id:int, user:User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user_id] = user.dict()
    return user

# Update User
@app.put("/users/{user_id}")
def update_user(user_id:int, user:UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=400, detail="User is not here")
    
    current_user = users[user_id]
    if user.name is not None:
        current_user["name"] = user.name
    if user.linkedin is not None:
        current_user["linkedin"] = user.linkedin
    if user.age is not None:
        current_user["age"] = user.age
    if user.role is not None:
        current_user["role"] = user.role
    return current_user

# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User is not here")

    deleted_user = users.pop(user_id)
    return {"message": "User has been deleted successfully", "deleted_user":deleted_user}

# Search for a user
@app.get("/users/search/")
def search_by_name(name: Optional[str] = None):
    if not name:
        return {"message": "Name parameter is required"}

    for user in users.values():
        if user["name"] == name:
            return user

    raise HTTPException(status_code=404, detail="User not found!")
