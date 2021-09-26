# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2
# 1, 1 appears twice so even
# 2, 2, 2 appears three times so odd
# even is divisible by 2


# from itertools import groupby 

# def get_odd(input_array) -> list:
#     grouped_list = [list(grouped_numbers) for item, grouped_numbers in groupby(input_array)]
#     odd_number_list = [odd_times for odd_times in grouped_list if len(odd_times) % 2 != 0]
#     return odd_number_list


# def main():
#     input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3, 3]
#     print_array = get_odd(input_array)
#     for item in print_array:
#         print(item[0])
#     # print(max(print_array)[0])
    
# if __name__ =="__main__":
#     main()

from collections import Counter

def odd_number_times(input_array):
    grouped_values = Counter(input_array).most_common(3)
    odd_times_list = [number for number, count in grouped_values if count % 2 != 0]
    return odd_times_list
    
def main():
    input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3,7, 7, 7, 7, 7]
    result = odd_number_times(input_array)
    for number in result:
        print(number)
    
if __name__ == "__main__":
    main()
