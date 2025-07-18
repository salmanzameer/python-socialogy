from fastapi import FastAPI
from routes import blog, user, auth

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)