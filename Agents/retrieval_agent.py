from datetime import datetime

from backend.context_schema import (
    SharedContext,
    AgentOutput
)


def run_retrieval_agent(context: SharedContext) -> AgentOutput:

    query = context.user_query

    # Simulated multi-hop retrieval
    # (Strategic MVP implementation)

    retrieved_chunks = [
        {
            "chunk_id": "chunk_1",
            "source": "web_search_stub",
            "content": f"Primary information related to query: {query}",
            "relevance_score": 0.91
        },
        {
            "chunk_id": "chunk_2",
            "source": "knowledge_base",
            "content": "Secondary supporting evidence retrieved for multi-hop reasoning.",
            "relevance_score": 0.87
        }
    ]

    context.retrieved_chunks = retrieved_chunks

    output_text = (
        "Retrieved and combined evidence from multiple sources "
        "to support downstream reasoning."
    )

    citations = [
        "chunk_1",
        "chunk_2"
    ]

    return AgentOutput(
        agent_name="RetrievalAgent",
        output_text=output_text,
        citations=citations,
        critiques=[],
        token_usage=400,
        timestamp=datetime.utcnow()
    )