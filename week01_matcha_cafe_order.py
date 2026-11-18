print("Welcome to Nat'Cho Matcha")
print("-" * 30)

cafe = "Nat'Cho Matcha"         #str
tea_origin = "Kagoshima, Japan" #str
latte_price = 6                 #int
student_latte_price = 4.5       #float
cups_sold_today = 0             #int
is_open = True                  #bool

print(type(cafe), type(latte_price), type(cups_sold_today), type(is_open))
print(f"Our matcha comes from {tea_origin}.")
print(f"A matcha latte costs £{latte_price:.2f}.")
print(f"A student matcha latte costs £{student_latte_price:.2f}.")

name = input("What's your name? ")
student = input("Are you a student? (Yes/No)")
quantity = int(input("How many matcha lattes would you like? "))

if student.lower() == "yes":
    total = student_latte_price * quantity
else:
    total = latte_price * quantity

cups_sold_today = cups_sold_today + quantity

print("-" * 30)
print(f"Thanks {name}! {quantity} x matcha latte = £{total:.2f}")
print(f"Cups sold today at {cafe}: {cups_sold_today}")

