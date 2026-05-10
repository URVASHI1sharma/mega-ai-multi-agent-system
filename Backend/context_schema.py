from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime


class ToolCallLog(BaseModel):
    tool_name: str
    input_data: Dict[str, Any]
    output_data: Dict[str, Any]
    latency_ms: float
    accepted: bool
    retry_count: int
    timestamp: datetime


class CritiqueEntry(BaseModel):
    claim: str
    confidence_score: float
    flagged: bool
    critique_reason: Optional[str] = None


class AgentOutput(BaseModel):
    agent_name: str
    output_text: str
    citations: List[str] = []
    critiques: List[CritiqueEntry] = []
    token_usage: int = 0
    timestamp: datetime


class SharedContext(BaseModel):
    job_id: str

    user_query: str

    decomposed_tasks: List[Dict[str, Any]] = []

    retrieved_chunks: List[Dict[str, Any]] = []

    agent_outputs: List[AgentOutput] = []

    tool_logs: List[ToolCallLog] = []

    provenance_map: Dict[str, Any] = {}

    token_budget: int = 8000

    remaining_budget: int = 8000

    policy_violations: List[str] = []

    evaluation_scores: Dict[str, Any] = {}

    metadata: Dict[str, Any] = {}

    created_at: datetime = datetime.utcnow()