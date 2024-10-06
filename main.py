from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models import UserProfile
from recommendation import match_jobs
from database import create_connection, close_connection
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files (for JavaScript)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up template rendering with Jinja2
templates = Jinja2Templates(directory="templates")

# Index route (renders HTML page)
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API to get job recommendations
@app.post("/recommendations")
async def recommend_jobs(profile: UserProfile):
    connection = create_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        recommendations = match_jobs(profile, connection)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        close_connection(connection)
