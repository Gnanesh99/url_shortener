# URL Shortener API ⚡
 
A fast, lightweight URL shortener API built with FastAPI. Shorten long URLs, track clicks, and view statistics.
 
## Features
 
- Shorten any long URL to a 6-character code
- Redirect to original URL via short code
- Track click count per URL
- View URL statistics
- Auto-generated interactive API docs
## Tech Stack
 
- **Framework** — FastAPI
- **Database** — SQLite via SQLAlchemy
- **Validation** — Pydantic
- **Server** — Uvicorn
## Project Structure
 
```
url-shortener/
├── main.py          # Routes and app entry point
├── database.py      # Database connection and session
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
└── requirements.txt
```
 
## Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/Gnanesh99/url-shortener.git
cd url-shortener
```
 
### 2. Create and activate virtual environment
 
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Run the app
 
```bash
uvicorn main:app --reload
```
 
Visit `http://127.0.0.1:8000`
 
## API Endpoints
 
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/shorten` | Shorten a URL |
| GET | `/{short_code}` | Redirect to original URL |
| GET | `/stats/{short_code}` | View URL statistics |
 
## Usage
 
### Shorten a URL
 
```bash
curl -X POST "http://127.0.0.1:8000/shorten" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://www.google.com"}'
```
 
Response:
```json
{
    "id": 1,
    "original_url": "https://www.google.com",
    "short_code": "abc123",
    "clicks": 0,
    "created_at": "2026-05-30T09:13:30"
}
```
 
### Redirect
 
Visit `http://127.0.0.1:8000/abc123` in your browser — automatically redirects to the original URL and increments click count.
 
### View Stats
 
```bash
curl "http://127.0.0.1:8000/stats/abc123"
```
 
Response:
```json
{
    "id": 1,
    "original_url": "https://www.google.com",
    "short_code": "abc123",
    "clicks": 5,
    "created_at": "2026-05-30T09:13:30"
}
```
 
## Interactive Docs
 
FastAPI auto-generates interactive documentation.
 
Visit `http://127.0.0.1:8000/docs` to explore and test all endpoints directly in the browser.
 
## Author
 
Gorle Gnanesh
 
