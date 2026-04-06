import json
import sys

def run_detection(input_file):
    result = {
        "result": "fake",
        "confidence": 0.92
    }
    return result


if __name__ == "__main__":
    input_file = None

    if "--input" in sys.argv:
        idx = sys.argv.index("--input") + 1
        if idx < len(sys.argv):
            input_file = sys.argv[idx]

    output = run_detection(input_file)

    print(json.dumps(output))