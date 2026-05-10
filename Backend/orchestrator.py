import uuid
from datetime import datetime

from backend.context_schema import SharedContext
from agents.decomposition_agent import run_decomposition_agent
from agents.retrieval_agent import run_retrieval_agent
from agents.critique_agent import run_critique_agent
from agents.synthesis_agent import run_synthesis_agent


class Orchestrator:

    def __init__(self):
        pass

    def initialize_context(self, user_query: str) -> SharedContext:
        return SharedContext(
            job_id=str(uuid.uuid4()),
            user_query=user_query,
            created_at=datetime.utcnow()
        )

    def log_policy_violation(self, context: SharedContext, violation: str):
        context.policy_violations.append(violation)

    def run_pipeline(self, user_query: str):

        context = self.initialize_context(user_query)

        try:

            # STEP 1 — Decomposition
            decomposition_output = run_decomposition_agent(context)
            context.agent_outputs.append(decomposition_output)

            # STEP 2 — Retrieval
            retrieval_output = run_retrieval_agent(context)
            context.agent_outputs.append(retrieval_output)

            # STEP 3 — Critique
            critique_output = run_critique_agent(context)
            context.agent_outputs.append(critique_output)

            # STEP 4 — Synthesis
            synthesis_output = run_synthesis_agent(context)
            context.agent_outputs.append(synthesis_output)

            return {
                "job_id": context.job_id,
                "final_output": synthesis_output.output_text,
                "policy_violations": context.policy_violations,
                "tool_logs": [log.dict() for log in context.tool_logs]
            }

        except Exception as e:

            self.log_policy_violation(
                context,
                f"Pipeline failure: {str(e)}"
            )

            return {
                "job_id": context.job_id,
                "error": str(e),
                "policy_violations": context.policy_violations
            }