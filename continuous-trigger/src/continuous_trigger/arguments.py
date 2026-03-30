import argparse
from argparse import Namespace


def get_parser() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path with the input data")
    arg = parser.parse_args()
    return arg