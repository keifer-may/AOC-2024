FILE_PATH = './input.txt'

def get_levels(line):
    new_line = line.replace('\n', '')
    str_nums = new_line.split(' ')
    nums = [int(x) for x in str_nums]
    return nums

def check_order(nums):
    sorted_nums = nums.copy()
    sorted_nums.sort()
    reversed_nums = nums.copy()
    reversed_nums.sort(reverse=True)

    if (nums == sorted_nums) or (nums == reversed_nums):
        ##print('Ok order', nums)
        return True
    else:
        ##print('Aw hell naw', nums)
        return False

def check_steps(nums):
    steps = list(map(lambda x, y: (x-y)if x>= y else (y - x),nums[:len(nums)-1], nums[1:]))
    ##print(steps)
    outlying_steps = list(filter(lambda x: x < 1 or x > 3, steps))
    ##print(outlying_steps)
    if not outlying_steps:
        return True
    else:
        return False

def first_process_lines(lines):
    sum = 0
    for line in lines:
        nums = get_levels(line)
        ##print(nums)
        ordered = check_order(nums)
        ##print(ordered)
        if ordered:
            steps = check_steps(nums)
            if steps:
                sum += 1
    return sum
        
def second_process_lines(lines):
    sum = 0
    for line in lines:
        steps = False
        nums = get_levels(line)
        ordered = check_order(nums)
        if ordered:
            checking = check_steps(nums)
            if checking:
                sum += 1
            else:
                for i in range(len(nums)):
                    copy_nums = nums.copy()
                    del copy_nums[i]
                    ordered = check_order(copy_nums)
                    if ordered:
                        #print("new ordered")
                        #print(nums, copy_nums)
                        checking = check_steps(copy_nums)
                        if checking:
                            steps = True
                if steps == True:
                    sum += 1
        else:
            steps = False
            for i in range(len(nums)):
                copy_nums = nums.copy()
                del copy_nums[i]
                ordered = check_order(copy_nums)
                if ordered:
                    #print("new ordered")
                    #print(nums, copy_nums)
                    checking = check_steps(copy_nums)
                    if checking:
                        steps = True
            if steps == True:
                sum += 1

    return sum

with open(FILE_PATH) as file:
    lines = file.readlines()
    first_ans = first_process_lines(lines)
    print("First answer:", first_ans)

with open(FILE_PATH) as file:
    lines = file.readlines()
    print(lines)
    sec_ans = second_process_lines(lines)
    print("Second answer:", sec_ans)

