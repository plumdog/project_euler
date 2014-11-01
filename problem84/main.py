#!/usr/bin/env python3

import random
import itertools
import collections

random.seed(1)


BOARD = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
         'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
         'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
         'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']


CC_CARDS = ['GOTO GO', 'GOTO JAIL'] + 14 * [None]


CH_CARDS = [
    'GOTO GO', 'GOTO JAIL', 'GOTO C1', 'GOTO E3', 'GOTO H2', 'GOTO R1',
    'GOTO NEXTRAIL', 'GOTO NEXTRAIL', 'GOTO NEXTUTIL', 'GOTO -3'] + \
    6 * [None]


REPEATS = 1000000
DICE_UPTO = 4


def rand_2dice(upto):
    return (random.randrange(1, upto + 1),
            random.randrange(1, upto + 1))


def move(index, previous_rolls, previous_cc_cards, previous_ch_cards):
    roll = rand_2dice(DICE_UPTO)
    previous_rolls.append(roll)

    if len(previous_cc_cards) == len(CC_CARDS):
        del previous_cc_cards[:]
    if len(previous_ch_cards) == len(CH_CARDS):
        del previous_ch_cards[:]

    if speeding(previous_rolls):
        return BOARD.index('JAIL')

    index += roll[0] + roll[1]
    index %= len(BOARD)

    landed_on = BOARD[index]

    if landed_on[:2] == 'CH':
        ch_options = available_cards(previous_ch_cards, CH_CARDS)
        if ch_options:
            card = random.choice(ch_options)
            previous_ch_cards.append(card)
            if card:
                index = process_card(index, card)
                landed_on = BOARD[index]

    if landed_on[:2] == 'CC':
        cc_options = available_cards(previous_cc_cards, CC_CARDS)
        if cc_options:
            card = random.choice(cc_options)
            previous_cc_cards.append(card)
            if card:
                index = process_card(index, card)
                landed_on = BOARD[index]

    if landed_on == 'G2J':
        return BOARD.index('JAIL')
    return index


def speeding(previous_rolls):
    if len(previous_rolls) < 3:
        return False

    return (previous_rolls[-1][0] == previous_rolls[-1][1] and
            previous_rolls[-2][0] == previous_rolls[-2][1] and
            previous_rolls[-3][0] == previous_rolls[-3][1])


def available_cards(previous_cards, all_cards):
    available = all_cards[:]
    for prev in previous_cards:
        available.remove(prev)
    return available


def process_card(index, card):
    target = card[5:]
    if target.startswith('NEXT'):
        for trial in itertools.count(index):
            trial %= len(BOARD)
            if target == 'NEXTRAIL' and BOARD[trial][0] == 'R':
                return trial
            if target == 'NEXTUTIL' and BOARD[trial][0] == 'U':
                return trial
    elif target.startswith('-'):
        return index - int(target[1:])
    else:
        return BOARD.index(target)


def simulate_game(turns, counting_dict):
    index = 0
    previous_rolls = []
    previous_cc_cards = []
    previous_ch_cards = []

    for i in range(turns):
        index = move(index, previous_rolls,
                     previous_cc_cards, previous_ch_cards)
        counting_dict[index] += 1
    return counting_dict


def main():
    hits = collections.defaultdict(int)
    simulate_game(REPEATS, hits)
    top_hits = sorted(hits.items(), key=lambda x: x[1], reverse=True)[:3]
    print(''.join('%02d' % a for a, _ in top_hits))


if __name__ == '__main__':
    main()
