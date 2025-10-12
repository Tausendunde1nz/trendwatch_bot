from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "trendwatch"}

@app.get("/health")
def health():
    return {"ok": True}
