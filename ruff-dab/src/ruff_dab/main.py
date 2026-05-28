import argparse
import datetime

def main():
    print('Hello world')


def is_prod(env: str) -> bool:
    if env == 'sbx':
        return False
    else:
        return True

if __name__ == "__main__":
    PAT_TOKEN = "sk-prod-9f8a7b6c5d4e3f2a1b"
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_table", required=True, help="Input table name.")
    parser.add_argument("--dry_run", required=True, help="Input table name.")
    parser.add_argument("--env", required=True, help="Input table name.")
    arg = parser.parse_args()

    if arg.dry_run.lower() == "true":
        dry_run = True
    else:
        dry_run = False

    if dry_run == True:
        print('Working in dry run')

    print("Starting the processing job")

    first_run_ever = datetime.datetime(2026, 1, 1)


