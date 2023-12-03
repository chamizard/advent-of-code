# Part one solution
# uncomment replace appropriate text for your input and run
"""
# constants for readability
RED = 0
GREEN = 1
BLUE = 2
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
# @arg to_parse: input line read from file
# @return: id of valid game or 0 if invaild game
def check_game(to_parse):
    first_parse = to_parse.lstrip('Game ')
    # print("first parse: " + first_parse)
    id = first_parse.split(':')[0]
    # print(id)
    second_parse = first_parse.lstrip('1234567890:')
    # print("second_parse: " + second_parse)
    bags = second_parse.split(';')
    # print("og line: " + to_parse)
    for bag in bags:
        print("bag: " + bag)
        if 'red' in bag:
            print("red in bag: " + bag[bag.find('red')-2])
            if int(bag[bag.find('red')-3] + bag[bag.find('red')-2]) > MAX_RED:
                return 0
        if 'green' in bag:
            if int(bag[bag.find('green')-3] + bag[bag.find('green')-2]) > MAX_GREEN:
                return 0
        if 'blue' in bag:
            if int(bag[bag.find('blue')-3] + bag[bag.find('blue')-2]) > MAX_BLUE:
                return 0
    # print("red: " + str(counts[RED]))
    # print("green: " + str(counts[GREEN]))
    # print("blue: " + str(counts[BLUE]))
    return int(id)

# replace this with the name of your file
# file must be in same directory
fname = 'day2-input.txt'
input_file = open(fname, 'r')
sum = 0
for line in input_file:
    result = check_game(line)
    print(result)
    sum += result

print("Sum: " + str(sum))
input_file.close()
"""
# Part two solution below
# uncomment replace appropriate text for your input and run
"""
# @arg to_parse: input line read from file
# @return: power = minimum allowed values of each color per line/game
def game_power(to_parse):
    to_parse = to_parse.strip()
    first_parse = to_parse.lstrip('Game ')
    # print("first parse: " + first_parse)
    id = first_parse.split(':')[0]
    # print(id)
    second_parse = first_parse.lstrip('1234567890:')
    # print("second_parse: " + second_parse)
    bags = second_parse.split(';')
    if bags[1] == '':
        print('Single value')
    # print("og line: " + to_parse)
    min_red = 1
    min_green = 1
    min_blue = 1
    for bag in bags:
        # print("bag: " + bag)
        bag_items = bag.split(',')
        for item in bag_items:
            # print("item: " + item)
            if 'red' in item:
                val = item.removesuffix(' red')
                # print("red val: " + val)
                if int(val) > min_red:
                    min_red = int(val)
            if 'green' in item:
                val = item.removesuffix('green')
                # print(val)
                if int(val) > min_green:
                    min_green = int(val)
            if 'blue' in item:
                val = item.removesuffix(' blue')
                if int(val) > min_blue:
                    min_blue = int(val)
    return min_red * min_green * min_blue

# replace this with the name of your file
# file must be in same directory
fname = 'day2-input.txt'
input_file = open(fname, 'r')
sum = 0
for line in input_file:
    result = game_power(line)
    # print(result)
    sum += result

print("Sum: " + str(sum))
input_file.close()
"""