# main.py

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User, UpdateUser

from uuid import UUID


app=FastAPI()


# this the in-memory database
db: List[User]=[
    User(
        id=uuid4(),
        first_name="john",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
        ),

    User(
        id=uuid4(),
        first_name="jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="anyane",
        last_name="shankar",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="sam",
        last_name="Dinces",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="kindy",
        last_name="grpy",
        gender=Gender.female,
        roles=[Role.user,Role.admin],
    ),
]

# http://localhost:8000/redoc - redoc provides the Endpoints

@app.get("/")
async def root():
    return {"greeting":"Hello world"}


# This code defines the endpoint /api/v1/users,
# and creates an async function, get_users, which returns all the contents of the database, db
@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user:User):
    db.append(user)
    return {"id":user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
        return
    raise HTTPException(
        status_code=404,detail=f"Delete User Failed ,id {id} not Found"
    )


@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
 for user in db:
    if user.id == id:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.roles is not None:
            user.roles = user_update.roles
 return user.id
 raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")

# def calculate_price(beef_price:int,meal_price:int)-> int:
#     total_price: int = beef_price+meal_price
#     return total_price
#
# print("total Price from the Pydantic  Models : " , calculate_price(75,78))
