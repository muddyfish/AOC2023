with open("1") as f:
    nums = []
    for line in f:
        digits = [int(i) for i in line.strip() if i.isdigit()]
        nums.append(digits[-1] + 10*digits[0])

print(sum(nums))
