num_set = [1,4,7,3,8,9,5]

def sum_with_recursion(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + sum_with_recursion(num[1:])

def answer(vari):
    print(sum_with_recursion(vari))

answer(num_set)