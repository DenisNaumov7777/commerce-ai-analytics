"""
Main entry point for the FastAPI application.
"""
from fastapi import FastAPI
from app.config import settings
from app.routers import emotion

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-driven analytics microservice for e-commerce customer feedback."
)

app.include_router(emotion.router)

@app.get("/")
async def root():
    """
    Root endpoint to verify service health.
    """
    return {"message": "Commerce AI Analytics Service is running. Visit /docs for Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
