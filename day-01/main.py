import re

PATH = 'input.txt'

def split_into_nums(text):
    text = text.replace("\n", "")
    nums = re.split(" +", text)
    nums = list(map(lambda x: int(x), nums))
    return nums

def get_two_lists(lines):
    list_one = [split_into_nums(line)[0] for line in lines]
    list_two = [split_into_nums(line)[1] for line in lines]

    return list_one, list_two

def compare_lists(list_one, list_two):
    copy_one = list_one.copy()
    copy_two = list_two.copy()

    copy_one.sort()
    copy_two.sort()

    total = 0

    for i in range(len(copy_one)):
        if copy_one[i] >= copy_two[i]:
            total += copy_one[i] - copy_two[i]
        else:
            total += copy_two[i] - copy_one[i]

    return total

def sim_score(list_one, list_two):
    copy_one = list_one.copy()
    copy_two = list_two.copy()
    total = 0

    for num in copy_one:
        total += (num * copy_two.count(num))

    return total

with open(PATH) as file:
    lines = file.readlines()
    ##print(lines)
    lst_one, lst_two = get_two_lists(lines)
    final = compare_lists(lst_one, lst_two)
    print("First total:", final)

with open(PATH) as file:
    lines = file.readlines()
    lst_one, lst_two = get_two_lists(lines)
    final = sim_score(lst_one, lst_two)
    print("Second total:", final)

