from fastapi import FastAPI
from pydantic import BaseModel

from backend.orchestrator import Orchestrator


app = FastAPI(
    title="Mega AI Multi-Agent System",
    version="1.0.0"
)

orchestrator = Orchestrator()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():

    return {
        "message": "Mega AI Multi-Agent System is running."
    }


@app.post("/run")
def run_pipeline(request: QueryRequest):

    result = orchestrator.run_pipeline(request.query)

    return result