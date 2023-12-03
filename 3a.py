import re

digits = re.compile(r"(\d+)")

with open("3") as f:
    data = [line.strip() for line in f]


def has_adjacent_symbols(x_pos: int, y_pos: int) -> bool:
    for x in [x_pos - 1, x_pos, x_pos + 1]:
        if 0 <= x < len(data):
            for y in [y_pos - 1, y_pos, y_pos + 1]:
                if 0 <= y < len(data[0]):
                    if not data[y][x].isdigit() and data[y][x] != ".":
                        return True
    return False


parts = []

for y, line in enumerate(data):
    for match in digits.finditer(line):
        number = int(match.group())
        start, end = match.span()
        for x in range(start, end):
            if has_adjacent_symbols(x, y):
                parts.append(number)
                break
print(sum(parts))
