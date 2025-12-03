from commons.utils import logging, args
import os

from commons.advent_of_code_client import AdventOfCodeClient

script_path = f"adventofcode{args.YEAR}/scripts/day{args.DAY}.py"
cli = f"python -m adventofcode{args.YEAR}.scripts.day{args.DAY} --day {args.DAY} --input {args.INPUT} --part {args.PART}"


if not os.path.exists(script_path):
    logging.warning(f"{script_path} doesnot exist yet, creating files...")
    os.system("python commons/create_files.py")

os.system(f"code {script_path}")
logging.info(f"Running the following command:\n{cli}\n\n")
os.system(cli)

if args.submit:
    client = AdventOfCodeClient(year=args.YEAR)
    test_answer = input("Enter your answer to submit: ")
    response = client.submit_answer(day=args.DAY, level=args.PART, answer=test_answer)
    logging.info(f"Submission response:\n{response}")