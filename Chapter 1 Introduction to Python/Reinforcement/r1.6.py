from typing import List, Tuple, Optional, Any

def negative_to_positive_index(data: List[Any], k: int) -> Optional[Tuple[Any, int]]:
    """
    A function that provides the equivalent positive index with the value from the list upon providing the negative index
    """
    if k >= 0 or (-(k) > len(data)): 
        raise ValueError("The index should be negative and within the range -n <= k < 0")

    positive_index = len(data) + k

    if data[k] == data[positive_index]:
        return (data[positive_index], positive_index)
    
    return None

print(f'The positive index for negative index {-1} is ', negative_to_positive_index([3,4,8,92,5,2], -1))