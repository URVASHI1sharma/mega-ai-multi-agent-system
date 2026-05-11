#This is ReadMe file
# Mega AI — Multi-Agent Orchestration System

A production-style multi-agent orchestration system built for the Mega AI take-home assignment.

This project demonstrates a modular AI-agent architecture capable of:
- task decomposition
- multi-hop retrieval
- critique/self-evaluation
- provenance-aware synthesis
- structured tool orchestration
- reproducible evaluation
- observability through structured logging

The system was intentionally designed as a pragmatic engineering MVP focused on:
- modularity
- reproducibility
- traceability
- orchestration clarity
- engineering simplicity under time constraints

---

# System Architecture

The pipeline follows a centralized orchestration model where agents communicate exclusively through a shared context object.

```text
User Query
    ↓
FastAPI Endpoint
    ↓
Orchestrator
    ↓
Shared Context
    ↓
Decomposition Agent
    ↓
Retrieval Agent
    ↓
Critique Agent
    ↓
Synthesis Agent
    ↓
Final Response
```

---

# Core Components

## 1. Shared Context

Acts as the central memory and communication layer between all agents.

Responsibilities:
- stores decomposed tasks
- tracks retrieved chunks
- maintains provenance mappings
- logs tool usage
- stores critiques and evaluation metadata

---

## 2. Orchestrator

Acts as the execution controller for the entire pipeline.

Responsibilities:
- initializes shared context
- routes execution flow
- coordinates agent execution
- handles failures
- enforces centralized orchestration

Agents never communicate directly with each other.

---

## 3. Agents

### Decomposition Agent
Breaks complex user queries into structured subtasks with dependency tracking.

### Retrieval Agent
Performs lightweight multi-hop retrieval across multiple evidence chunks.

### Critique Agent
Evaluates outputs from previous agents using structured confidence scoring.

### Synthesis Agent
Combines outputs into a final provenance-aware response.

---

## 4. Tools Layer

### Web Search Tool
Provides structured external retrieval simulation.

### Python Sandbox Tool
Executes isolated Python snippets with timeout handling.

### SQL Lookup Tool
Supports lightweight natural-language-driven SQLite querying.

### Self Reflection Tool
Performs introspection over prior agent outputs to identify inconsistencies.

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd mega-ai-multi-agent-system
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run FastAPI Server

```bash
uvicorn backend.main:app --reload
```

Server starts at:

```text
http://127.0.0.1:8000
```

---

## 4. Swagger API Documentation

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# API Usage

## POST `/run`

Example Request:

```json
{
  "query": "Analyze electric vehicle adoption trends."
}
```

Example Response:

```json
{
  "job_id": "example-job-id",
  "final_output": "Structured multi-agent response...",
  "policy_violations": [],
  "tool_logs": []
}
```

---

# Evaluation Harness

The project includes a lightweight evaluation framework for reproducible testing.

Evaluation pipeline:
- runs predefined benchmark queries
- validates pipeline execution
- records success/failure states
- supports reproducible experimentation

Evaluation entrypoint:

```python
from evaluation.evaluator import evaluate_pipeline
```

---

# Structured Logging

Structured JSON logging is implemented using append-only `.jsonl` logs.

Logs include:
- pipeline lifecycle events
- failures
- orchestration traces
- execution metadata

Example log fields:
- timestamp
- event_type
- agent_name
- metadata

---

# Docker Support

The project includes lightweight Docker support for reproducible execution.

Docker files included:
- Dockerfile
- docker-compose.yml
- .dockerignore

Example run command:

```bash
docker compose up --build
```

---