from __future__ import division
import itertools
import sys
from numpy import matrix

def parse_pools(pool_strings):
    pools = {}
    pools['win'] = [int(x) for x in pool_strings[0].split(',')]
    pools['place'] = [int(x) for x in pool_strings[1].split(',')]
    pools['show'] = [int(x) for x in pool_strings[2].split(',')]
    try:
        assert len(pools['win']) == len(pools['place']) == len(pools['show']) > 3
        return pools
    except AssertionError:
        print('inconsistent')
        sys.exit()

def outlay(bets):
    bankroll = 0
    for k in bets:
        bankroll += sum(bets[k])
    return bankroll

if __name__ == '__main__':
    vig = float(sys.argv[1])
    pools = parse_pools(sys.argv[2:5])
    n = len(pools['win'])
    bets = {}
    pots = {}
    for k in pools:
        bets[k] = [x for x in pools[k]]
    for k in pools:
        pots[k] = (1 - vig) * (sum(pools[k]) + sum(bets[k]))
    outcomes = list(itertools.permutations(range(n), 3))
    bankroll = outlay(bets)

    for w, p, s in outcomes:
        winner = pots['win'] * bets['win'][w] / (bets['win'][w] + pools['win'][w])
        placers = pots['place'] * (bets['place'][w] + bets['place'][p]) / (bets['place'][w] + pools['place'][w] + bets['place'][p] + pools['place'][p])
        showers = pots['show'] * (bets['show'][w] + bets['show'][p] + bets['show'][s]) / (bets['show'][w] + pools['show'][w] + bets['show'][p] + pools['show'][p] + bets['show'][s] + pools['show'][s])
        print((winner + placers + showers - bankroll) / bankroll)
