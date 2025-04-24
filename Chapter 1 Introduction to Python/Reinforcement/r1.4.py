def positive_int_sum(num: int) -> int:
    """
    A function that takes a positive integer (num) and returns the sum of the square of all the even positive integers before num
    """
    if num <= 0:
        raise ValueError("Integer entered must be a positive integer")
    
    even_positive = 2
    sum_val = 0

    while even_positive < num:
        sum_val += pow(even_positive, 2)
        even_positive += 2

    return sum_val

print(positive_int_sum(8))