# Task 1: multiply every number in a list
def multiply_list(items):
    result = 1
    for item in items:
        if type(item) == int or type(item) == float:
            result *= item
    return result

print(multiply_list([1,2,3,4]))
print(multiply_list([2, "matcha", 5, None, 3]))

#Task 2: every 2 word combination
def word_pairs(words):
    pairs = []
    for first in words:
        for second in words:
            if first != second:
                pairs.append(first + " " + second)
    return pairs

print(word_pairs(["comfortable", "round", "support", "machinery"]))

#class task 1 - keeping only unique values
def unique(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
print(unique(["matcha", "latte", "matcha", "hojicha", "latte"]))

#class task 2: rotate a list left or right
def rotate_left(items, k):
    k = k % len(items)
    return items[k:] + items[:k]

def rotate_right(items, k):
    k = k % len(items)
    return items[-k:] + items[:-k]

menu = ["matcha", "hojicha", "sencha", "genmaicha"]
print(rotate_left(menu, 1))
print(rotate_right(menu, 1))

#class task 3: biggest sum of numbers
def largest_sum(numbers):
    best = numbers[0]
    for start in range(len(numbers)):
        total = 0
        for end in range(start, len(numbers)):
            total = total + numbers[end]
            if total > best:
                best = total
    return best
print(largest_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

