#even or odd
def is_even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even(n - 2)

print(7, "even" if is_even(7) else "odd")
print(10, "even" if is_even(10) else "odd")


