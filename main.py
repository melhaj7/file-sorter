import argparse
from datetime import datetime
from sorter_logic import sort_by_type, undo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", type=str, help="Path to the directory to be sorted", required=True)
    parser.add_argument(
        "--type", action="store_true", help="sort files by type"
    )
    parser.add_argument(
        "--undo", action="store_true", help="undo all sorting operation done in directory"
    )
    parser.add_argument(
        "--preview", action="store_true", help="shows where the file will be transferred"
    )
    parser.add_argument(
        "--history", type=str,
        help="provide a file path in order to store sorting history. This is used for undo",
        default=f"history_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json"
    )
    args = parser.parse_args()

    log_file = args.history

    # if args.type:
    #     sort_by_type(args.path, args.preview, log_file)
    if args.undo:
        undo(log_file)

    # path = "C:/Users/ichib/Music/Sort tutorial"
main()
