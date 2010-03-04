nums = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

tot = 0
for i in range(1, 1001):
    if i in nums:
        tot += len(nums[i])
    elif i < 100:
        tot += len(nums[(i//10)*10])
        tot += len(nums[i%10])
    elif i < 1000:
        tot += len(nums[(i//100)])
        tot += len('hundred')
        if i % 100 != 0:
            tot += len('and')
            if i % 100 in nums:
                tot += len(nums[i%100])
            elif i % 100 // 10 != 0:
                tot += len(nums[(i%100//10)*10])
            if i % 100 % 10 != 0 and i % 100 not in nums:
                tot += len(nums[i%100%10])
    elif i == 1000:
        tot += len('onethousand')

print tot        

