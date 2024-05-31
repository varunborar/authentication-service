from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Authentication Service",
    description="Genric Authentication Service for any application",
    version="0.1.0",
    docs_url="/docs"
)


# Probes and Health Check
@app.get("/health-check")
async def status():
    return JSONResponse(content={"status": "OK"})


@app.get("/ready")
async def readinessProbe():
    return JSONResponse(content={"status": "OK"})


@app.get("/live")
async def livenessProbe():
    return JSONResponse(content={"status": "OK"})
