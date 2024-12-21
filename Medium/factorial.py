def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def main():
    n = int(input("Enter a number: "))
    
    fact = factorial(n)
    print(f"Factorial of {n} is: {fact}")
    
    factors = count_factors(n)
    print(f"Number of factors of {n} is: {factors}")

if __name__ == "__main__":
    main()
