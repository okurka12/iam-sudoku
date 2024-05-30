##################
##  Vit Pavlik  ##
##   xpavli0a   ##
##    251301    ##
##     2024     ##
##################

#
# a view program accompanying sudoku.py
#
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
        value = num % 9
        print(f"{num} {x=} {y=} {value=}")
        self.x = x
        self.y = y
        self.value = value
        self.num = num


input_text = sys.stdin.read()

positions: List[Position] = []

for token in input_text.split():
    if token.isdigit() and token != "0":
        positions.append(Position(token))

positions.sort(key=lambda p: p.num)

assert len(positions) == 81, "there must be 81 true variables..."

for pos in positions:
    template = template.replace("x", str(pos.value), 1)

print(template)
