import sys
import os

def parsecard(card):
    parsedcard = []
    for field in range((len(card) - 1) / 8):
        parsedcard.append(card[8 * field : 8 * (field + 1)])
    return tuple(parsedcard)

def dvcrel1(eid, pid, elemtype):
    return['$HMNAME DVPRELS '+str(eid).ljust(8)+'DVCREL1_'+str(eid)+'\n',
            'DVCREL1 '+str(eid).ljust(8)+str(elemtype).ljust(8)+str(eid).rjust(8)+'   ZOFFS                0.0     \n',
            '+       '+str(pid).ljust(8)+'0.5     \n']

def ctria3(card):
    elemtype, eid, pid, g1, g2, g3, theta, zoffs = parsecard(card)
    if zoffs == '        ':
        return []
    else:
        return dvcrel1(int(eid), int(pid), elemtype)

def ctria6(cards):
    elemtype, eid, pid, g1, g2, g3, g4, g5, g6 = parsecard(cards[0])
    blank, theta, zoffs, t1, t2, t3 = parsecard(cards[1])
    if zoffs == '        ':
        return []
    else:
        return dvcrel1(int(eid), int(pid), elemtype)

def cquad4(card):
    elemtype, eid, pid, g1, g2, g3, g4, theta, zoffs = parsecard(card)
    if zoffs == '        ':
        return []
    else:
        return dvcrel1(int(eid), int(pid), elemtype)

def cquad8(cards):
    elemtype, eid, pid, g1, g2, g3, g4, g5, g6 = parsecard(cards[0])
    blank, g7, g8, t1, t2, t3, t4, theta, zoffs = parsecard(cards[1])
    if zoffs == '        ':
        return []
    else:
        return dvcrel1(int(eid), int(pid), elemtype)
    
if __name__ == '__main__':
    femdeck = open(sys.argv[1], 'r')
    femcards = femdeck.readlines()
    femdeck.close()
    carditer = iter(femcards)
    dvcrels = []
    for card in carditer:
        if card.startswith('CTRIA3'):
            dvcrels.extend(ctria3(card))
        elif card.startswith('CQUAD4'):
            dvcrels.extend(cquad4(card))
        elif card.startswith('CTRIA6'):
            dvcrels.extend(ctria6((card, carditer.next())))
        elif card.startswith('CQUAD8'):
            dvcrels.extend(cquad8((card, carditer.next())))
    dvcreldeck = open(sys.argv[2], 'w')
    dvcreldeck.writelines(dvcrels)
    dvcreldeck.close()
