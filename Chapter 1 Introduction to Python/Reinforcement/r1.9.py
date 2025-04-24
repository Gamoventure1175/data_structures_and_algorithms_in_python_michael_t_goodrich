from random import randrange
from typing import List, TypeVar

T = TypeVar('T')

def custom_random_choice(sample_list: List[T]) -> T:
    """
    A function that takes a list of any generic value and returns a random value from that list
    """
    return sample_list[randrange(len(sample_list))]

print(f'A random number from the list {[1,2,3,4,5]} is {custom_random_choice([1,2,3,4,5])}')