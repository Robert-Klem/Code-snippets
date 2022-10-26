from math import trunc as tc

def is_perf_sq(num):
    x = tc(num**0.5)
    return num == x*x

def is_fibonacci_num(num):
    return is_perf_sq(5*num*num + 4) or is_perf_sq(5*num*num - 4) 

def fibonacci(num):
    n0 = 0
    n1 = 1
    working_sum = 1
    index = 2
    if is_fibonacci_num(num):
        while working_sum != num:
            working_sum = n0 + n1
            n0 = n1
            n1 = working_sum
            index += 1
        print(f'Index is: {index}')
    else:
        while index != num:
            working_sum = n0 + n1
            n0 = n1
            n1 = working_sum
            index += 1
        print(f'Fib. num is: {working_sum}')


fibonacci(34)
