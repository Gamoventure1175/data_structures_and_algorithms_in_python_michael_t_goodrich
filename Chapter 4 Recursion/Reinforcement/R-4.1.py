def recursive_max(input_array, curr_max, index):
    """
    An algorithm that takes an inpurt array of numbers and returns the max element from the array using recursion approach
    """
    
    if index == len(input_array):
        return curr_max
    else:
        curr_max = curr_max if curr_max > input_array[index]  else input_array[index]
        return recursive_max(input_array, curr_max, index+1)

example = [3,6,28,5,2910,3]

max_num = recursive_max(example, 6, 0)

print(max_num)