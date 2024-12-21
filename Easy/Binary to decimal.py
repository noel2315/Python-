def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_octal(binary):
    decimal = int(binary, 2)
    return oct(decimal)[2:]

print("Choose an option:")
print("1. Convert binary to decimal")
print("2. Convert binary to octal")
choice = int(input("Enter your choice (1 or 2): "))

binary = input("Enter a binary number: ")

if choice == 1:
    result = binary_to_decimal(binary)
    print(f"Decimal equivalent: {result}")
elif choice == 2:
    result = binary_to_octal(binary)
    print(f"Octal equivalent: {result}")
else:
    print("Invalid choice. Please select either 1 or 2.")
