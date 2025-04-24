from typing import List, Tuple

def minmax(data: List[int]) -> Tuple[int, int]:
    """A function that returns the minimum and maximum from a list of numbers in the form of a tuple with two numbers, (min, max) without using the inbuilt functions min and max"""

    if not data: 
        raise ValueError("minmax() arg is an empty sequence")

    data_length = len(data)
    min_val = max_val = data[0]

    for i in range(data_length):
        if data[i] >= max_val:
            max_val = data[i]
        elif min_val >= data[i]:
            min_val = data[i]

    return (min_val, max_val)

print(f'The minimum and maximum values from the given array, {[2,3,4,58,7]} are ', minmax([2,3,4,58,7]))
print(f'The minimum and maximum values from the given array, {[100,22,54,58,7]} are ', minmax([100,22,54,58,7]))
print(f'The minimum and maximum values from the given array, {[-45, -28, -89, -2]} are ', minmax([-45, -28, -89, -2]))    