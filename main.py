import logging
from file_scanner import get_destination_path, get_files_in_dir, move_file


def main():
    path = "C:/Users/ichib/Music/Sort tutorial"
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="logs.log",
                        encoding='utf-8', level=logging.DEBUG)

    files = get_files_in_dir(path)
    for file in files:
        source_path = file.absolute()
        destination_path = get_destination_path(path, file)

        try:
            logger.debug("moving file from: %s to: %s",
                         source_path, destination_path)
            move_file(source_path, destination_path)
        except Exception as e:
            logger.error("Fail %s: moving %s from: %s to: %s",
                         e, file.name, source_path, destination_path)


main()
