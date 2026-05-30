from fastapi import FastAPI,Depends
# Standard library
import random
import string

# FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse

# Database
from sqlalchemy.orm import Session
from database import engine, get_db

# Local
import models
from models import URL
from schemas import URLCreate, URLResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to URL Shortener"}


@app.post("/shorten", response_model=URLResponse)
def shorten_url(request: URLCreate, db: Session = Depends(get_db)):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    new_url = URL(original_url=request.original_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    db_url.clicks = (db_url.clicks or 0) + 1
    db.commit()
    return RedirectResponse(url=db_url.original_url)


@app.get("/stats/{short_code}", response_model=URLResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url
