import datetime
import os
import time


def write_files_to_tmp(tmp_dir: str):
    os.makedirs(tmp_dir, exist_ok=True)
    while True:
        current_time = datetime.datetime.now()
        current_time_for_file = current_time.strftime("%Y%m%d%H%M%S")
        file_name = f'file_{current_time_for_file}.txt'
        file_path = os.path.join(tmp_dir, file_name)
        with open(file_path, 'w') as f:
            current_time_for_content = current_time.strftime("%Y%m%d %H%M%S")
            f.write(f'Test from {current_time_for_content}')

        time.sleep(5)