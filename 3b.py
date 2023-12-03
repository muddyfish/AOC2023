import re
from math import prod
from collections import defaultdict
from typing import Optional, Tuple

digits = re.compile(r"(\d+)")

with open("3") as f:
    data = [line.strip() for line in f]


def has_adjacent_symbols(x_pos: int, y_pos: int) -> Optional[Tuple[int, int]]:
    for x in [x_pos - 1, x_pos, x_pos + 1]:
        if 0 <= x < len(data):
            for y in [y_pos - 1, y_pos, y_pos + 1]:
                if 0 <= y < len(data[0]):
                    if data[y][x] == "*":
                        return x, y


gears = defaultdict(list)

for y, line in enumerate(data):
    for match in digits.finditer(line):
        number = int(match.group())
        start, end = match.span()
        for x in range(start, end):
            if position := has_adjacent_symbols(x, y):
                gears[position].append(number)
                break

print(sum(prod(values) for values in gears.values() if len(values) == 2))
