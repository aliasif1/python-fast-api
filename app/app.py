from fastapi import FastAPI, HTTPException
from app.mock_posts import posts
from app.schemas import PostCreate, PostResponse

app = FastAPI()

# Get all posts
@app.get("/posts")
def get_posts(limit: int = 10):
    return posts[:limit]

# Get post by ID
@app.get("/posts/{post_id}")
def get_post(post_id: int) -> PostResponse:
    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break
    if post is None: raise HTTPException(status_code=404, detail="Post not found")
    return post

# Create a new post
@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate) -> PostResponse:
    new_post = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content
    }
    posts.append(new_post)
    return new_post