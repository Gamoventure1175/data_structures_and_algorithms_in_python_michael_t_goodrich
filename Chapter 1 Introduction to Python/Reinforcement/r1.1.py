def is_multiple(n: int, m: int) -> bool:
    """A function that takes two integer values and returns True if n is a multiple of m, that is, n = m*i for some integer i or False if it is not"""
    i: int = 1
    while m * i <= n:
        if m * i == n:
            return True
        i += 1
    return False

print("Is 27 multiple of 3? ", is_multiple(27, 3))
print("Is 85 multiple of 7? ", is_multiple(85, 7))
print("Is 81 multiple of 9? ", is_multiple(81, 9))
print("Is 8 multiple of 9? ", is_multiple(8, 9))
print("Is 101 multiple of 9? ", is_multiple(101, 9))


#A more concised version of the code
# def is_multiple(n: int, m: int) -> bool: 
#     return n%m == 0