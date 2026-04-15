import json
from datetime import datetime

def save_output(data):
    file_name = "content_log.json"

    try:
        with open(file_name, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({
        "timestamp": str(datetime.now()),
        "data": data
    })

    with open(file_name, "w") as f:
        json.dump(logs, f, indent=2)
