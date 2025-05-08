def harmonic(n):
    """A function that takes a number n and returns back the harmonic sum of n using recursion"""
    if n == 1:
        return 1
    
    return 1/n + harmonic(n-1)


print(harmonic(100))