def add_one(x):
    return x + 1
def use_func(func, num):
    return add_one(num) **2
print(use_func(add_one, 0))