from pathlib import Path
from config import SORTING_RULES


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


def move_file(source, destination):
    if destination.parent.exists():
        new_path = source.rename(destination)
        print(new_path)
    else:
        destination.parent.mkdir(exist_ok=True)
        new_path = source.rename(destination)
        print(new_path)
