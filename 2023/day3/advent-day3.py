import re
lines = []

fname = 'day3-sample-input.txt'
input_file = open(fname)

for line in input_file:
    lines.append(line)

# @param top: the top line to be checked
# @param mid: the middle line which is the one to be summed
# @param bot: the bottom line to be checked
# @return: the sum of valid parts from the 'mid' line
def sum_line(top, mid, bot):
    sum = 0
    if top is None:
        pass
    elif bot is None:
        pass
    else:
        valid_digit = re.compile("[0-9]{2,3}")
        valid_symbol = re.compile("\*|\$|\/")
        matches = valid_digit.findall(mid)
        # print(matches)
        for match in matches:
            pos = mid.find(match)
            print("pos: " + str(pos))
            if pos != 0 or pos != len(mid)-1:
                print("l: " + mid[pos-1] + " r: " + mid[pos+1])

# @param arr: array of strings where each element is a sequential line of input
# ex: line 0 of input file = arr[0], line 1 = arr[0], etc...
# @return the sum of all valid parts in input file
def sum_parts(array):
    return 0

# top = None
# mid = None
# bot = None
# for num in range(len(lines)):
#     if num == 0:
#         mid = lines[num]
#         bot = lines[num+1]
#         pass
#     elif num == len(lines)-1:
#         pass
#     else:
#         pass
# print(len(lines))

sum_line(lines[1], lines[2], lines[3])
