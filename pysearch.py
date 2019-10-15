import argparse
import os
from pathlib import Path

HOME_DIR = str(Path.home())
DEFAULT_FILE_TYPE = '.py'


def pysearch(dir_path: str, file_type: str) -> list:
    """
    :param dir_path: Directory path to search files from
    :type dir_path: str
    :param file_type: File extension of the files to be searched
    :type file_type: str
    :return: List of files found with the provided file extension and dir path
    :rtype: list
    """
    files_list = list()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(file_type):
                files_list.append(os.path.join(root, file))
    return files_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find files in a directory with a specific extension")
    parser.add_argument('-d', '--dir-path', type=str, required=False, default=HOME_DIR,
                        help="Enter directory path to search files in.")
    parser.add_argument('-f', '--file-type', type=str, required=False, default=DEFAULT_FILE_TYPE,
                        help="Enter type of files to search. Eg: .txt or .json or .mp3")
    args = parser.parse_args()

    [print(i) for i in pysearch(args.dir_path, args.file_type)]
