#!/usr/bin/env python3

def my_map(my_func, my_list):
    result = []
    for i in my_list:
        result.append(my_func(i))
    return result

res = my_map(lambda x: x * 2, [1, 2, 3])
print(res)
