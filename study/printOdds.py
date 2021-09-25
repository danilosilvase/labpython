from itertools import groupby


def find_odd_number(input_array) -> list:
        grouped_numbers = [list(value) for item, value in groupby(input_array)]
        list_odd_count_numbers = (x for x in grouped_numbers if len(x) % 2 != 0)
        return list_odd_count_numbers

def print_odd_numbers(odd_number):
    # for items in odd_number:
    #     print(items[0])
    print(max(odd_number)[0])

def main():

    input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3, 7, 7, 7, 8, 8]
    array = find_odd_number(input_array)
    print_odd_numbers(array)

    
if __name__ == "__main__":
    main()