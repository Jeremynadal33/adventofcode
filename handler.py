from commons.utils import logging, args
import os

script_path = f"adventofcode{args.YEAR}/scripts/day{args.DAY}.py"
test_path = f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
web_page = f"https://adventofcode.com/{args.YEAR}/day/{args.DAY}"
cli = f"python -m adventofcode{args.YEAR}.scripts.day{args.DAY} --day {args.DAY} --input {args.INPUT} --part {args.PART}"

if not os.path.exists(script_path):
    logging.warning(f"{script_path} doesnot exist yet, creating files...")
    os.system("python commons/create_files.py")
    os.system(f"code {test_path}")

os.system(f"code {script_path}")
logging.info(f"\nRunning the following command:\n{cli}\n")
logging.info(f"Web page : {web_page}\n\n")
os.system(cli)