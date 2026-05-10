import subprocess
import tempfile
import time


def run_python_code(code: str):

    start_time = time.time()

    if not code or len(code.strip()) == 0:
        return {
            "status": "error",
            "error_code": "EMPTY_CODE",
            "message": "No Python code provided.",
            "stdout": "",
            "stderr": "",
            "exit_code": 1
        }

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as temp_file:

            temp_file.write(code)
            temp_file_path = temp_file.name

        result = subprocess.run(
            ["python", temp_file_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        latency = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "latency_ms": latency
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "error",
            "error_code": "TIMEOUT",
            "message": "Python execution timed out.",
            "stdout": "",
            "stderr": "",
            "exit_code": 1
        }

    except Exception as e:

        return {
            "status": "error",
            "error_code": "EXECUTION_FAILURE",
            "message": str(e),
            "stdout": "",
            "stderr": "",
            "exit_code": 1
        }