# Part one solution below

""" 
input_file = open('day1-input.txt', 'r')
sum = 0
for line in input_file:
    parsed_line = ''
    for char in line:
        if char.isnumeric():
            parsed_line += char
    print(parsed_line[0] + "" + parsed_line[len(parsed_line)-1])
    sum += int(parsed_line[0] + parsed_line[len(parsed_line)-1])

print(sum)
input_file.close()
"""

# Part two solution below
"""
number_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

special_cases = ['oneight', 'twone', 'threeight', 'nineight', 'fiveight', 'eighthree', 'eightwo', 'sevenine']
special_case_vals = ['18', '21', '38', '98', '58', '83', '82', '79']

input_file = open('day1-input.txt', 'r')
sum = 0
line_num = 0
# loop through input and parse digits
for line in input_file:
    # check for special cases first
    for num in range(len(special_cases)):
        if special_cases[num] in line:
            line = line.replace(special_cases[num], special_case_vals[num])
    # replace rest of number strings with digits
    for num in range(len(number_strs)):
        line = line.replace(number_strs[num], number_digits[num])
    # parse digits from line
    parsed_line = ''
    for char in line:
        if char.isnumeric():
            parsed_line += char
    # add first + last digit to sum
    sum += int(parsed_line[0] + parsed_line[len(parsed_line)-1])
    line_num += 1

print("Sum: " + str(sum))
print("Total lines: " + str(line_num))
input_file.close()
"""
