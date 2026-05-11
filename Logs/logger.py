import json
from datetime import datetime


LOG_FILE_PATH = "logs/system_logs.jsonl"


def write_log(
    event_type: str,
    agent_name: str,
    message: str,
    metadata: dict = None
):

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "agent_name": agent_name,
        "message": message,
        "metadata": metadata or {}
    }

    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")