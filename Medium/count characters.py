def count_characters():
    upper_count, lower_count, number_count = 0, 0, 0
    while (char := input("Enter a character: ")) != '*':
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            number_count += 1
    print(f"\nUppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
    print(f"Numbers: {number_count}")

count_characters()
