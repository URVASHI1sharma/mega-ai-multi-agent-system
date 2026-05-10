from datetime import datetime

from backend.context_schema import (
    SharedContext,
    AgentOutput
)


def run_decomposition_agent(context: SharedContext) -> AgentOutput:

    query = context.user_query

    # Simple decomposition logic
    # (Strategic MVP version)

    decomposed_tasks = [
        {
            "task_id": 1,
            "task_type": "analysis",
            "description": f"Analyze primary topic from query: {query}",
            "dependencies": []
        },
        {
            "task_id": 2,
            "task_type": "retrieval",
            "description": "Retrieve supporting information",
            "dependencies": [1]
        },
        {
            "task_id": 3,
            "task_type": "synthesis",
            "description": "Generate final synthesized response",
            "dependencies": [1, 2]
        }
    ]

    context.decomposed_tasks = decomposed_tasks

    output_text = (
        "Successfully decomposed query into structured subtasks "
        "with dependency tracking."
    )

    return AgentOutput(
        agent_name="DecompositionAgent",
        output_text=output_text,
        citations=[],
        critiques=[],
        token_usage=250,
        timestamp=datetime.utcnow()
    )