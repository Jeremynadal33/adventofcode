import time
from commons.utils import args, logging
import numpy as np
import json


def main():
    file_path = f"adventofcode{args.YEAR}/inputs/input_day{args.DAY}.txt" if args.INPUT == "REAL" else f"adventofcode{args.YEAR}/inputs/test_day{args.DAY}.txt" 
    solve_puzzle(input_file = file_path, part = args.PART)

def solve_puzzle(input_file, part):
    logging.info(f"Solving puzzle part {args.PART}")
    if part == 1 :
        solve_part_1(input_file)
    elif part == 2 :
        solve_part_2(input_file)


def get_hand_power(hand, part=args.PART):
    ''' return 7 (weekest) to 1 (strongest) '''
    types = {
        'FiveOAK': 1,
        'FourOAK': 2,
        'FH': 3,
        'ThreeOAK': 4,
        'Pairs': 5,
        'Pair': 6,
        'HC': 7
    }
    if part==1:
        _, counts = np.unique(list(hand), return_counts=True)

        if 5 in counts: return types['FiveOAK']
        elif 4 in counts: return types['FourOAK']
        elif 3 in counts and 2 in counts: return types['FH']
        elif 3 in counts : return types['ThreeOAK']
        elif sum(counts==2) == 2: return types['Pairs']
        elif 2 in counts: return types['Pair']
        else: return types['HC']
    else:
        cards_without_j = hand.replace('J', '')
        num_jockers = 5 - len(cards_without_j)

        _, counts = np.unique(list(cards_without_j), return_counts=True)

        if num_jockers == 5: return types['FiveOAK']
        elif (5 - num_jockers) in counts: return types['FiveOAK']
        elif (4 - num_jockers) in counts: return types['FourOAK']
        # list all possibilities to get a full house
        elif (3 in counts) and (2 in counts): return types['FH']
        elif (num_jockers == 1) and (sum(counts==2) == 2): return types['FH']

        elif (3 - num_jockers) in counts : return types['ThreeOAK']
        elif sum(counts==2) == 2: return types['Pairs']
        elif (2 - num_jockers) in counts: return types['Pair']
        else: return types['HC']


def get_card_power(card, part=args.PART):
    '''
        return M (weakest => 2) to A (strongest => A)
        It will then be easy to sort alphabetically the hands!
    '''
    if part == 1:
        types = {
            'A': 'A',
            'K': 'B',
            'Q': 'C',
            'J': 'D',
            'T': 'E',
            '9': 'F',
            '8': 'G',
            '7': 'H',
            '6': 'I',
            '5': 'J',
            '4': 'K',
            '3': 'L',
            '2': 'M'
        }
    else:
        types = {
            'A': 'A',
            'K': 'B',
            'Q': 'C',
            'T': 'E',
            '9': 'F',
            '8': 'G',
            '7': 'H',
            '6': 'I',
            '5': 'J',
            '4': 'K',
            '3': 'L',
            '2': 'M',
            'J': 'N'
        }
    return types[card]

def get_hand_card_power(hand):
    return ''.join([get_card_power(card) for card in list(hand)])

def pprint(_dict):
    print(json.dumps(_dict, indent=2))

def solve_part_1(input_file):
    file = open(input_file, 'r').read().split('\n')

    hands = {}
    for line in file:
        hand = line.split(' ')[0]
        bid = int(line.split(' ')[1])
        hands[hand]= {"power": get_hand_power(hand), "bid": bid, "card_values": get_hand_card_power(hand)}

    sorted_hands = dict(sorted(hands.items(), key=lambda item: (item[1]["power"], item[1]["card_values"]), reverse=True))
    multiplier = 1
    summ = 0
    for _, value in sorted_hands.items():
        summ += multiplier * value["bid"]
        multiplier += 1
    print(summ)


def solve_part_2(input_file):
    file = open(input_file, 'r').read().split('\n')
    # test = '2347J'
    # print(test, get_hand_power(test))

    hands = {}
    for line in file:
        hand = line.split(' ')[0]
        bid = int(line.split(' ')[1])
        # get_hand_power(hand)
        hands[hand]= {"power": get_hand_power(hand), "bid": bid, "card_values": get_hand_card_power(hand)}

    sorted_hands = dict(sorted(hands.items(), key=lambda item: (item[1]["power"], item[1]["card_values"]), reverse=True))
    # pprint(sorted_hands)
    multiplier = 1
    summ = 0
    for _, value in sorted_hands.items():
        summ += multiplier * value["bid"]
        multiplier += 1
    print(summ)    
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    logging.info(f"Elapsed in {1000*(end-start)} secondes")