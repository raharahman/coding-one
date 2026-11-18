# Task 1: sum of multiples
first = int(input("First number: "))
second = int(input("Second number: "))
multiple = int(input("Multiple of: "))

total = 0
for number in range(first + 1, second):
    if number % multiple == 0:
        total += number
print("Sum:", total)
print()

#Task 2: count each letter
text = input("Type some text: ")
text = text.lower()

result =""
for letter in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for character in text:
        if character == letter:
            count += 1
    result = result + letter + ":" + str(count) + ","

print(result)
print()

#Task 3: division with subtraction
dividend = int(input("Number to divide (e.g. cups): "))
divisor = int(input("Divide by (e.g. tables): "))

if divisor <= 0:
    print("Can only divide by a positive whole number.")
else:
    remaining = dividend
    times = 0
    steps = str(dividend)
    while remaining >= divisor:
        remaining = remaining - divisor
        times = times + 1
        steps =steps + "-" + str(divisor)

    print(steps + "=" + str(remaining))
    print("Result:", times, "remainder", remaining)
