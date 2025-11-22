from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My FastAPI Backend",
    description="A modern REST API built with FastAPI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers can be included here when available, e.g.:
# from app.routers import users, auth
# app.include_router(users.router)
# app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Backend"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
