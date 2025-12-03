import time
from commons.utils import args, logging


def main():
    file_path = (
        f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt"
        if args.INPUT == "REAL"
        else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt"
    )
    solve_puzzle(input_file=file_path, part=args.PART)


def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.DAY}")
    if part == 1:
        solve_part_1(input_file)
    elif part == 2:
        solve_part_2(input_file)


def solve_part_1(input_file):
    file = open(input_file, "r").read().split("\n")
    banks = []
    
    for bank in file:
        max_1 = 0
        max_2 = 0
        for i in range(len(bank)):
            if int(bank[i]) > max_1 and i != len(bank) - 1: # not the last one
                max_1 = int(bank[i])
                max_2 = int(bank[i + 1])
            elif int(bank[i]) > max_2 and i != 0: # not the first one
                max_2 = int(bank[i])

        banks.append(int(f"{max_1}{max_2}"))
        logging.info(f"Banks values: {banks[-1]}")
    logging.info(f"Sum of banks values: {sum(banks)}") # Final answer is 17158
    
def largest_bank_value(bank, battery_length):
    max_1 = 0
    max_2 = 0
    for i in range(len(bank)):
        if int(bank[i]) > max_1 and i != len(bank) - 1: # not the last one
            max_1 = int(bank[i])
            max_2 = int(bank[i + 1])
        elif int(bank[i]) > max_2 and i != 0: # not the first one
            max_2 = int(bank[i])
    return int(f"{max_1}{max_2}")

def test_largest_bank_value():
    assert largest_bank_value("987654321111111", 2) == 98
    assert largest_bank_value("811111111111119", 2) == 89
    assert largest_bank_value("234234234234278", 2) == 78
    assert largest_bank_value("818181911112111", 2) == 92
    assert largest_bank_value("4123535244222342322334342233754335452333242522124322242423331132232242422443224231234323332243364522", 2 ) == 76
    


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")


if __name__ == "__main__":
    # start = time.time()
    # main()
    # end = time.time()
    # logging.info(f"Elapsed in {1000 * (end - start)} secondes")
    test_largest_bank_value()
