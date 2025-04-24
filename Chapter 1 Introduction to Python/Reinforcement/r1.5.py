def comprehension_based_sum(num: int) -> int:
    """
    A function that takes a postive integer (num) and returns the sum of all the positive even integers before it using pythons comprehension mechanism
    """
    if num <= 0:
        raise ValueError("The number should be a positive integer")

    return sum([x*x for x in range(2, num, 2)])

print(comprehension_based_sum(118))