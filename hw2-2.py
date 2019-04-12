# ------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools
import time

def timing(func):
    def new_func():
        t0 = time.clock()
        res = func()
        print('run time: {:f} s'.format(time.clock()-t0))
        return res
    return new_func

def floor_puzzle():
    return ((
        [h, k, l, p, r]
        for l in (2, 3, 4)
        for k in (2, 3, 4, 5)
        if abs(k-l) > 1
        for r in range(1, 6)
        if abs(r-l) > 1
        for h in (1, 2, 3, 4)
        for p in range(1, 6)
        if set((h, k, l, p, r)) == set((1, 2, 3, 4, 5))
    ))

@timing
def show_all():
    for i in floor_puzzle():
        print(i)

show_all()