import json
from pathlib import Path


def main():
    result = {
        "experiment_id": "EXP-001",
        "status": "PASS",
        "metrics": {
            "value": 4
        },
        "artifacts": []
    }

    output = Path("experiments/EXP-001/result.json")
    output.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
