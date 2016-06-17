"""
cypher.

Licensed under MIT.
Copyright (c) 2016 Joseph Kato.
"""
import argparse
from .util import identify

parser = argparse.ArgumentParser(
    prog="cypher",
    description="A source code identification tool."
)
parser.add_argument(
    "src",
    nargs=1,
    help="Path to unknown source code."
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Return all scores."
)
args = vars(parser.parse_args())


def main():
    result = identify(args["src"][0], verbose=args["verbose"])
    if result < 0:
        print("Language not recognized.")
    else:
        print(result)
    return result if result < 0 else 0
