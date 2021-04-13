def judge_class(num):
    for id in range(num):
        if id < 10:
            print('this is a kind of animal')
            if id % 2 ==1:
                print('this is a cat')
            else:
                print('this is a dog')
        else:
            print('this is not a kind of animal')


def sum_int(n):
    res = 0
    for ii in range(n):
        res = res + ii 
        if res > 10000:
            res = res -10000
    return res


print(sum_int(10))
judge_class(5)