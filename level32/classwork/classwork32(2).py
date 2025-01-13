def multiply_array(arr):
    result = 1
    for num in arr:
        result *= num
    return result

numbers = [1, 2, 3, 4]
print(multiply_array(numbers)) 
