import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(mydeck)
    return [mydeck[i*n:(i+1)*n] for i in range(numhands) if (i+1)*n <= 52]

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_list, max_val = [], None
    key = key or (lambda x: x)
    for itr in iterable:
        itr_val = key(itr)
        if not max_list or itr_val > max_val:
            max_list, max_val = [itr], itr_val
        elif itr_val == max_val:
            max_list.append(itr)
    return max_list

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    res = sorted(['--23456789TJQKA'.index(r) for r, s in cards], reverse=True)
    return [5, 4, 3, 2, 1] if [14, 5, 4, 3, 2] == res else res

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return len(set(ranks)) == 5 and ranks[0] - ranks[4] == 4


def flush(hand):
    "Return True if all the cards have the same suit."
    return len(set([s for r, s in hand])) == 1


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    from collections import Counter
    return next(iter([r for r, c in Counter(ranks).most_common() if c == n]), None)


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    from collections import Counter
    l = [r for r, c in Counter(ranks).most_common(2) if c == 2]
    return tuple(sorted(l, reverse=True)) if len(l) == 2 else None


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush -> ['6C', '7C', '8C', '9C', 'TC'] 
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert len(deal(10, 5)) == 10
    assert len(deal(10, 5)[9]) == 5
    assert len(deal(3, 26)) == 2
    assert len(deal(3, 26)[0]) == 26

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(al) == [5, 4, 3, 2, 1]

    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + [fk]*99) == [sf]

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)

    return 'tests pass'

print(test())
