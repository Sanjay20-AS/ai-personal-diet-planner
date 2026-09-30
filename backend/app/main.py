from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.db.database import Base, engine
from app.models.user import User
from app.models.profile import Profile
from app.models.diet_plan import DietPlan
from app.models.uploaded_file import UploadedFile
from app.models.generation_log import GenerationLog
from app.api.v1 import auth, profile, plans, files, dashboard

settings = get_settings()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Cloud-ready AI Personal Diet Planner API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(profile.router, prefix="/api/v1")
app.include_router(plans.router, prefix="/api/v1")
app.include_router(files.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")

@app.get("/api/v1/health", tags=["Health"])
def health():
    return {"status": "ok", "environment": settings.environment}
