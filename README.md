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
git clone https://github.com/URVASHI1sharma/mega-ai-multi-agent-system
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

# Design Tradeoffs & Simplifications

This project was intentionally implemented as a pragmatic engineering MVP under assignment time constraints.

The primary focus areas were:
- modular architecture
- centralized orchestration
- observability
- reproducibility
- structured agent communication
- evaluation readiness

Several production-scale concerns were intentionally simplified to prioritize architectural clarity and end-to-end system completeness.

---

## Intentional Simplifications

### Retrieval System
A lightweight simulated multi-hop retrieval flow was implemented instead of a full vector-database-backed RAG pipeline.

### SQL Querying
Natural language to SQL conversion uses lightweight rule-based mapping instead of a fine-tuned semantic parser.

### Context Compression
Approximate token budgeting structures were prepared, but advanced context compression strategies were intentionally deferred.

### Tool Execution
Tool orchestration focuses on structured interfaces, failure contracts, and reproducibility rather than production-scale distributed execution.

### Observability
Structured JSON logging was prioritized over external observability platforms to keep the system lightweight and reproducible.

---

# Failure Handling

The system includes lightweight failure management through:
- structured error contracts
- centralized orchestration
- exception handling
- policy violation tracking
- timeout-aware execution

---

# Reproducibility

The project emphasizes reproducibility through:
- deterministic orchestration flow
- structured evaluation harness
- Docker configuration
- append-only structured logs
- modular architecture

---

# AI Assistance Disclosure

AI tools were used during the development process for:
- architecture brainstorming
- debugging support
- implementation guidance
- documentation refinement
- workflow validation

All final implementation decisions, integrations, and testing were reviewed and validated manually.

---

# Future Improvements

Potential future extensions include:
- vector database integration
- advanced context compression
- dynamic agent routing
- async worker orchestration
- streaming responses
- advanced contradiction resolution
- semantic retrieval pipelines
- automated prompt optimization

---

# Final Notes

This project prioritizes engineering clarity, orchestration structure, and reproducibility while intentionally balancing implementation scope against assignment constraints.

The goal was to deliver a clean, runnable, architecture-focused multi-agent system demonstrating practical systems engineering principles for modern LLM workflows.

