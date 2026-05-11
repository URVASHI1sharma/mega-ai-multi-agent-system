from datetime import datetime


TEST_QUERIES = [
    "Compare renewable energy adoption trends.",
    "Analyze risks in AI regulation.",
    "Summarize electric vehicle market growth."
]


def evaluate_pipeline(orchestrator):

    evaluation_results = []

    for idx, query in enumerate(TEST_QUERIES):

        result = orchestrator.run_pipeline(query)

        evaluation_entry = {
            "test_id": idx + 1,
            "query": query,
            "status": "success" if "final_output" in result else "failure",
            "timestamp": datetime.utcnow().isoformat(),
            "result_summary": result.get(
                "final_output",
                result.get("error", "Unknown error")
            )
        }

        evaluation_results.append(evaluation_entry)

    return {
        "total_tests": len(TEST_QUERIES),
        "successful_runs": len([
            r for r in evaluation_results
            if r["status"] == "success"
        ]),
        "results": evaluation_results
    }