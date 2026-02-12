import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy import create_engine

app = FastAPI(title="Faith Sobriety Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    if engine is None:
        return {"ok": False, "error": "DATABASE_URL not set"}

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar_one()
    return {"ok": True, "result": result}
