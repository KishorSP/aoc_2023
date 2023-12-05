import re
import time

def main():
    # get the start time
    st = time.time()
    help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    puzzle_input = open("day1_input.txt")
    list_of_nums = []
    regex_pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d{1}))"
    
    for line in puzzle_input:
        num_find = re.findall(regex_pattern,line)
        first_num = num_find[0] if num_find[0].isnumeric() else help_dict[num_find[0]]
        second_num = num_find[-1] if num_find[-1].isnumeric() else help_dict[num_find[-1]]
        list_of_nums.append(int(first_num+second_num))
    print(sum(list_of_nums))
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time*1000000, 'microseconds')

main()
