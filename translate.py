##################
##  Vit Pavlik  ##
##   xpavli0a   ##
##    251301    ##
##     2024     ##
##################

#
# translate program accompanying sudoku.py
# used python version: Python 3.12.3 (GCC 13.1.0) on Debian 12.5
#
# instead of encoding line `1 2 3` as a variable 123, I encoded it as
# 1 * 81 + 2 * 9 + 3 (see get_index in sudoku.py)
#
# to comply with the assignment, I made this tool to translate my encoding
# to the desired encoding
#
# use like this: python3 translate.py < my_encoding.txt > desired_encoding.txt
#
import sys
import re
import math


def sign(n) -> int:
    return int(math.copysign(1, n))


def handle_line_with_numbers(line: str) -> None:
    """translates numbers, fills missing numbers, prints"""
    translated_numbers = []
    for token in line.split():
        number = translate_number(token)
        translated_numbers.append(number)
    absolute_values = [abs(n) for n in translated_numbers]
    for i in range(1000):
        if i not in absolute_values:
            translated_numbers.append(-i)
    translated_numbers.sort(key=lambda n: abs(n))
    if translated_numbers[0] == 0:
        translated_numbers.pop(0)
    translated_numbers.append(0)
    print(" ".join([str(n) for n in translated_numbers]))


def translate_number(number: str) -> int:
    """returns the translated number"""

    if number == "0":
        return 0

    if re.match(r"-?\d+", number) is not None:
        n = abs(int(number)) - 1
        y = n // (9 * 9)
        x = (n - y * 9 * 9) // 9
        value = n % 9            + 1
        translated = (y + 1) * 100 + (x + 1) * 10 + value
        translated *= sign(int(number))
        assert isinstance(translated, int)
        # print(f"translated {number} to {translated}", file=sys.stderr)
        return translated
    else:
        raise ValueError("unexpected format: expected only numbers on the "
                         "second line")


text = sys.stdin.read()

for line in text.splitlines():
    if re.match(r"-?\d+", line) is not None:
        handle_line_with_numbers(line)
    else:
        print(line)
