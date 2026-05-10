import sqlite3
import time


def run_sql_lookup(natural_language_query: str):

    start_time = time.time()

    if not natural_language_query:
        return {
            "status": "error",
            "error_code": "EMPTY_QUERY",
            "message": "No query provided.",
            "results": []
        }

    try:

        conn = sqlite3.connect("database/eval_data.db")
        cursor = conn.cursor()

        # Simplified NL → SQL mapping
        if "all eval runs" in natural_language_query.lower():
            sql_query = "SELECT * FROM eval_runs"
        else:
            sql_query = "SELECT name FROM sqlite_master WHERE type='table';"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        conn.close()

        latency = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "query": natural_language_query,
            "sql_executed": sql_query,
            "results": rows,
            "latency_ms": latency
        }

    except Exception as e:

        return {
            "status": "error",
            "error_code": "SQL_FAILURE",
            "message": str(e),
            "results": []
        }