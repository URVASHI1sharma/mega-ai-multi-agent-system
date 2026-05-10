import time


def run_web_search(query: str):

    start_time = time.time()

    if not query or len(query.strip()) == 0:
        return {
            "status": "error",
            "error_code": "EMPTY_QUERY",
            "message": "Search query cannot be empty.",
            "results": []
        }

    try:

        # Simulated search results
        results = [
            {
                "title": "Sample Search Result 1",
                "url": "https://example.com/result1",
                "relevance_score": 0.91
            },
            {
                "title": "Sample Search Result 2",
                "url": "https://example.com/result2",
                "relevance_score": 0.87
            }
        ]

        latency = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "query": query,
            "results": results,
            "latency_ms": latency
        }

    except Exception as e:

        return {
            "status": "error",
            "error_code": "SEARCH_FAILURE",
            "message": str(e),
            "results": []
        }