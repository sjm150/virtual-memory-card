from fastapi import FastAPI, HTTPException
from bson import ObjectId
from model import PostModel
from db import db

app = FastAPI()

@app.post("/posts")
async def create_post(post: PostModel):
    result = await db.posts.insert_one(post.dict())
    return {"id": str(result.inserted_id)}

@app.get("/posts/{id}")
async def get_post(id: str):
    post = await db.posts.find_one({"_id": ObjectId(id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post["_id"] = str(post["_id"])
    return post

@app.put("/posts/{id}")
async def update_post(id: str, post: PostModel):
    result = await db.posts.update_one({"_id": ObjectId(id)}, {"$set": post.dict()})
    if not result.modified_count:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "success"}
