import re
import time

def main():
    # get the start time
    st = time.time()
    puzzle_input = open("day2_input.txt")
    final_set_answer_1 = []
    final_set_answer_2 = []
    regex_pattern = r"(\s\d+\sblue|\s\d+\sred|\s\d+\sgreen)"
    for line in puzzle_input:
        help_dict = {
                "red" : [],
                "blue" : [],
                "green" : []
        }
        colour_find = re.findall(regex_pattern,line)
        for ball in colour_find:
            help_dict[ball.split()[1]].append(int(ball.split()[0]))
        if(sorted(help_dict["red"])[-1] <= 12 and sorted(help_dict["green"])[-1] <= 13 and sorted(help_dict["blue"])[-1] <= 14):
                final_set_answer_1.append(int(line.split()[1].strip(":")))
        final_set_answer_2.append(sorted(help_dict["red"])[-1] * sorted(help_dict["green"])[-1] * sorted(help_dict["blue"])[-1])
    print(sum(final_set_answer_1))
    print(sum(final_set_answer_2))
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time*1000000, 'microseconds')

main()
