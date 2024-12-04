import re
import functools

FILE_PATH = './input.txt'
PATTERN = r'mul\(\d+,\d+\)'
SEC_PATTERN = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

def get_matches(text):
    matched_list = re.findall(PATTERN, text)
    return matched_list

def multiply_string(inp_str):
    two_num_string = re.search(r'\d+,\d+', inp_str)
    if two_num_string != None:
        list_num_str = two_num_string[0].split(',')
        return (int(list_num_str[0]) * int(list_num_str[1]))
    else:
        return 0

def first_process(list_matches):
    prods = list(map(multiply_string, list_matches))
    #print(prods, list_matches)
    sum = functools.reduce(lambda a, b: a + b, prods)
    return sum

def remove_dont(list_matches):
    indices = []
    begin = ""
    for i in range(len(list_matches)):

        if list_matches[i] == "don't()":
            begin += f'{i}:'
        elif list_matches[i] == "do()":
            begin += f'{i+1}'
            indices.append(begin)
            begin = ""
    #print(indices)
    copied_matches = list_matches.copy()
    print(indices)
    for index in indices[-1:0:-1]:
        print(index, indices[-1])
        split_ind_str = index.split(":")
        if len(split_ind_str) > 1:
            ind_one = int(split_ind_str[0])
            ind_two = int(split_ind_str[-1])

            del copied_matches[ind_one:ind_two]
        else:
            print(split_ind_str, copied_matches[int(index)])
            

    #print(copied_matches, list_matches)
    return copied_matches

with open(FILE_PATH) as file:
    text = file.read()
    #print(text)
    matches = get_matches(text)
    first_ans = first_process(matches)
    print("First answer:", first_ans)

with open(FILE_PATH) as file:
    text = file.read()
    print(text)
    matches = re.findall(SEC_PATTERN, text)
    print(matches[709:])
    cleaned_matches = remove_dont(matches)
    sec_ans = first_process(cleaned_matches)
    print("Second answer:", sec_ans)
