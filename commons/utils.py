import datetime
import os

# Parse arguments
import argparse

import logging

logging.root.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

parser = argparse.ArgumentParser()
parser.add_argument(
    "--year",
    help="Specify year if you want to. Default is current year.",
    metavar="year",
    dest="YEAR",
    default=datetime.date.today().year,
    type=int,
)

parser.add_argument(
    "--day",
    help="Specify day if you want to. Default is current day. Must be between 1 & 24",
    metavar="day",
    dest="DAY",
    default=datetime.date.today().day,
    type=int,
)

parser.add_argument(
    "--input",
    help="Specify if we are using the real input or the test. Must be one of 'TEST' or 'REAL' ",
    metavar="input",
    dest="INPUT",
    default="TEST",
    type=str,
)

parser.add_argument(
    "--part",
    help="Specify which part we are resolving. Must be 1 or 2",
    metavar="part",
    dest="PART",
    default=1,
    type=int,
)

parser.add_argument(
        "--submit",
        help="Whether to submit the answer after solving the puzzle.",
        action="store_true",
        required=False,
        default=False,
    )

args = parser.parse_args()

if args.YEAR > datetime.date.today().year:
    logging.error("ERROR: year cannot be in the future")
    exit()
if args.DAY > datetime.date.today().day and args.YEAR == datetime.date.today().year:
    logging.error("ERROR: cannot be in the future")
    exit()
if args.PART not in [1, 2]:
    logging.error("ERROR: part must be 1 or 2")
    exit()
