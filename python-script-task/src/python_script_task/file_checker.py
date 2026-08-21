import argparse
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_to_check", required=True, help="The file path to look for.")
    arg = parser.parse_args()

    if not pathlib.Path(arg.file_to_check).is_file():
        raise RuntimeError(f'File {arg.file_to_check} not found.')
