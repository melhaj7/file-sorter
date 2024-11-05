import json
import os
import stat
import logging
from pathlib import Path
from config import SORTING_RULES
from sorter_log_logic import log_dir_creation, log_file_movement


def get_files_in_dir(path):
    path_obj = Path(path)
    files = [f for f in path_obj.iterdir() if f.is_file()]
    return files


def get_files_by_ext(path, ext):
    path_obj = Path(path)
    files = get_files_in_dir(path_obj)

    return [f.name for f in files if f.suffix == ext]


def get_destination_folder(ext):
    for key, value in SORTING_RULES.items():
        if ext == key:
            return value
    return SORTING_RULES["default"]


def get_destination_path(path, file):
    path_obj = Path(path)
    destination_folder = get_destination_folder(file.suffix)
    destination_folder_path = path_obj / destination_folder
    return destination_folder_path / file.name


def move_file(file: Path, destination: Path, preview: bool, log_file_path: str):
    if not preview:
        if destination.parent.exists():
            log_file_movement(file, destination, log_file_path)
            file.rename(destination)
        else:
            dir_exist = destination.parent.exists()
            destination_folder = get_destination_folder(file.suffix)
            log_dir_creation(destination_folder, dir_exist, log_file_path)
            destination.parent.mkdir(exist_ok=True)
            log_file_movement(file, destination, log_file_path)
            file.rename(destination)
    else:
        print(f"file will be moved from {file} to {destination}")


def undo(log_file_path: str):
    full_log_file_path = Path.cwd() / log_file_path

    if not full_log_file_path.exists():
        print("Log file does not exist! Cannot undo sorting.")
        return
    try:
        with open(full_log_file_path, "r", encoding="utf-8") as log_file:
            log_data = json.load(log_file)

        for entry in reversed(log_data):
            if "source" not in entry or "destination" in entry:
                continue
            if source.exists() and destination.exists():
                source = Path(entry["source"])
                destination = Path(entry["destination"])

                destination.rename(source)
                print(f"moved {destination.name} back to {source.absolute()} ")
            else:
                print(
                    f"file {destination.name} not found. Moving to the next entry on log")

    except:
        print("file does not exist")


def sort_by_type(path: Path, preview: bool, log_file_path: str):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="logs.log",
                        encoding='utf-8', level=logging.DEBUG)

    files = get_files_in_dir(path)
    for file in files:
        file_path = file.absolute()
        destination_path = get_destination_path(path, file)
        try:
            logger.debug("moving file from: %s to: %s",
                         file_path, destination_path)
            move_file(file_path, destination_path, preview, log_file_path)
        except Exception as e:
            logger.error("Fail %s: moving %s from: %s to: %s",
                         e, file.name, file_path, destination_path)
