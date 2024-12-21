a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"\nOriginal numbers: a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After swapping with temp variable: a = {a}, b = {b}")

a, b = b, a

a = a + b
b = a - b
a = a - b
print(f"After swapping without temp variable: a = {a}, b = {b}")

a, b = b, a

a, b = b, a
print(f"After swapping using tuple assignment: a = {a}, b = {b}")
