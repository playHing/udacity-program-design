# --------------
# User Instructions
# 
# Modify the function compile_formula so that the function 
# it returns, f, does not allow numbers where the first digit
# is zero. So if the formula contained YOU, f would return 
# False anytime that Y was 0 

import re
import itertools

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit 
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""
    
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    non_zero_items = set(re.findall(r'\b[A-Z]', formula)) # readability
    parms = ', '.join(letters)
    tokens = list(map(compile_word, re.split('([A-Z]+)', formula)))
    body = ''.join(tokens)
    # non_zero_items = set([token[-2] for token in tokens if '10' in token])
    f = 'lambda {0}: {1} if all([item != 0 for item in [{2}]]) else False' \
            .format(parms, body, ','.join(non_zero_items))
    if verbose: print(f)
    return eval(f), letters

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words uncahanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) 
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word
    
def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def test():
    assert faster_solve('A + B == BA') == None # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') in ('324 == 18**2', '289 == 17**2', '576 == 24**2', '841 == 29**2')
    assert faster_solve('X / X == X') == '1 / 1 == 1'
    print('tests pass')

test()