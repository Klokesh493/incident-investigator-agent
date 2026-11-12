import argparse
import json
from pathlib import Path


def evaluate(data):
    if data["end"] < data["start"]:
        raise ValueError("incident end precedes start")
    matches = [event for event in data["events"] if event["service"] == data["service"]
               and data["start"] <= event["minute"] <= data["end"]]
    return [event["id"] for event in sorted(matches, key=lambda item: (item["minute"], item["id"]))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), indent=2))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")


if __name__ == "__main__":
    main()
