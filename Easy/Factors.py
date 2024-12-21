def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

number = int(input("Enter a number: "))

factors = count_factors(number)
print(f"The number of factors of {number} is: {factors}")
