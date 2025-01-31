# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text: str):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here+
    if text == '': return (0 ,0)
    text = text.lower()
    res = (1, (0, 1))
    for ml in range(len(text)):
        for mr in (ml, ml+1):
            if mr >= len(text): continue
            lo, hi = ml, mr
            while 0 <= lo and hi < len(text) and text[lo] == text[hi]:
                lo -= 1
                hi += 1
            if hi-lo-1 > res[0]: res = (hi-lo-1, (lo+1, hi))
    
    return res[1]
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())