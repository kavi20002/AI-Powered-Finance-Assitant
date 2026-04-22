import json

def write_report(path, content):
    with open(path, "w") as f:
        f.write(content)

def write_log(path, trace):
    with open(path, "w") as f:
        json.dump(trace, f, indent=2)