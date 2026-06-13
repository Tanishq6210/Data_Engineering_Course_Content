# Module - It is simply a python file containing code

# How to use methods or functions created in another file
# Method 1: import module

import utils.math_util as mu

# print(f'Addition: {math_util.add(2, 3)}')
# print(f'Addition: {math_util.subtract(2, 3)}')
# print(f'Addition: {math_util.multiply(2, 3)}')
# print(f'Addition: {math_util.divide(2, 3)}')

# Method 2 - from module import a function
# from math_util import divide, add

# print(divide(10,2))
# print(add(2, 3))

# Method 3 -> Aliasing with as
# Why Aliasing -> shorter code, easier to read, common in data engineering
# import math_util as mu
# print(mu.add(2, 3))
# print(mu.subtract(2, 3))


if __name__ == "__main__":
    print(__name__)
    print("Hello main!")