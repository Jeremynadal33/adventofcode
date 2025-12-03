from utils import args, logging
from advent_of_code_client import AdventOfCodeClient

import os


def create_inputs_files():
    folder_name = f"adventofcode{args.YEAR}"
    if not os.path.exists(folder_name):
        logging.error(
            f"Folder {folder_name} does not exists. Are you running the script from the root ?"
        )
        exit()
    if not os.path.exists(f"{folder_name}/inputs"):
        os.system(f"mkdir {folder_name}/inputs")

    file_types = ["input", "test"]
    for file_type in file_types:
        file_name = f"{folder_name}/inputs/{file_type}_day{args.DAY}.txt"
        if os.path.exists(file_name):
            logging.info("File {} already exist".format(file_name))
        elif file_type == "input":
            try:
                client = AdventOfCodeClient(args.YEAR)
                response = client.get_input(args.DAY)
                open(file_name, "w").write(response)
                logging.info(f"Created input file {file_name}")
            except:
                print("wtf")
                logging.info(
                    f"Could not retrieve input data for day {args.DAY}. Create an empty file instead."
                )
                open(file_name, "w")
        else:
            open(file_name, "w")


def create_bootstrap_script():
    folder_name = f"adventofcode{args.YEAR}"
    if not os.path.exists(folder_name):
        logging.error(
            f"Folder {folder_name} does not exists. Are you running the script from the root ?"
        )
        exit()
    if not os.path.exists(f"{folder_name}/scripts"):
        os.system(f"mkdir {folder_name}/scripts")

    script_name = f"{folder_name}/scripts/day{args.DAY}.py"
    if os.path.exists(script_name):
        print("File {} already exist".format(script_name))
    else:
        f = open(script_name, "w")
        f.write(open("commons/template_script.py", "r").read())
        f.close()


def create_files():
    create_inputs_files()
    create_bootstrap_script()


def main():
    create_files()


if __name__ == "__main__":
    main()
