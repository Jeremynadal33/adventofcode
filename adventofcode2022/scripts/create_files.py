import sys
import os
import requests

year = "2022"

if __name__ == "__main__":
    prefixes = ["test", "input"]
    parts = ["1"]  # , '2'] # it appears that this year's always gets only one file
    try:
        day = int(sys.argv[1])
    except:
        print("ERROR : no day was given or wrong number")

    for prefix in prefixes:
        for part in parts:
            filename = "../inputs/" + prefix + "_day" + str(day) + "_" + part + ".txt"
            if os.path.exists(filename):
                print("File {} already exist".format(filename))
            elif prefix == "input":
                try:
                    session_token = {"session": open("../../session_token.txt").read()}
                    input_url = f"https://adventofcode.com/{year}/day/{str(day)}/input"
                    response = requests.get(url=input_url, cookies=session_token)
                    open(filename, "w").write(response.text)
                except:
                    print(f"Could not retrieve input data for day {str(day)}")
                    open(filename, "w")
            else:
                open(filename, "w")

    scriptname = "day" + str(day) + ".py"
    if os.path.exists(scriptname):
        print("File {} already exist".format(scriptname))
    else:
        f = open(scriptname, "w")
        f.write(
            """
import sys
import numpy as np
import time 
from functions import *

def main():
    input_file, part = handle_args(sys.argv)
    solve_puzzle(input_file = input_file, part = part)

def solve_puzzle(input_file, part):
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def solve_part_1(input_file):
    print('Solving puzzle part 1')
    file = open(input_file, 'r').read().split('\\n')

def solve_part_2(input_file):
    print('Solving puzzle part 2')
    file = open(input_file, 'r').read().split('\\n')
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Elapsed in {} milisecondes'.format(1000*(end-start)))"""
        )
        f.close()
