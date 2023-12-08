import time
from commons.utils import args, logging

def main():
    file_path = f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt" if args.INPUT == "REAL" else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt" 
    solve_puzzle(input_file = file_path, part = args.PART)

def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)

def get_distance(hold_time, race_time):
    remaining_time = race_time - hold_time
    return hold_time * remaining_time

def solve_part_1(input_file):
    file = open(input_file, 'r').read().split('\n')
    race_times = [int(time) for time in file[0].split(':')[1].strip().split()]
    race_records = [int(dist) for dist in file[1].split(':')[1].strip().split()]
    
    ans = 1
    for race_number in range(len(race_times)):
        times = []
        for time in range(race_times[race_number]):
            times.append(get_distance(time, race_times[race_number]))
        ans *= sum( [ 1 if time > race_records[race_number] else 0 for time in times ]  )
    print(ans)

def solve_part_2(input_file):
    file = open(input_file, 'r').read().split('\n')
    race_time = int(file[0].split(':')[1].strip().replace(' ',''))
    race_record = int(file[1].split(':')[1].replace(' ', ''))
    
    # print(race_time, race_record)

    times = []
    for time in range(race_time):
        times.append(get_distance(time, race_time))

    print(sum( [ 1 if time > race_record else 0 for time in times ]  ))

    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")