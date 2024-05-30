##################
##  Vit Pavlik  ##
##   xpavli0a   ##
##    251301    ##
##     2024     ##
##################

#
# a view program accompanying sudoku.py
# used python version: Python 3.12.3 (GCC 13.1.0) on Debian 12.5
#
# also checks if the model is valid
#
# expects SAT output from minisat
# tested with Debian package minisat 1:2.2.1-5+b3 (bookworm)
#
from itertools import combinations
from typing import List
import sys

template = """
#########################
# x x x | x x x | x x x #
# x x x | x x x | x x x #
# x x x | x x x | x x x #
#-------|-------|-------#
# x x x | x x x | x x x #
# x x x | x x x | x x x #
# x x x | x x x | x x x #
#-------|-------|-------#
# x x x | x x x | x x x #
# x x x | x x x | x x x #
# x x x | x x x | x x x #
#########################
"""

class Position:
    """class representing a number on a position"""
    def __init__(self, token: str) -> None:
        num = int(token) - 1
        y = num // (9 * 9)
        x = (num - y * 9 * 9) // 9
        value = num % 9 + 1
        segment = 3 * (y // 3) + (x // 3)
        # print(f"{num} {x=} {y=} {value=}")
        self.x = x
        self.y = y
        self.value = value
        self.num = num
        self.segment = segment


input_text = sys.stdin.read()

assert "unsat" not in input_text.lower()

positions: List[Position] = []

for token in input_text.split():
    if token.isdigit() and token != "0":
        positions.append(Position(token))

positions.sort(key=lambda p: p.num)

assert len(positions) == 81, "there must be 81 true variables..."

for pos in positions:
    template = template.replace("x", str(pos.value), 1)

# perform checks
error_found = False
for p, q in combinations(positions, 2):
    if p.x == q.x and p.value == q.value:
        error_found = True
        print(f"conflicting numbers {p.value} in column {p.x + 1}")
    if p.y == q.y and p.value == q.value:
        error_found = True
        print(f"conflicting numbers {p.value} in row {p.y + 1}")
    if p.segment == q.segment and p.value == q.value:
        error_found = True
        print(f"conflicting numbers {p.value} in segment {p.segment + 1}")
if error_found:
    print("errors were found")
else:
    print("no errors found")


print(template)
if error_found:
    print("errors were found")
