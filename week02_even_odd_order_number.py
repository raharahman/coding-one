number = float(input("Enter your order number: "))

if number != int(number):
    print("Neither even nor odd - it's a fraction.")
elif number % 2 == 0:
    print("That's even - you've won the Nat'Cho Matcha Kagoshima Morning sticker!")
else:
    print("That's odd - you've won the Nat'Cho Matcha Kagoshima Night Sticker")