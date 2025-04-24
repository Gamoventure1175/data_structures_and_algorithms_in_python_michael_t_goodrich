from typing import List

def unique_number_count(seq:List[int]) -> int:
    '''
    A function that takes in a list of integers and returns the count of unique numbers in the list
    '''
    if not seq:
        raise ValueError("The list of integers cannot be empty")
    
    return len(set(seq))
    
    
print(f'The number of unique numbers in the list {[2,6,6,2,6]} is {unique_number_count([2,6,6,2,6])}')