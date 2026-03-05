import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--execution_time", required=True, help="Execution time for the data retrieval.")
    parser.add_argument("--backfill_time", required=True, help="Backfill time for the data retrieval.")
    arg = parser.parse_args()
    print(f'Hello world for {arg.execution_time} and {arg.backfill_time}')


def failing_main():
    raise Exception("The job failed!")
