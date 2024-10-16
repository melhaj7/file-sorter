from pathlib import Path
from file_scanner import *
from sorter_logic import *
from config import SORTING_RULES


def main():
    path = "C:/Users/ichib/Music/Sort tutorial"
    # path = Path("C:/Users/ichib/Music/Sort tutorial")

    files = get_files_in_dir(path)
    for file in files:
        print(f"File {file.name}")
        source_path = file.absolute()
        print(source_path)

        target_folder = get_target_folder(file.suffix)
        print(target_folder)

    # print(target_folder)
        target_path = file.parent / target_folder / file.name
        print(target_path)

    # path = Path(path) / "images"

    # if path.exists():
    #     print("path exists")
    # else:
    #     path.mkdir()

    # return_path = source_path.rename(target_path)
    # print(return_path)


main()
