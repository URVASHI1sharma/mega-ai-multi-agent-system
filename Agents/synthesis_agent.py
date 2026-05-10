from datetime import datetime

from backend.context_schema import (
    SharedContext,
    AgentOutput
)


def run_synthesis_agent(context: SharedContext) -> AgentOutput:

    combined_outputs = []

    provenance_map = {}

    for idx, agent_output in enumerate(context.agent_outputs):

        combined_outputs.append(
            f"{agent_output.agent_name}: {agent_output.output_text}"
        )

        provenance_map[f"statement_{idx+1}"] = {
            "source_agent": agent_output.agent_name,
            "citations": agent_output.citations
        }

    final_response = "\n".join(combined_outputs)

    context.provenance_map = provenance_map

    return AgentOutput(
        agent_name="SynthesisAgent",
        output_text=final_response,
        citations=[],
        critiques=[],
        token_usage=500,
        timestamp=datetime.utcnow()
    )