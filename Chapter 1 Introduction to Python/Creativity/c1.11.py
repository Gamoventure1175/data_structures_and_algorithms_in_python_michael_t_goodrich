from typing import List, Tuple

def consecutive_even_pairs(sequence: List[int]) -> List[Tuple[int, int]]:
    """
    A function that takes in a non empty list of integers and returns a list of pairs of consecutive integers from the given list such that their product is an even number     
    """

    if not sequence:
        raise ValueError("The sequence cannot be empty")
    
    pairs: List[Tuple[int, int]] = []

    for i in range(1, len(sequence)):
        a, b = sequence[i-1], sequence[i]
        if a%2 == 0 or b%2 == 0:
            pairs.append((a,b))

    return pairs

print(consecutive_even_pairs([8,3,9,4,6,2]))