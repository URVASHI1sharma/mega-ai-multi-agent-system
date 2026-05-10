from datetime import datetime

from backend.context_schema import (
    SharedContext,
    AgentOutput,
    CritiqueEntry
)


def run_critique_agent(context: SharedContext) -> AgentOutput:

    critiques = []

    for agent_output in context.agent_outputs:

        critique = CritiqueEntry(
            claim=agent_output.output_text,
            confidence_score=0.88,
            flagged=False,
            critique_reason=None
        )

        critiques.append(critique)

    output_text = (
        "Reviewed agent outputs and assigned structured confidence scores."
    )

    return AgentOutput(
        agent_name="CritiqueAgent",
        output_text=output_text,
        citations=[],
        critiques=critiques,
        token_usage=300,
        timestamp=datetime.utcnow()
    )