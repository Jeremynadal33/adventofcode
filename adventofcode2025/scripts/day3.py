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
        banks.append(largest_bank_value(bank, 2))
    logging.info(f"Sum of banks values: {sum(banks)}") # Final answer is 17158
    
def largest_bank_value(bank, battery_length):
    nb_batteries_left_to_find = battery_length
    current_idx = 0
    batteries = ""
    logging.debug(f"Finding largest bank value in {bank} for battery length {battery_length}")
    while nb_batteries_left_to_find > 0:
        looking_toward_idx = -nb_batteries_left_to_find+1 if nb_batteries_left_to_find > 1 else None
        looking_in = bank[:looking_toward_idx] if looking_toward_idx is not None else bank
        logging.debug(f"Looking in: {looking_in}")
        batteries += max(looking_in)
        nb_batteries_left_to_find -= 1
        current_idx = looking_in.index(max(looking_in))
        logging.debug(f"Found battery value {looking_in[current_idx]} at index {current_idx}")
        bank = bank[current_idx + 1:]
        logging.debug(f"Remaining bank to look into: {bank}")
    logging.debug(f"Largest batteries found: {batteries}")
    return int(batteries)

def test_largest_bank_value():
    assert largest_bank_value("987654321111111", 2) == 98
    assert largest_bank_value("811111111111119", 2) == 89
    assert largest_bank_value("234234234234278", 2) == 78
    assert largest_bank_value("818181911112111", 2) == 92
    assert largest_bank_value("4123535244222342322334342233754335452333242522124322242423331132232242422443224231234323332243364522", 2 ) == 76

    assert largest_bank_value("987654321111111", 12) == 987654321111
    assert largest_bank_value("811111111111119", 12) == 811111111119
    assert largest_bank_value("234234234234278", 12) == 434234234278
    assert largest_bank_value("818181911112111", 12) == 888911112111
    


def solve_part_2(input_file):
    file = open(input_file, "r").read().split("\n")
    banks = []

    for bank in file:
        banks.append(largest_bank_value(bank, 12))
    logging.info(f"Sum of banks values: {sum(banks)}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")
    # test_largest_bank_value()
