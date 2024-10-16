from pathlib import Path
from file_scanner import *
from sorter_logic import *
from config import SORTING_RULES


def main():
    path = "C:/Users/ichib/Music/Sort tutorial"
    # path = Path("C:/Users/ichib/Music/Sort tutorial")

    files = get_files_in_dir(path)
    for file in files:
        source_path = file.absolute()

        path_obj = Path(path)
        target_folder = get_target_folder(file.suffix)
        target_folder_path = path_obj / target_folder
        target_path = path_obj / target_folder / file.name

        if target_path.parent.exists():
            new_path = source_path.rename(target_path)
            print(new_path)
        else:
            target_folder_path.mkdir(exist_ok=True)
            new_path = source_path.rename(target_path)
            print(new_path)


main()
