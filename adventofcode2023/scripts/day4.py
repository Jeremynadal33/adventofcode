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

def solve_part_1(input_file):
    file = open(input_file, 'r').read().split('\n')
    summ = 0
    for card in file:
        winning_str = card.split(':')[1].split('|')[0].strip().replace('  ',' ').split(' ')
        inputs_str = card.split(':')[1].split('|')[1].strip().replace('  ',' ').split(' ')

        num_winnings = 0
        for input_str in inputs_str:
            if input_str in winning_str:
                num_winnings += 1
        if num_winnings > 0: summ += pow(2, num_winnings - 1)

    print(summ)

def solve_part_2(input_file):
    file = open(input_file, 'r').read().split('\n')   
         
    all_cards = {}
    for card in file:
        num_card = card.split(':')[0].split(' ')[-1]
        # if we already won copies of that card when it arrives
        if num_card in all_cards.keys(): all_cards[num_card] += 1
        # else we have only one copy of it
        else: all_cards[num_card] = 1

        winning_str = card.split(':')[1].split('|')[0].strip().replace('  ',' ').split(' ')
        inputs_str = card.split(':')[1].split('|')[1].strip().replace('  ',' ').split(' ')

        num_winnings = 0
        for input_str in inputs_str:
            if input_str in winning_str:
                num_winnings += 1
        for index in range(int(num_card) + 1, int(num_card) + num_winnings + 1):
            # we add one copy for each following cards
            if str(index) in all_cards.keys(): all_cards[str(index)] += all_cards[num_card]
            # else we have only one copy of it
            else: all_cards[str(index)] = all_cards[num_card]
        print(all_cards)
        print(sum(all_cards.values()))
        # if num_winnings > 0: summ += pow(2, num_winnings - 1)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")