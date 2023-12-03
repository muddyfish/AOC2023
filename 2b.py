import re

game_re = re.compile(r"^Game (\d+):(.+)\n?")
red_re = re.compile("(\d+) red")
green_re = re.compile("(\d+) green")
blue_re = re.compile("(\d+) blue")


def get_count(regex, text: str) -> int:
    result = regex.search(text)
    if result is None:
        return 0
    return int(result.group(1))

value = 0


with open("2") as f:
    for line in f:
        game_id, rest = game_re.match(line).groups()
        game_id = int(game_id)
        rounds = rest.split(";")
        reds = []
        blues = []
        greens = []
        for round in rounds:
            reds.append(get_count(red_re, round))
            greens.append(get_count(green_re, round))
            blues.append(get_count(blue_re, round))

        max_red = max(reds)
        max_green = max(greens)
        max_blue = max(blues)

        value += max_red * max_green * max_blue

print(value)