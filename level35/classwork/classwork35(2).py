def even_numbers(arr, number):
    return [x for x in arr if x % 2 == 0][-number:]
