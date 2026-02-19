import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job_name", required=True)
    parser.add_argument("--volume_path_orders", required=True)
    parser.add_argument("--items_catalog_path", required=True)
    parser.add_argument("--a_variable", required=True)
    parser.add_argument("--warehouse_id_sql_queries", required=True)
    arg = parser.parse_args()
    print(f'Hello world for {arg.job_name}; volume paths: {arg.volume_path_orders} and {arg.items_catalog_path}'
          f' // a variable was {arg.a_variable}'
          f'// warehouse id sql queries: {arg.warehouse_id_sql_queries}')
