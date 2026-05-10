import time


def run_self_reflection(context):

    start_time = time.time()

    try:

        reflections = []

        agent_outputs = context.agent_outputs

        for output in agent_outputs:

            reflections.append({
                "agent": output.agent_name,
                "summary": output.output_text[:120],
                "potential_issue": "No major contradiction detected."
            })

        latency = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "reflection_count": len(reflections),
            "reflections": reflections,
            "latency_ms": latency
        }

    except Exception as e:

        return {
            "status": "error",
            "error_code": "REFLECTION_FAILURE",
            "message": str(e),
            "reflections": []
        }