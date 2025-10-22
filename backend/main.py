from fastapi import FastAPI
from api import routes_chat, routes_docs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Study Assistant")

# Allow Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_docs.router)
app.include_router(routes_chat.router)

@app.get("/")
def home():
    return {"message": "AI Study Assistant Backend running!"}
