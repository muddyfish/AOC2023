number_words = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
)


def all_indexes(needle: str, haystack: str, i: int = 0):
    if needle not in haystack:
        return []
    index = haystack.index(needle)
    return [index + i, *all_indexes(needle, haystack[index + len(needle):], i + index + len(needle))]


with open("1") as f:
    nums = []
    for line in f:
        digits = [(i, int(num)) for i, num in enumerate(line.strip()) if num.isdigit()]
        words = [(index, num) for num, word in enumerate(number_words, 1) for index in all_indexes(word, line.strip())]
        all_digits = [j for i, j in sorted([*digits, *words], key=lambda i: i[0])]
        nums.append(all_digits[0]*10 + all_digits[-1])

print(sum(nums))
