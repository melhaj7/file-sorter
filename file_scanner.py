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


def get_target_folder(ext):
    for key, value in SORTING_RULES.items():
        if key == ext:
            return value
