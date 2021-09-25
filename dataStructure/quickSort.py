def quick_sort(input_array):
    if len(input_array) < 2:
        return input_array
    else:
        pivolt = input_array[0]
        less = [i for i in input_array[1:] if i <= pivolt]
        greater = [i for i in input_array[1:] if i > pivolt]
        return quick_sort(less) + [pivolt] + quick_sort(greater)

def main():
    result = quick_sort([10, 5 ,2 ,3])
    print(result)
if __name__=="__main__":
    main()