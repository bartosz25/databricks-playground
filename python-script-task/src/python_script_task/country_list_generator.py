import argparse
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_to_read", required=True, help="The file path to look for.")
    arg = parser.parse_args()

    countries_list = str(pathlib.Path(arg.file_to_read).read_text(encoding='UTF-8')).split(',')
    from databricks.sdk.runtime import dbutils
    dbutils.jobs.taskValues.set(key='countries_list', value=countries_list)
