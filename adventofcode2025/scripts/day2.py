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

def is_invalid_id(id):
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return False
    else:
        middle_idx = len(str_id) // 2
        return str_id[:middle_idx] == str_id[middle_idx:]

def is_invalid_id_part2(id):
    str_id = str(id)
    for size in range(1, len(str_id)//2 + 1):
        if len(str_id) % size == 0: # can be a repetition of "size" x times in the string
            if str_id[:size] * (len(str_id) // size) == str_id:
                return True
    return False

def solve_part_1(input_file):
    file = open(input_file, "r").read()
    ranges = file.split(",")
    print(ranges)
    invalid_ids = set()
    for _range in ranges:
        start, end = map(int, _range.split("-"))
        for i in range(start, end + 1):
            if is_invalid_id(i):
                invalid_ids.add(i)
                logging.debug(f"Added invalid id {i}")
                logging.debug(f"Current invalid ids: {invalid_ids}")

    logging.info(f"sum of invalid ids: {sum(invalid_ids)}")



def solve_part_2(input_file):
    file = open(input_file, "r").read()
    ranges = file.split(",")

    invalid_ids = set()
    for _range in ranges:
        start, end = map(int, _range.split("-"))
        for i in range(start, end + 1):
            if is_invalid_id_part2(i):
                invalid_ids.add(i)
                logging.debug(f"Added invalid id {i}")
                logging.debug(f"Current invalid ids: {invalid_ids}")

    logging.info(f"sum of invalid ids: {sum(invalid_ids)}")



def test_is_invalid_id():
    assert is_invalid_id(11) == True
    assert is_invalid_id(5) == False
    assert is_invalid_id(1515) == True
    assert is_invalid_id(16) == False
    assert is_invalid_id(25) == False
    assert is_invalid_id(22) == True
    assert is_invalid_id(1000) == False
    assert is_invalid_id(10001000) == True
    assert is_invalid_id(38593859) == True

def test_is_invalid_id_part2():
    assert is_invalid_id_part2(11) == True
    assert is_invalid_id_part2(22) == True
    assert is_invalid_id_part2(99) == True
    assert is_invalid_id_part2(111) == True
    assert is_invalid_id_part2(111111) == True
    assert is_invalid_id_part2(1188511885) == True
    assert is_invalid_id_part2(222222) == True
    assert is_invalid_id_part2(1010) == True
    assert is_invalid_id_part2(565656) == True
    assert is_invalid_id_part2(824824824) == True
    assert is_invalid_id_part2(2121212121) == True

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000 * (end - start)} secondes")

    # test_is_invalid_id()
    # test_is_invalid_id_part2()


