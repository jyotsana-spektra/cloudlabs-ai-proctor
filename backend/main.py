from fastapi import FastAPI

app = FastAPI(
    title="CloudLabs AI Proctor API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "CloudLabs AI Proctor API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}