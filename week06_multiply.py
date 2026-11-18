nums = [1, 2, 3, 4, "hello", 1.5]

def mult(numbers):
    result = 1
    for i in numbers:
        if isinstance(i, (int, float)):
            result = result * i

    return result

#print(multiply(nums))