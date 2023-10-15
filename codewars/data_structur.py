# https://www.codewars.com/kata/56a6ce697c05fb4667000029/train/python
def next_pal(val):
    val += 1 
    while val:
        if str(val) == str(val)[::-1]:
            return val
        val += 1

from itertools import permutations

def find_mult_3(num):
    ls = set()
    for i in range(1, len(str(num))+1):
        for j in set(permutations(str(num), i)):
            ls.add(int(''.join(j)))
    solve = [x for x in ls if x != 0 and x % 3 == 0]
    return [len(solve), max(solve)]

print(find_mult_3(6073))

