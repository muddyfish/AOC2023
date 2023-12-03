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


passed_games = []

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

        if max_red > 12 or max_blue > 14 or max_green > 13:
            pass
        else:
            passed_games.append(game_id)

print(sum(passed_games))
