
# investor_outreach_agent/investor_main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .investor_router import router as investor_router

app = FastAPI()

# Serve static files if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up template rendering
templates = Jinja2Templates(directory="app/templates")

# Include the investor outreach routes
app.include_router(investor_router)
