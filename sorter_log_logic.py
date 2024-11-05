import json
from pathlib import Path


def log_dir_creation(directory: Path | str, dir_exist: bool, log_file_path: str):
    if dir_exist:
        return
    if not Path(log_file_path).exists():
        log_data = []
    else:
        with open(log_file_path, "r", encoding="utf-8") as log_file:
            log_data = json.load(log_file)

    log_data.append({"created": str(directory)})

    with open(log_file_path, "w", encoding="utf-8") as log_file:
        json.dump(log_data, log_file, indent=4)


def log_file_movement(file: Path | str, destination: Path | str, log_file_path):
    log_data = []

    if Path(log_file_path).exists():
        try:
            with open(log_file_path, "r", encoding="utf-8") as log_file:
                log_data = json.load(log_file)
        except json.JSONDecodeError as e:
            print(f"error decoding json in {log_file_path}: {e}")
            log_data = []

    log_data.append({"source": str(file), "destination": str(destination)})

    try:
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            json.dump(log_data, log_file, indent=4)
    except IOError as e:
        print(f"error writing to {log_file_path}: {e}")
