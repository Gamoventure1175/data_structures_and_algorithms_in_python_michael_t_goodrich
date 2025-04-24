from typing import List

def is_even(k: int) -> bool:
    """A function that takes an integer and determines if it is even (True) or not (False) without using multiplication, division or modulo operator"""
    even_last_digits: List[str] = ['0', '2', '4','6','8']
    k_string: str = str(k)
    return k_string[-1] in even_last_digits

print('Is 2 an even number? ', is_even(2))
print('Is 27 an even number? ', is_even(27))
print('Is 91 an even number? ', is_even(91))